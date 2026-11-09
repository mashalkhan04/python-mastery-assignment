"""Tests for school/attendance.py."""

import pytest

from school.attendance import attendance_percentage, attendance_status


def test_attendance_percentage() -> None:
    assert attendance_percentage(18, 20) == pytest.approx(90.0)


def test_attendance_status() -> None:
    assert attendance_status(75) == "Good"
    assert attendance_status(74.9) == "Low attendance"


def test_attendance_rejects_wrong_numbers() -> None:
    with pytest.raises(ValueError):
        attendance_percentage(25, 20)
    with pytest.raises(ValueError):
        attendance_percentage(5, 0)
