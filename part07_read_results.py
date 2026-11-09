# Part 7 (Challenge) - Second program: read results.csv and print the topper
# NAME: MASHAL KHAN
# Roll number: TRN-2026-000349
# Date: 08/11/2026
#
# Run part07_exceptions_files.py first so that results.csv exists.

import csv

try:
    with open("results.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)  # each row becomes a dictionary
        rows = list(reader)
except FileNotFoundError:
    print("results.csv not found. Run part07_exceptions_files.py first.")
else:
    topper_row = None
    for row in rows:
        print(f"{row['Name']:<10} average = {row['Average']}")
        # CSV gives text, so convert the average to float before comparing
        if topper_row is None or float(row["Average"]) > float(topper_row["Average"]):
            topper_row = row

    if topper_row is None:
        print("The file has no students.")
    else:
        print()
        print(f"Topper: {topper_row['Name']} with an average of {topper_row['Average']}")
