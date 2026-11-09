"""Attendance helpers (part of the Part 8 package layout)."""


def attendance_percentage(days_present: int, total_days: int) -> float:
    """Return attendance as a percentage (0 to 100)."""
    if total_days <= 0:
        raise ValueError("Total days must be more than zero.")
    if not 0 <= days_present <= total_days:
        raise ValueError("Days present must be between 0 and the total days.")
    return days_present / total_days * 100


def attendance_status(percentage: float) -> str:
    """Return 'Good' for 75% or more, otherwise 'Low attendance'."""
    return "Good" if percentage >= 75 else "Low attendance"
