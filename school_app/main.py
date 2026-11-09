"""School Manager - a menu-driven program for a school office."""

import logging

from school.comments import ask_model, stream_words
from school.grades import average, grade, report_card
from school.manager import add_marks, add_student, class_ranking, find_student
from school.models import MAX_MARK, MIN_MARK, Student
from school.storage import load_students, save_students

DATA_FILE = "school.json"
LOG_FILE = "school.log"
LOGGER = logging.getLogger(__name__)

MENU = """
===== SCHOOL MANAGER =====
1. Add student
2. Add marks
3. Show report card
4. Class ranking
5. Save and exit
6. Write teacher comment (bonus)
"""


# ---------- small input helpers (they keep asking until the input is valid) ----------
def ask_text(prompt: str) -> str:
    """Ask until the user types something that is not empty."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("This cannot be empty. Please try again.")


def ask_int(prompt: str, minimum: int = 1) -> int:
    """Ask until the user types a whole number that is at least `minimum`."""
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            print("Please type a whole number.")
            continue
        if value < minimum:
            print(f"The number must be at least {minimum}.")
            continue
        return value


def ask_marks(prompt: str) -> list[float]:
    """Ask until the user types one or more marks between 0 and 100."""
    while True:
        parts = input(prompt).replace(",", " ").split()
        if not parts:
            print("Please type at least one mark.")
            continue
        try:
            marks = [float(part) for part in parts]
        except ValueError:
            print("Marks must be numbers, for example: 80 72 91")
            continue
        if all(MIN_MARK <= mark <= MAX_MARK for mark in marks):
            return marks
        print(f"Each mark must be between {MIN_MARK} and {MAX_MARK}.")


def ask_for_student(students: list[Student]) -> Student | None:
    """Ask for a roll number and return that student (or None with a message)."""
    if not students:
        print("There are no students yet. Add a student first.")
        return None
    student = find_student(students, ask_int("Roll number: "))
    if student is None:
        print("No student with that roll number.")
    return student


# ---------- one handler per menu option ----------
def handle_add_student(students: list[Student]) -> None:
    name = ask_text("Student name: ").title()
    roll_number = ask_int("Roll number: ")
    try:
        add_student(students, name, roll_number)
    except ValueError as error:
        print(f"Could not add the student: {error}")
    else:
        print(f"Added {name} (Roll {roll_number}).")


def handle_add_marks(students: list[Student]) -> None:
    student = ask_for_student(students)
    if student is None:
        return
    marks = ask_marks("Enter marks separated by spaces (e.g. 80 72 91): ")
    try:
        add_marks(students, student.roll_number, marks)
    except ValueError as error:
        print(f"Could not add the marks: {error}")
    else:
        print(f"Saved. {student.name} now has {len(student.marks)} mark(s).")


def handle_report_card(students: list[Student]) -> None:
    student = ask_for_student(students)
    if student is not None:
        print(report_card(student))


def handle_ranking(students: list[Student]) -> None:
    ranked = class_ranking(students)
    if not ranked:
        print("No marks have been recorded yet, so there is no ranking.")
        return
    print()
    print("========= CLASS RANKING =========")
    print(f"{'Rank':<6}{'Name':<14}{'Roll':<6}{'Average':>8}  Grade")
    for position, student in enumerate(ranked, start=1):
        avg = average(student.marks)
        print(f"{position:<6}{student.name:<14}{student.roll_number:<6}{avg:>8.2f}  {grade(avg)}")


def handle_comment(students: list[Student]) -> None:
    student = ask_for_student(students)
    if student is None:
        return
    try:
        comment = ask_model(student)
    except RuntimeError as error:
        LOGGER.error("Comment failed: %s", error)
        print("Sorry, a comment could not be created.")
        return
    print(f"Comment for {student.name}: ", end="")
    for chunk in stream_words(comment, delay=0.05):   # word-by-word output
        print(chunk, end="", flush=True)
    print()


# ---------- the menu loop ----------
def run_menu(students: list[Student]) -> None:
    """Show the menu again and again until the user chooses 5."""
    while True:
        print(MENU)
        choice = input("Choose: ").strip()
        if choice == "1":
            handle_add_student(students)
        elif choice == "2":
            handle_add_marks(students)
        elif choice == "3":
            handle_report_card(students)
        elif choice == "4":
            handle_ranking(students)
        elif choice == "5":
            return
        elif choice == "6":
            handle_comment(students)
        else:
            print("Invalid choice. Please type a number from 1 to 6.")


def main() -> None:
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    students = load_students(DATA_FILE)
    print(f"Loaded {len(students)} student(s) from {DATA_FILE}.")

    try:
        run_menu(students)
    except (KeyboardInterrupt, EOFError):
        print("\nInput closed. Saving your data before exit.")

    try:
        save_students(students, DATA_FILE)
    except OSError as error:
        LOGGER.error("Could not save: %s", error)
        print(f"Could not save the data: {error}")
    else:
        print(f"Data saved to {DATA_FILE}. Goodbye!")


if __name__ == "__main__":
    main()
