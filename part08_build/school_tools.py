# Part 8 (Build) - Your own module: school_tools.py
# NAME: MASHAL KHAN
# Roll number: TRN-2026-000349
# Date: 08/11/2026
#
# These are the Part 5 functions, moved into their own module.

from collections.abc import Sequence


def average(marks: Sequence[float]) -> float:
    """Return the average of the marks (0.0 if there are no marks)."""
    if not marks:
        return 0.0
    return sum(marks) / len(marks)


def grade(avg: float) -> str:
    """Return the grade for an average, using the table from Part 2."""
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


def report(name: str, marks: Sequence[float]) -> str:
    """Return a one-line result string using average() and grade()."""
    avg = average(marks)
    return f"{name}: average {avg:.2f}, grade {grade(avg)}"


# This block runs ONLY when you run this file directly:
#     python school_tools.py
# It does NOT run when another file does "import school_tools".
if __name__ == "__main__":
    print("school_tools.py is running directly - self-test:")
    print(report("Test Student", [80, 90, 100]))
    assert average([80, 90, 100]) == 90
    assert grade(90) == "A"
    print("All self-tests passed.")
