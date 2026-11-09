# Part 3 - Loops (for / while)
# NAME: MASHAL KHAN
# Roll number: TRN-2026-000349
# Date: 08/11/2026

import random


# =====================================================
# WARM-UP: Times table
# =====================================================
print("===== WARM-UP: Times table =====")

try:
    number = int(input("Enter a number: "))

    # range(1, 11) gives 1, 2, ... 10 (the last number is not included)
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

except ValueError:
    print("Invalid input: please type a whole number, for example 7.")


# =====================================================
# BUILD: ATM PIN check
# =====================================================
print()
print("===== BUILD: ATM PIN check =====")

CORRECT_PIN = "4321"   # kept as text so letters never crash the program
MAX_TRIES = 3

tries_left = MAX_TRIES

while tries_left > 0:
    entered_pin = input("Enter your PIN: ").strip()

    if entered_pin == CORRECT_PIN:
        print("Welcome")
        break  # stop the loop: the PIN was correct

    # Wrong PIN: use up one try
    tries_left -= 1
    print(f"Wrong PIN. Tries left: {tries_left}")

    if tries_left == 0:
        print("Card blocked")


# =====================================================
# CHALLENGE: Number guessing game
# =====================================================
print()
print("===== CHALLENGE: Number guessing game =====")

LOWEST = 1
HIGHEST = 50

play_again = "y"

while play_again == "y":
    secret_number = random.randint(LOWEST, HIGHEST)
    guesses = 0
    print(f"I am thinking of a number between {LOWEST} and {HIGHEST}.")

    while True:
        text = input("Your guess: ").strip()

        # Make sure the guess is a whole number
        try:
            guess = int(text)
        except ValueError:
            print("Please type a whole number.")
            continue  # ask again (this does not count as a guess)

        # Make sure the guess is inside the allowed range
        if guess < LOWEST or guess > HIGHEST:
            print(f"Please guess between {LOWEST} and {HIGHEST}.")
            continue

        guesses += 1  # count only valid guesses

        if guess > secret_number:
            print("Too high")
        elif guess < secret_number:
            print("Too low")
        else:
            word = "guess" if guesses == 1 else "guesses"
            print(f"Got it in {guesses} {word}!")
            break

    # Ask until the user types y or n
    while True:
        answer = input("Play again? (y/n): ").strip().lower()
        if answer in ("y", "n"):
            break
        print("Please type y or n.")
    play_again = answer

print("Thanks for playing!")


# =====================================================
# EXTRA PRACTICE: star triangle and sum of even numbers
# =====================================================
print()
print("===== EXTRA PRACTICE =====")

# Triangle of stars using nested loops
rows = 5
for row in range(1, rows + 1):
    for star in range(row):
        print("*", end="")  # end="" keeps the stars on the same line
    print()                 # move to the next line

# Sum of all even numbers from 1 to 100
even_sum = 0
for n in range(1, 101):
    if n % 2 == 0:
        even_sum += n
print(f"Sum of even numbers from 1 to 100 = {even_sum}")
