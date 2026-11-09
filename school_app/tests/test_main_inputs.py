"""Tests that wrong input does not crash the menu helpers in main.py."""

import pytest

from main import ask_int, ask_marks, ask_text


def fake_input(monkeypatch: pytest.MonkeyPatch, answers: list[str]) -> None:
    """Make input() return the answers one by one."""
    iterator = iter(answers)
    monkeypatch.setattr("builtins.input", lambda prompt="": next(iterator))


def test_ask_int_keeps_asking_until_valid(monkeypatch: pytest.MonkeyPatch) -> None:
    fake_input(monkeypatch, ["abc", "-4", "0", "12"])
    assert ask_int("Roll: ") == 12


def test_ask_marks_rejects_letters_and_out_of_range(monkeypatch: pytest.MonkeyPatch) -> None:
    fake_input(monkeypatch, ["", "eighty", "80 150", "80, 72 91"])
    assert ask_marks("Marks: ") == [80.0, 72.0, 91.0]


def test_ask_text_rejects_empty(monkeypatch: pytest.MonkeyPatch) -> None:
    fake_input(monkeypatch, ["", "   ", "Ali"])
    assert ask_text("Name: ") == "Ali"
