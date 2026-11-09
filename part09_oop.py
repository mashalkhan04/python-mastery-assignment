# Part 9 - OOP: classes and objects
# NAME: MASHAL KHAN
# Roll number: TRN-2026-000349
# Date: 08/11/2026
#
# BankAccount is also imported by test_bank.py (Part 12), so the demo code
# is inside "if __name__ == '__main__':" at the bottom.


# =====================================================
# WARM-UP: Student class
# =====================================================
class Student:
    """A student with a name, roll number and a list of marks."""

    def __init__(self, name: str, roll_number: int, marks: list[float] | None = None) -> None:
        self.name = name
        self.roll_number = roll_number
        # Every student gets their OWN list (see the Part 6 default-argument bug)
        self.marks: list[float] = marks if marks is not None else []

    def add_mark(self, mark: float) -> None:
        """Add one mark (must be between 0 and 100)."""
        if not 0 <= mark <= 100:
            raise ValueError("A mark must be between 0 and 100.")
        self.marks.append(mark)

    def average(self) -> float:
        """Return the average mark (0.0 if there are no marks)."""
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)

    def __str__(self) -> str:
        return f"{self.name} (Roll {self.roll_number}): avg {self.average():.1f}"


# =====================================================
# BUILD: Bank account
# =====================================================
class BankAccount:
    """A bank account with deposit, withdraw and a transaction history."""

    def __init__(self, owner: str, balance: float = 0) -> None:
        if balance < 0:
            raise ValueError("The opening balance cannot be negative.")
        self.owner = owner
        self.balance = balance
        self.history: list[str] = []

    def deposit(self, amount: float) -> None:
        """Add money. Refuses zero or negative amounts."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.history.append(f"Deposit   +Rs {amount:.2f} | Balance: Rs {self.balance:.2f}")

    def withdraw(self, amount: float) -> None:
        """Take money out. Refuses wrong amounts and amounts above the balance."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        self.history.append(f"Withdraw  -Rs {amount:.2f} | Balance: Rs {self.balance:.2f}")

    def print_history(self) -> None:
        """Print every transaction."""
        print(f"Transaction history for {self.owner}:")
        if not self.history:
            print("  (no transactions yet)")
        for line in self.history:
            print(f"  {line}")


# =====================================================
# CHALLENGE: Library system
# =====================================================
class Book:
    """A book with a title, an author and an availability flag."""

    def __init__(self, title: str, author: str, available: bool = True) -> None:
        self.title = title
        self.author = author
        self.available = available

    def __str__(self) -> str:
        status = "Available" if self.available else "Borrowed"
        return f"'{self.title}' by {self.author} [{status}]"


class EBook(Book):
    """Inheritance: an EBook IS a Book, plus a file size."""

    def __init__(self, title: str, author: str, file_size_mb: float, available: bool = True) -> None:
        super().__init__(title, author, available)  # reuse the Book setup
        self.file_size_mb = file_size_mb

    def __str__(self) -> str:
        # Override __str__ and reuse the parent's text
        return f"{super().__str__()} (E-book, {self.file_size_mb} MB)"


class Library:
    """Composition: a Library HAS many Book objects."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def _find(self, title: str) -> Book | None:
        """Find a book by title, ignoring capital letters (helper method)."""
        for book in self.books:
            if book.title.lower() == title.strip().lower():
                return book
        return None

    def borrow(self, title: str) -> Book:
        book = self._find(title)
        if book is None:
            raise ValueError(f"'{title}' is not in the library.")
        if not book.available:
            raise ValueError(f"'{title}' is already borrowed.")
        book.available = False
        return book

    def return_book(self, title: str) -> Book:
        book = self._find(title)
        if book is None:
            raise ValueError(f"'{title}' does not belong to this library.")
        if book.available:
            raise ValueError(f"'{title}' was not borrowed.")
        book.available = True
        return book

    def available_books(self) -> list[Book]:
        return [book for book in self.books if book.available]


def demo_student() -> None:
    print("===== WARM-UP: Student class =====")
    ali = Student("Ali", 12)
    for mark in (80, 72, 91, 81):
        ali.add_mark(mark)
    print(ali)
    sara = Student("Sara", 7, [95, 88, 90])
    print(sara)
    try:
        ali.add_mark(150)
    except ValueError as error:
        print(f"Error: {error}")


def demo_bank() -> None:
    print()
    print("===== BUILD: Bank account =====")
    account = BankAccount("Ali", 1000)
    account.deposit(500)
    account.withdraw(200)
    for action, amount in (("deposit", -50), ("withdraw", 5000)):
        try:
            getattr(account, action)(amount)
        except ValueError as error:
            print(f"Refused {action}({amount}): {error}")
    print(f"Final balance: Rs {account.balance:.2f}")
    account.print_history()


def demo_library() -> None:
    print()
    print("===== CHALLENGE: Library system =====")
    library = Library("City Library")
    library.add_book(Book("Python Basics", "A. Khan"))
    library.add_book(Book("Data Science 101", "S. Ahmed"))
    library.add_book(EBook("AI for Everyone", "M. Raza", 4.5))

    print("Available books:")
    for book in library.available_books():
        print(f"  {book}")

    print(f"Borrowed: {library.borrow('python basics')}")
    try:
        library.borrow("Python Basics")
    except ValueError as error:
        print(f"Error: {error}")

    print("Available now:")
    for book in library.available_books():
        print(f"  {book}")

    library.return_book("Python Basics")
    print(f"After returning, available books: {len(library.available_books())}")


if __name__ == "__main__":
    demo_student()
    demo_bank()
    demo_library()
