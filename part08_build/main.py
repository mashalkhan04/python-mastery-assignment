# Part 8 (Build) - main.py uses the school_tools module
# NAME: MASHAL KHAN
# Roll number: TRN-2026-000349
# Date: 08/11/2026
#
# Try both:
#   python school_tools.py   -> prints the self-test lines
#   python main.py           -> does NOT print the self-test lines,
#                               because the "if __name__ == '__main__'" block
#                               in school_tools.py does not run on import.

from school_tools import average, grade, report

students = {
    "Ali": [80, 72, 91],
    "Sara": [95, 88, 90],
    "Ahmed": [60, 45, 70],
}

print("===== BUILD: main.py using school_tools =====")
for student_name, student_marks in students.items():
    print(report(student_name, student_marks))

print()
print(f"Average of Ali: {average(students['Ali']):.2f}")
print(f"Grade for 75: {grade(75)}")
print("main.py finished (no self-test lines were printed above).")
