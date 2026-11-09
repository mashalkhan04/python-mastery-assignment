# Part 4 - Lists, dictionaries, tuples and sets
# NAME: MASHAL KHAN
# Roll number: TRN-2026-000349
# Date: 08/11/2026


# =====================================================
# WARM-UP: Shopping list
# =====================================================
print("===== WARM-UP: Shopping list =====")

items = ["milk", "bread", "eggs"]
items.append("tea")      # add "tea" at the end
items.remove("bread")    # remove "bread"
items.sort()             # sort A to Z

# enumerate gives a number with each item (start=1 so we count from 1)
for number, item in enumerate(items, start=1):
    print(f"{number}. {item}")


# =====================================================
# BUILD: Phone book
# =====================================================
print()
print("===== BUILD: Phone book =====")

# A dictionary: name -> phone number
contacts = {
    "Ali": "0300-1111111",
    "Sara": "0301-2222222",
    "Ahmed": "0302-3333333",
    "Fatima": "0303-4444444",
    "Bilal": "0304-5555555",
}

while True:
    print()
    print("1) Add   2) Search   3) Delete   4) Show all   5) Exit")
    choice = input("Choose (1-5): ").strip()

    if choice == "1":
        name = input("Name: ").strip().title()
        phone = input("Phone number: ").strip()
        # Allow digits, + and - only
        cleaned = phone.replace("-", "").replace("+", "").replace(" ", "")
        if name == "":
            print("Name cannot be empty.")
        elif not cleaned.isdigit():
            print("Invalid phone number: use digits only (- and + are allowed).")
        else:
            contacts[name] = phone
            print(f"Saved {name}: {phone}")

    elif choice == "2":
        name = input("Name to search: ").strip().title()
        phone = contacts.get(name)   # .get() gives None instead of crashing
        if phone is None:
            print("Not found")
        else:
            print(f"{name}: {phone}")

    elif choice == "3":
        name = input("Name to delete: ").strip().title()
        if name in contacts:
            del contacts[name]
            print(f"Deleted {name}.")
        else:
            print("Not found")

    elif choice == "4":
        if len(contacts) == 0:
            print("The phone book is empty.")
        else:
            for name, phone in contacts.items():
                print(f"{name:<10} {phone}")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please type a number from 1 to 5.")


# =====================================================
# CHALLENGE: Class result sheet
# =====================================================
print()
print("===== CHALLENGE: Class result sheet =====")

# name -> list of three marks
results = {
    "Ali": [80, 72, 91],
    "Sara": [95, 88, 90],
    "Ahmed": [60, 45, 70],
    "Fatima": [78, 82, 69],
    "Bilal": [35, 60, 55],
    "Hina": [38, 52, 41],
    "Zara": [20, 30, 32],
}

print(f"{'Name':<10}{'Total':>7}{'Average':>10}")
print("-" * 27)

topper = ""
highest_average = -1.0
below_40 = set()   # a set keeps each name only once

for name, marks in results.items():
    total = sum(marks)
    average = total / len(marks)
    print(f"{name:<10}{total:>7}{average:>10.2f}")

    # Track the student with the highest average
    if average > highest_average:
        highest_average = average
        topper = name

    # Add the student to the set if ANY mark is below 40
    for mark in marks:
        if mark < 40:
            below_40.add(name)

print()
print(f"Class topper: {topper} with an average of {highest_average:.2f}")
print(f"Students who scored below 40 in any subject: {below_40}")
