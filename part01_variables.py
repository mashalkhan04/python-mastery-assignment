# Part 1 - Variables, data types, input and output
# NAME: MASHAL KHAN
# Roll number: TRN-2026-000349
# Date: 08/11/2026


# =====================================================
# WARM-UP: Student ID card
# =====================================================
print("===== WARM-UP: Student ID card =====")

try:
    # input() always gives text (str), so we convert age to int
    name = input("Enter your name: ").strip().title()
    age = int(input("Enter your age: "))
    # 'class' is a reserved word in Python, so we call the variable student_class
    student_class = input("Enter your class (e.g. 1st Year): ").strip()
    city = input("Enter your city: ").strip().title()

    # Print the card
    print()
    print("======== STUDENT CARD ========")
    print(f"Name : {name}")
    print(f"Age : {age}")
    print(f"Class: {student_class}")
    print(f"City : {city}")
    print("==============================")

    # Print the data type of each value using type()
    print()
    print("Data type of each value:")
    print(f"name          -> {type(name)}")
    print(f"age           -> {type(age)}")
    print(f"student_class -> {type(student_class)}")
    print(f"city          -> {type(city)}")

except ValueError:
    # Runs if the user types letters where a whole number is needed
    print("Invalid input: age must be a whole number, for example 17.")


# =====================================================
# BUILD: Shop bill
# =====================================================
print()
print("===== BUILD: Shop bill =====")

# Constants: values that never change while the program runs
DISCOUNT_RATE = 0.05  # 5% discount
TAX_RATE = 0.17       # 17% tax
LINE = "=" * 32

try:
    item_name = input("Item name: ").strip().title()
    price = float(input("Price of one item (Rs): "))
    quantity = int(input("Quantity: "))

    # The maths, step by step
    subtotal = price * quantity
    discount = subtotal * DISCOUNT_RATE
    discounted_amount = subtotal - discount
    tax = discounted_amount * TAX_RATE  # tax is on the DISCOUNTED amount
    final_total = discounted_amount + tax

    # Print the bill ( :10.2f means 2 decimals, 10 characters wide )
    print()
    print(LINE)
    print("           SHOP BILL")
    print(LINE)
    print(f"Item           : {item_name} x {quantity}")
    print(f"Subtotal       : Rs {subtotal:10.2f}")
    print(f"Discount (5%)  : Rs {discount:10.2f}")
    print(f"After discount : Rs {discounted_amount:10.2f}")
    print(f"Tax (17%)      : Rs {tax:10.2f}")
    print(LINE)
    print(f"FINAL TOTAL    : Rs {final_total:10.2f}")
    print(LINE)

except ValueError:
    print("Invalid input: price must be a number and quantity a whole number.")


# =====================================================
# CHALLENGE: Unit converter
# =====================================================
print()
print("===== CHALLENGE: Unit converter =====")

KM_TO_MILES = 0.621371
METRES_PER_KM = 1000

try:
    celsius = float(input("Temperature in Celsius: "))
    km = float(input("Distance in kilometres: "))

    fahrenheit = celsius * 9 / 5 + 32
    kelvin = celsius + 273.15
    miles = km * KM_TO_MILES
    metres = km * METRES_PER_KM

    # .1f means 1 decimal place
    print()
    print("======== UNIT CONVERTER ========")
    print(f"{celsius:.1f} C  = {fahrenheit:.1f} F")
    print(f"{celsius:.1f} C  = {kelvin:.1f} K")
    print(f"{km:.1f} km = {miles:.1f} miles")
    print(f"{km:.1f} km = {metres:.1f} metres")
    print("================================")

except ValueError:
    print("Invalid input: please type numbers only, for example 36.5")
