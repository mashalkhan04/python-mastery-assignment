# Part 12 - Debugging and testing
# NAME: MASHAL KHAN
# Roll number: TRN-2026-000349
# Date: 08/11/2026
#
# Warm-up    -> this file (fix 3 bugs)
# Build      -> test_grades.py   (run: pytest test_grades.py -v)
# Challenge  -> test_bank.py     (run: pytest test_bank.py -v)
# Run both:     pytest -v

# =====================================================
# WARM-UP: Fix 3 bugs
# =====================================================
# The code should print the average of the PASSING marks (90 and 70) = 80.0.
#
# ORIGINAL (buggy) code:
#
#   marks = [90, 25, 70]
#   passing = []
#   for m in range(len(marks) - 1):
#       if marks[m] > 33:
#           passing = [marks[m]]
#   print(sum(passing) / len(marks))
#
# How I found the bugs (print debugging): I added lines like
#   print("m =", m, "mark =", marks[m], "passing =", passing)
# inside the loop. The output showed that the loop never visited the last
# mark (70), and that `passing` was replaced each time instead of growing.
#
# BUG 1 - Off-by-one error (a LOGIC error)
#   range(len(marks) - 1) stops one item too early, so the last mark (70)
#   is never checked.            Fix: range(len(marks))
#
# BUG 2 - Overwriting instead of adding (a LOGIC error)
#   passing = [marks[m]] throws away the old list every time.
#   Fix: passing.append(marks[m])
#
# BUG 3 - Wrong divisor (a LOGIC error)
#   The average of the PASSING marks must be divided by len(passing),
#   not by len(marks).           Fix: sum(passing) / len(passing)
#
# None of them crashed the program (no error message), which is why they are
# logic errors: the program ran fine but gave a wrong answer (30.0 instead of 80.0).
#
# Extra note: the pass mark in our grade table is 33, so `>= 33` is more
# correct than `> 33`. It does not change this example's answer.


def buggy_version() -> None:
    marks = [90, 25, 70]
    passing = []
    for m in range(len(marks) - 1):
        if marks[m] > 33:
            passing = [marks[m]]
    print(sum(passing) / len(marks))


def fixed_version() -> None:
    marks = [90, 25, 70]
    passing = []
    for m in range(len(marks)):          # Fix 1
        if marks[m] >= 33:
            passing.append(marks[m])     # Fix 2
    print(sum(passing) / len(passing))   # Fix 3


if __name__ == "__main__":
    print("===== WARM-UP: Fix 3 bugs =====")
    print("Buggy version prints:")
    buggy_version()
    print("Fixed version prints:")
    fixed_version()
    print()
    print("Now run the tests with:  pytest -v")
