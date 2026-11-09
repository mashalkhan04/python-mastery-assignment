"""The Student dataclass and mark validation."""

from dataclasses import dataclass, field

MIN_MARK = 0
MAX_MARK = 100


def validate_mark(mark: float) -> None:
    """Raise ValueError if a mark is not between 0 and 100."""
    if not MIN_MARK <= mark <= MAX_MARK:
        raise ValueError(f"A mark must be between {MIN_MARK} and {MAX_MARK}, got {mark}.")


@dataclass
class Student:
    """One student: name, roll number and a list of marks."""

    name: str
    roll_number: int
    marks: list[float] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Check the data as soon as a Student is created (also when loading)."""
        if not self.name.strip():
            raise ValueError("The name cannot be empty.")
        if self.roll_number <= 0:
            raise ValueError("The roll number must be a positive number.")
        for mark in self.marks:
            validate_mark(mark)
