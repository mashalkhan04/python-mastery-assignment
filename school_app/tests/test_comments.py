"""Tests for the bonus: comments, retry decorator and streaming (all offline)."""

import pytest

from school.comments import ask_model, make_comment, retry, stream_words
from school.models import Student


def test_excellent_student_comment() -> None:
    student = Student("Sara", 2, [95, 88, 90])
    assert make_comment(student) == "Excellent in all subjects, keep it up."


def test_comment_for_student_without_marks() -> None:
    assert "No marks" in make_comment(Student("Ali", 1))


def test_comment_for_weak_student() -> None:
    assert "serious improvement" in make_comment(Student("Zara", 9, [20, 30, 32]))


def test_stream_words_gives_the_text_back_word_by_word() -> None:
    chunks = list(stream_words("Well done Ali"))
    assert chunks == ["Well ", "done ", "Ali "]
    assert "".join(chunks).strip() == "Well done Ali"


def test_retry_succeeds_after_two_failures() -> None:
    calls: list[int] = []

    def flaky_model(student: Student) -> str:
        calls.append(1)
        if len(calls) < 3:
            raise ConnectionError("model is busy")   # fails twice
        return "Great work!"

    # A mocked model: no internet and no API key needed
    assert ask_model(Student("Ali", 1, [90]), model=flaky_model) == "Great work!"
    assert len(calls) == 3


def test_retry_gives_up_after_all_attempts() -> None:
    @retry(times=2)
    def always_fails() -> str:
        raise ConnectionError("down")

    with pytest.raises(RuntimeError):
        always_fails()
