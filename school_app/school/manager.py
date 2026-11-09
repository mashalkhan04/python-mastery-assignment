"""The school office logic: add students, add marks, class ranking."""

import logging

from school.grades import average
from school.models import Student, validate_mark

LOGGER = logging.getLogger(__name__)


def find_student(students: list[Student], roll_number: int) -> Student | None:
    """Return the student with this roll number, or None."""
    for student in students:
        if student.roll_number == roll_number:
            return student
    return None


def add_student(students: list[Student], name: str, roll_number: int) -> Student:
    """Create a student and add them to the list. Roll numbers must be unique."""
    if find_student(students, roll_number) is not None:
        raise ValueError(f"Roll number {roll_number} already exists.")
    student = Student(name=name, roll_number=roll_number)
    students.append(student)
    LOGGER.info("Added student %s (roll %d)", name, roll_number)
    return student


def add_marks(students: list[Student], roll_number: int, new_marks: list[float]) -> Student:
    """Add marks to a student. Nothing is added if any mark is invalid."""
    student = find_student(students, roll_number)
    if student is None:
        raise ValueError(f"No student with roll number {roll_number}.")
    for mark in new_marks:
        validate_mark(mark)   # check ALL marks first
    student.marks.extend(new_marks)
    LOGGER.info("Added %d marks to roll %d", len(new_marks), roll_number)
    return student


def class_ranking(students: list[Student]) -> list[Student]:
    """Return students that have marks, highest average first."""
    with_marks = [student for student in students if student.marks]
    return sorted(with_marks, key=lambda student: average(student.marks), reverse=True)
