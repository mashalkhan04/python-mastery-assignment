"""Tests for school/grades.py."""

import pytest

from school.grades import average, grade, report_card
from school.models import Student


@pytest.mark.parametrize(
    "avg, expected",
    [(0, "Fail"), (32, "Fail"), (33, "D"), (59, "D"), (60, "C"), (70, "B"), (80, "A"), (100, "A")],
)
def test_grade_boundaries(avg: float, expected: str) -> None:
    assert grade(avg) == expected


@pytest.mark.parametrize("bad", [-1, 101])
def test_grade_rejects_values_outside_0_to_100(bad: float) -> None:
    with pytest.raises(ValueError):
        grade(bad)


def test_average() -> None:
    assert average([80, 72, 91]) == pytest.approx(81.0)
    assert average([]) == 0.0


def test_report_card_shows_average_and_grade() -> None:
    card = report_card(Student("Ali", 12, [80, 72, 91]))
    assert "Ali" in card
    assert "81.00" in card
    assert "Grade   : A" in card


def test_report_card_without_marks() -> None:
    card = report_card(Student("Sara", 7))
    assert "no marks yet" in card
