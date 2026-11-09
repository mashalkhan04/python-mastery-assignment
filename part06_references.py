# Part 6 - References and mutability
# NAME: MASHAL KHAN
# Roll number: TRN-2026-000349
# Date: 08/11/2026

import copy


# =====================================================
# WARM-UP: Predict, then run
# =====================================================
print("===== WARM-UP: Predict, then run =====")

a = [1, 2, 3]
b = a            # b is NOT a copy: it is a second name for the same list
b.append(4)
print(a)         # Prediction: [1, 2, 3, 4]   (a and b are the same list)

c = a.copy()     # c is a real copy: a new list with the same items
c.append(5)
print(a, c)      # Prediction: [1, 2, 3, 4] [1, 2, 3, 4, 5]   (a is not changed)

print(a is b, a is c, a == a[:])
# Prediction: True False True
# - a is b   -> True : same object in memory
# - a is c   -> False: c is a different object
# - a == a[:] -> True: a[:] is a copy, and a copy has equal VALUES
#
# Explanation of the surprise: "is" asks "same object?", while "==" asks
# "same values?". A copy is equal (==) but not identical (is).


# =====================================================
# BUILD: Fix the cart bug
# =====================================================
print()
print("===== BUILD: Fix the cart bug =====")


def add_item_buggy(item, cart=[]):
    """BUGGY: the default list [] is created ONCE and shared by every call."""
    cart.append(item)
    return cart


print("Buggy version:")
print("Customer 1:", add_item_buggy("apple"))   # ['apple']
print("Customer 2:", add_item_buggy("bread"))   # ['apple', 'bread']  <- BUG!
# Customer 2 sees Customer 1's apple because both used the same default list.


def add_item(item, cart=None):
    """FIXED: use None as the default and make a NEW list inside the function."""
    if cart is None:
        cart = []
    cart.append(item)
    return cart


print("Fixed version:")
print("Customer 1:", add_item("apple"))   # ['apple']
print("Customer 2:", add_item("bread"))   # ['bread']  <- correct


# =====================================================
# CHALLENGE: Safe class copy
# =====================================================
print()
print("===== CHALLENGE: Safe class copy =====")

classes = {"A": ["Ali", "Sara"]}

shallow = copy.copy(classes)       # copies the dictionary, but NOT the lists inside
deep = copy.deepcopy(classes)      # copies everything, including the lists inside

shallow["A"].append("Ahmed")       # this changes the ORIGINAL list too
deep["A"].append("Bilal")          # this changes only the deep copy

print("Original:", classes)        # {'A': ['Ali', 'Sara', 'Ahmed']}
print("Shallow :", shallow)        # {'A': ['Ali', 'Sara', 'Ahmed']}
print("Deep    :", deep)           # {'A': ['Ali', 'Sara', 'Bilal']}
# The shallow copy shares the inner list with the original (so Ahmed appears
# in both). The deep copy has its own inner list (so Bilal appears only there).
