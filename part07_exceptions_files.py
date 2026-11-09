# Part 7 - Exceptions and files
# NAME: MASHAL KHAN
# Roll number: TRN-2026-000349
# Date: 08/11/2026
#
# The second program for the Challenge is in part07_read_results.py

import csv
import datetime
import json


# =====================================================
# WARM-UP: Safe division
# =====================================================
print("===== WARM-UP: Safe division =====")

while True:
    try:
        first = float(input("Enter the first number: "))
        second = float(input("Enter the second number: "))
        answer = first / second
    except ValueError:
        print("That is not a number. Please try again.")
    except ZeroDivisionError:
        print("You cannot divide by zero. Please try again.")
    else:
        # 'else' runs only when no error happened
        print(f"{first:g} / {second:g} = {answer:g}")
        break  # valid input, so stop asking


# =====================================================
# BUILD: Daily diary
# =====================================================
DIARY_FILE = "diary.txt"


def add_entry(note: str) -> None:
    """Append today's note to the diary file, with the date."""
    today = datetime.date.today()
    # "a" = append: adds to the end of the file (creates it if missing)
    with open(DIARY_FILE, "a", encoding="utf-8") as file:
        file.write(f"{today}: {note}\n")


def read_entries() -> None:
    """Print all past entries, or 'No entries yet'."""
    try:
        with open(DIARY_FILE, "r", encoding="utf-8") as file:
            text = file.read().strip()
    except FileNotFoundError:
        print("No entries yet")
        return
    if text == "":
        print("No entries yet")
    else:
        print(text)


def run_diary() -> None:
    """Show the diary menu until the user exits."""
    while True:
        print()
        print("1) Write today's note   2) Read all entries   3) Exit")
        choice = input("Choose (1-3): ").strip()
        if choice == "1":
            note = input("Today's note: ").strip()
            if note == "":
                print("The note cannot be empty.")
            else:
                add_entry(note)
                print("Saved.")
        elif choice == "2":
            read_entries()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please type 1, 2 or 3.")


print()
print("===== BUILD: Daily diary =====")
run_diary()


# =====================================================
# CHALLENGE: CSV result sheet (+ JSON)
# =====================================================
print()
print("===== CHALLENGE: CSV result sheet =====")

results = {
    "Ali": [80, 72, 91],
    "Sara": [95, 88, 90],
    "Ahmed": [60, 45, 70],
    "Fatima": [78, 82, 69],
    "Bilal": [35, 60, 55],
    "Hina": [38, 52, 41],
    "Zara": [20, 30, 32],
}

try:
    # newline="" stops blank lines appearing between rows on Windows
    with open("results.csv", "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Name", "Mark1", "Mark2", "Mark3", "Average"])
        for name, marks in results.items():
            average = round(sum(marks) / len(marks), 2)
            writer.writerow([name, *marks, average])
    print("Saved results.csv")

    with open("results.json", "w", encoding="utf-8") as json_file:
        json.dump(results, json_file, indent=4)
    print("Saved results.json")

except OSError as error:
    print(f"Could not save the files: {error}")

print("Now run part07_read_results.py to read the CSV back.")
