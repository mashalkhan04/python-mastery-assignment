"""Bonus: teacher comments (rule-based), streaming, and a retry decorator."""

import logging
import time
from collections.abc import Callable, Iterator
from functools import wraps
from typing import Any

from school.grades import average
from school.models import Student

LOGGER = logging.getLogger(__name__)


def make_comment(student: Student) -> str:
    """Create a short teacher comment from the marks using simple rules."""
    if not student.marks:
        return f"No marks have been recorded for {student.name} yet."

    avg = average(student.marks)
    lowest = min(student.marks)

    if avg >= 80 and lowest >= 80:
        return "Excellent in all subjects, keep it up."
    if avg >= 80:
        return "Excellent overall, but give extra attention to your weakest subject."
    if avg >= 60:
        comment = "Good work, a little more practice can take you higher."
    elif avg >= 33:
        comment = "Satisfactory, but more regular study is needed."
    else:
        return "Needs serious improvement. Please meet the teacher for extra support."

    if lowest < 33:
        comment += " One subject is below the passing mark, so please focus on it."
    return comment


def retry(times: int = 3, delay: float = 0.0) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Decorator factory: run the function again if it raises an error."""

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_error: Exception | None = None
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as error:   # a retry must catch any error
                    last_error = error
                    LOGGER.warning("Attempt %d of %d for %s failed: %s", attempt, times, func.__name__, error)
                    if attempt < times and delay > 0:
                        time.sleep(delay)
            raise RuntimeError(f"{func.__name__} failed after {times} attempts") from last_error

        return wrapper

    return decorator


@retry(times=3)
def ask_model(student: Student, model: Callable[[Student], str] = make_comment) -> str:
    """Get a comment from a 'model'. The model can be swapped (or mocked in tests).

    The default model is the rule-based make_comment(). A real AI model would be
    another function with the same shape: it takes a Student and returns text.
    """
    return model(student)


def stream_words(text: str, delay: float = 0.0) -> Iterator[str]:
    """Generator: hand out the text one word at a time, like a chat app."""
    for word in text.split():
        yield word + " "
        if delay > 0:
            time.sleep(delay)
