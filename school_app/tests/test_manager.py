"""Tests for school/manager.py and the Student dataclass."""

import pytest

from school.manager import add_marks, add_student, class_ranking, find_student
from school.models import Student


def test_add_student_and_find_them() -> None:
    students: list[Student] = []
    add_student(students, "Ali", 12)
    assert find_student(students, 12) is not None
    assert find_student(students, 99) is None


def test_duplicate_roll_number_is_refused() -> None:
    students: list[Student] = []
    add_student(students, "Ali", 12)
    with pytest.raises(ValueError):
        add_student(students, "Sara", 12)


def test_add_marks_to_student() -> None:
    students: list[Student] = []
    add_student(students, "Ali", 12)
    add_marks(students, 12, [80, 72])
    assert students[0].marks == [80, 72]


def test_invalid_mark_adds_nothing() -> None:
    students: list[Student] = []
    add_student(students, "Ali", 12)
    with pytest.raises(ValueError):
        add_marks(students, 12, [80, 150])
    assert students[0].marks == []   # the valid 80 was NOT added either


def test_add_marks_to_missing_student_raises() -> None:
    with pytest.raises(ValueError):
        add_marks([], 5, [70])


def test_class_ranking_highest_average_first() -> None:
    students = [
        Student("Ali", 1, [60, 60]),
        Student("Sara", 2, [95, 90]),
        Student("Ahmed", 3, [75, 70]),
        Student("NoMarks", 4),
    ]
    ranked = class_ranking(students)
    assert [student.name for student in ranked] == ["Sara", "Ahmed", "Ali"]


@pytest.mark.parametrize("name, roll", [("", 1), ("   ", 1), ("Ali", 0), ("Ali", -3)])
def test_student_rejects_bad_data(name: str, roll: int) -> None:
    with pytest.raises(ValueError):
        Student(name, roll)
