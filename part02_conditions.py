# Part 2 - Conditions (if / elif / else)
# NAME: MASHAL KHAN
# Roll number: TRN-2026-000349
# Date: 08/11/2026


# =====================================================
# WARM-UP: Even, odd and sign
# =====================================================
print("===== WARM-UP: Even, odd and sign =====")

try:
    number = int(input("Enter a whole number: "))

    # Check the sign of the number
    if number > 0:
        print(f"{number} is positive.")
    elif number < 0:
        print(f"{number} is negative.")
    else:
        print("The number is zero.")

    # Check even or odd: % gives the remainder after dividing by 2
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

except ValueError:
    print("Invalid input: please type a whole number, for example 7.")


# =====================================================
# BUILD: Grade calculator
# =====================================================
print()
print("===== BUILD: Grade calculator =====")

try:
    marks = float(input("Enter marks out of 100: "))

    # 'not 0 <= marks <= 100' catches anything below 0 or above 100
    if not 0 <= marks <= 100:
        print("Invalid marks")
    else:
        if marks >= 80:
            grade = "A"
        elif marks >= 70:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 33:
            grade = "D"
        else:
            grade = "Fail"
        print(f"Marks: {marks:.1f}  ->  Grade: {grade}")

except ValueError:
    print("Invalid input: please type marks as a number, for example 85.")


# =====================================================
# CHALLENGE: Electricity bill
# =====================================================
print()
print("===== CHALLENGE: Electricity bill =====")

# Constants (rates in Rs per unit)
RATE_FIRST_100 = 10    # units 1 to 100
RATE_NEXT_100 = 15     # units 101 to 200
RATE_ABOVE_200 = 20    # units above 200
FIXED_CHARGES = 50

# Edge cases to test (expected totals):
#   0 units -> Rs 50     100 units -> Rs 1050    101 units -> Rs 1065
#   200 units -> Rs 2550   201 units -> Rs 2570   250 units -> Rs 3550

try:
    units = int(input("Enter units used: "))

    if units < 0:
        print("Invalid input: units cannot be negative.")
    else:
        if units <= 100:
            energy_charges = units * RATE_FIRST_100
        elif units <= 200:
            energy_charges = 100 * RATE_FIRST_100 + (units - 100) * RATE_NEXT_100
        else:
            energy_charges = (
                100 * RATE_FIRST_100
                + 100 * RATE_NEXT_100
                + (units - 200) * RATE_ABOVE_200
            )

        total = energy_charges + FIXED_CHARGES

        print()
        print("======= ELECTRICITY BILL =======")
        print(f"Units used     : {units}")
        print(f"Energy charges : Rs {energy_charges}")
        print(f"Fixed charges  : Rs {FIXED_CHARGES}")
        print("--------------------------------")
        print(f"TOTAL          : Rs {total}")
        print("================================")

except ValueError:
    print("Invalid input: please type units as a whole number, for example 250.")
