# Part 10 - Iterators, generators and decorators
# NAME: MASHAL KHAN
# Roll number: TRN-2026-000349
# Date: 08/11/2026

import time
from collections.abc import Callable, Iterator
from functools import wraps
from typing import Any


# =====================================================
# WARM-UP: Countdown generator
# =====================================================
def countdown(n: int) -> Iterator[int]:
    """Yield n, n-1, ... 1, one value at a time."""
    while n > 0:
        yield n   # 'yield' pauses here and hands out one value
        n -= 1


def evens(limit: int) -> Iterator[int]:
    """Yield the even numbers from 0 up to and including limit."""
    for number in range(0, limit + 1, 2):
        yield number


print("===== WARM-UP: Countdown generator =====")
for number in countdown(5):
    print(number)
print("Liftoff!")
print(list(evens(10)))   # [0, 2, 4, 6, 8, 10]


# =====================================================
# BUILD: Big file reader
# =====================================================
LOG_FILE = "app.log"


def create_log_file(path: str, total_lines: int = 60) -> None:
    """Create a text file with many lines; every 7th line contains ERROR."""
    with open(path, "w", encoding="utf-8") as file:
        for line_number in range(1, total_lines + 1):
            if line_number % 7 == 0:
                file.write(f"Line {line_number}: ERROR something went wrong\n")
            else:
                file.write(f"Line {line_number}: INFO everything is fine\n")


def read_lines(path: str) -> Iterator[str]:
    """Generator 1: yield the file one line at a time (never loads it all)."""
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.rstrip("\n")


def only_errors(lines: Iterator[str]) -> Iterator[str]:
    """Generator 2: pass along only the lines that contain ERROR."""
    for line in lines:
        if "ERROR" in line:
            yield line


print()
print("===== BUILD: Big file reader =====")
create_log_file(LOG_FILE)

# Count the error lines WITHOUT building a list:
# the generator expression hands 1 to sum() for every error line.
error_count = sum(1 for _ in only_errors(read_lines(LOG_FILE)))
print(f"Number of ERROR lines in {LOG_FILE}: {error_count}")

print("First 3 error lines:")
shown = 0
for error_line in only_errors(read_lines(LOG_FILE)):
    print(f"  {error_line}")
    shown += 1
    if shown == 3:
        break


# =====================================================
# CHALLENGE: Your own decorators
# =====================================================
def timer(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator: print how long the function took."""
    @wraps(func)  # keeps the original name and docstring
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[timer] {func.__name__} took {elapsed:.4f} seconds")
        return result  # do not forget to return the result!
    return wrapper


def log_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator: print the function name and its arguments."""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"[log] Calling {func.__name__} with args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper


@log_calls
@timer
def sum_numbers(limit: int) -> int:
    """Return the sum of 1 to limit."""
    total = 0
    for number in range(1, limit + 1):
        total += number
    return total


print()
print("===== CHALLENGE: Your own decorators =====")
answer = sum_numbers(1_000_000)
print(f"Sum of 1 to 1,000,000 = {answer}")
print(f"Function name is still: {sum_numbers.__name__}")   # thanks to @wraps
