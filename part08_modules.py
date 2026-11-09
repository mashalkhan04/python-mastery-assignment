# Part 8 (Warm-up) - Standard library tour
# NAME: MASHAL KHAN
# Roll number: TRN-2026-000349
# Date: 08/11/2026
#
# Part 8 Build  -> folder part08_build/ (school_tools.py + main.py)
# Part 8 Challenge -> folder school_app/ (package layout, also the final project)

import datetime
import math
import random
import statistics

print("===== WARM-UP: Standard library tour =====")

# math: square root of 144
print(f"Square root of 144 = {math.sqrt(144)}")

# random: pick a random student from a list
students = ["Ali", "Sara", "Ahmed", "Fatima", "Bilal"]
print(f"Random student: {random.choice(students)}")

# datetime: days left until 31 December this year
today = datetime.date.today()
new_year_eve = datetime.date(today.year, 12, 31)
days_left = (new_year_eve - today).days   # subtracting two dates gives a timedelta
print(f"Days left until 31 December: {days_left}")

# statistics: mean and median of 5 marks
marks = [78, 85, 92, 66, 74]
print(f"Marks: {marks}")
print(f"Mean   = {statistics.mean(marks)}")
print(f"Median = {statistics.median(marks)}")
