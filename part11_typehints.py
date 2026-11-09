# Part 11 - Type hints and dataclasses
# NAME: MASHAL KHAN
# Roll number: TRN-2026-000349
# Date: 08/11/2026

import json
from dataclasses import asdict, dataclass, field

from part05_functions import area_of_circle, average, greet, grade, is_even, report


# =====================================================
# WARM-UP: Add hints
# =====================================================
# I added type hints (including return types) to ALL functions in
# part05_functions.py, for example:
#     def average(marks: Sequence[float]) -> float:
# Then I ran:   mypy part05_functions.py
# Result:       Success: no issues found in 1 source file
print("===== WARM-UP: Add hints =====")
print(f"area_of_circle(3) = {area_of_circle(3):.2f}")
print(f"is_even(10)       = {is_even(10)}")
print(greet("Ali", "ur"))
print(f"average([80, 90]) = {average([80, 90])}")
print(f"grade(85)         = {grade(85)}")
print(report("Sara", [95, 88, 90]))


# =====================================================
# BUILD: Product dataclass
# =====================================================
@dataclass(order=True)
class Product:
    """A shop product. @dataclass writes __init__, __repr__ and __eq__ for us."""

    name: str
    price: float
    stock: int
    tags: list[str] = field(default_factory=list)   # each product gets its own list

    def __post_init__(self) -> None:
        """Runs right after __init__: check the values."""
        if self.price < 0:
            raise ValueError("Price cannot be negative.")
        if self.stock < 0:
            raise ValueError("Stock cannot be negative.")


print()
print("===== BUILD: Product dataclass =====")

products = [
    Product("Pen", 30.0, 100, ["stationery"]),
    Product("Notebook", 120.0, 0, ["stationery", "school"]),
    Product("Backpack", 2500.0, 15, ["bags", "school"]),
    Product("Water Bottle", 450.0, 0),
    Product("Calculator", 900.0, 8, ["electronics", "school"]),
]

out_of_stock = [product for product in products if product.stock == 0]
print("Out of stock:")
for product in out_of_stock:
    print(f"  {product.name}")

# The validation in __post_init__ refuses bad data
try:
    Product("Broken item", -5.0, 3)
except ValueError as error:
    print(f"Refused: {error}")


# =====================================================
# CHALLENGE: Save and load
# =====================================================
def save_products(items: list[Product], path: str) -> None:
    """Save the products to a JSON file using asdict."""
    data = [asdict(item) for item in items]   # each Product becomes a dictionary
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_products(path: str) -> list[Product]:
    """Load products from a JSON file back into Product objects."""
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return [Product(**item) for item in data]   # ** turns a dict into keyword arguments


print()
print("===== CHALLENGE: Save and load =====")
save_products(products, "products.json")
loaded = load_products("products.json")
print(f"Saved and loaded {len(loaded)} products. Same as before? {loaded == products}")

# order=True lets us compare products with < and >.
# It compares the fields from left to right, so the FIRST field (name) decides:
print("sorted(products) -> sorted by NAME (first field):")
print("  ", [product.name for product in sorted(loaded)])

# To sort by price we tell sorted() which field to use:
by_price = sorted(loaded, key=lambda product: product.price)
print("Sorted by PRICE (cheapest first):")
for product in by_price:
    print(f"  Rs {product.price:>7.2f}  {product.name}")
