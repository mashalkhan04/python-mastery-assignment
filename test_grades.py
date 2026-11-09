# Part 12 (Build) - Test the grade function with pytest
# NAME: MASHAL KHAN
# Roll number: TRN-2026-000349
# Date: 08/11/2026
#
# grade() in part05_functions.py was changed to raise ValueError for
# marks outside 0-100.   Run:  pytest test_grades.py -v

import pytest

from part05_functions import grade


# One test function runs once for EACH (marks, expected) pair below.
@pytest.mark.parametrize(
    "marks, expected",
    [
        (0, "Fail"),
        (32, "Fail"),   # boundary: highest Fail
        (33, "D"),      # boundary: lowest D
        (59, "D"),      # boundary: highest D
        (60, "C"),      # boundary: lowest C
        (69, "C"),      # boundary: highest C
        (70, "B"),      # boundary: lowest B
        (79, "B"),      # boundary: highest B
        (80, "A"),      # boundary: lowest A
        (100, "A"),
    ],
)
def test_grade_boundaries(marks: float, expected: str) -> None:
    assert grade(marks) == expected


@pytest.mark.parametrize("bad_marks", [101, 150, -1, -0.5])
def test_grade_rejects_marks_outside_0_to_100(bad_marks: float) -> None:
    # pytest.raises passes only if a ValueError really happens
    with pytest.raises(ValueError):
        grade(bad_marks)
