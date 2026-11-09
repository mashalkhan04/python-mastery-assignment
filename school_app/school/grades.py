"""Average, grade and report card."""

from collections.abc import Sequence

from school.models import Student


def average(marks: Sequence[float]) -> float:
    """Return the average of the marks (0.0 if there are none)."""
    if not marks:
        return 0.0
    return sum(marks) / len(marks)


def grade(avg: float) -> str:
    """Return the letter grade for an average between 0 and 100."""
    if not 0 <= avg <= 100:
        raise ValueError(f"Marks must be between 0 and 100, got {avg}")
    if avg >= 80:
        return "A"
    if avg >= 70:
        return "B"
    if avg >= 60:
        return "C"
    if avg >= 33:
        return "D"
    return "Fail"


def report_card(student: Student) -> str:
    """Return a printable report card for one student."""
    line = "=" * 33
    if student.marks:
        marks_text = ", ".join(f"{mark:g}" for mark in student.marks)
        avg = average(student.marks)
        average_text = f"{avg:.2f}"
        grade_text = grade(avg)
    else:
        marks_text = "no marks yet"
        average_text = "-"
        grade_text = "-"

    return "\n".join(
        [
            line,
            "         REPORT CARD",
            line,
            f"Name    : {student.name}",
            f"Roll no : {student.roll_number}",
            f"Marks   : {marks_text}",
            f"Average : {average_text}",
            f"Grade   : {grade_text}",
            line,
        ]
    )
