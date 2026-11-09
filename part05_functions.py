# Part 5 - Functions and comprehensions
# NAME: MASHAL KHAN
# Roll number: TRN-2026-000349
# Date: 08/11/2026
#
# NOTE: This file already has the type hints asked for in Part 11 (Warm-up)
# and the grade() check asked for in Part 12 (Build), so other files can
# import from it safely. Check the hints with:  mypy part05_functions.py

import math
from collections.abc import Sequence  # "any list or tuple of numbers"


# =====================================================
# WARM-UP: Small helpers
# =====================================================
def area_of_circle(r: float) -> float:
    """Return the area of a circle with radius r."""
    return math.pi * r ** 2


def is_even(n: int) -> bool:
    """Return True if n is even, otherwise False."""
    return n % 2 == 0


def greet(name: str, lang: str = "en") -> str:
    """Greet a person in English ("en") or Urdu ("ur")."""
    if lang == "en":
        return f"Hello, {name}!"
    if lang == "ur":
        return f"Salaam, {name}!"
    return f"Sorry, I do not know the language '{lang}'."


# =====================================================
# BUILD: Marks toolkit
# =====================================================
def average(marks: Sequence[float]) -> float:
    """Return the average of the marks (0.0 if there are no marks)."""
    if not marks:
        return 0.0
    return sum(marks) / len(marks)


def grade(avg: float) -> str:
    """Return the grade for an average, using the table from Part 2."""
    # Part 12 change: refuse marks outside 0-100 with a ValueError
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


# =====================================================
# CHALLENGE: Comprehensions
# =====================================================
def demo_helpers() -> None:
    print("===== WARM-UP: Small helpers =====")
    for radius in (1, 2.5, 10):
        print(f"Area of circle with r={radius}: {area_of_circle(radius):.2f}")
    for number in (4, 7, 0):
        print(f"is_even({number}) -> {is_even(number)}")
    print(greet("Ali"))
    print(greet("Sara", "ur"))
    print(greet("Ahmed", lang="fr"))


def demo_toolkit() -> None:
    print()
    print("===== BUILD: Marks toolkit =====")
    print(report("Ali", [80, 72, 91]))
    print(report("Ahmed", [60, 45, 70]))
    print(report("Zara", [20, 30, 32]))


def demo_comprehensions() -> None:
    print()
    print("===== CHALLENGE: Comprehensions =====")

    # 1) squares of 1 to 10
    squares = [n ** 2 for n in range(1, 11)]
    print("Squares:", squares)

    # 2) only names longer than 4 letters
    names = ["Ali", "Sara", "Ahmed", "Fatima", "Bilal", "Zoe"]
    long_names = [name for name in names if len(name) > 4]
    print("Names longer than 4 letters:", long_names)

    # 3) dict of {name: average} from the Part 4 result sheet
    results = {
        "Ali": [80, 72, 91],
        "Sara": [95, 88, 90],
        "Ahmed": [60, 45, 70],
        "Fatima": [78, 82, 69],
        "Bilal": [35, 60, 55],
        "Hina": [38, 52, 41],
        "Zara": [20, 30, 32],
    }
    averages = {name: round(average(marks), 2) for name, marks in results.items()}
    print("Averages:", averages)

    # 4) only the passing students (average >= 33)
    passing = {name: avg for name, avg in averages.items() if avg >= 33}
    print("Passing students:", passing)


if __name__ == "__main__":
    demo_helpers()
    demo_toolkit()
    demo_comprehensions()
