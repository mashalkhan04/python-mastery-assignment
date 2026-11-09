"""Tests for school/storage.py (tmp_path is a temporary folder made by pytest)."""

from pathlib import Path

from school.models import Student
from school.storage import load_students, save_students


def test_save_then_load_gives_the_same_students(tmp_path: Path) -> None:
    file_path = tmp_path / "school.json"
    students = [Student("Ali", 12, [80, 72, 91]), Student("Sara", 7)]
    save_students(students, file_path)
    assert load_students(file_path) == students


def test_missing_file_gives_empty_list(tmp_path: Path) -> None:
    assert load_students(tmp_path / "does_not_exist.json") == []


def test_broken_file_gives_empty_list_and_keeps_a_backup(tmp_path: Path) -> None:
    file_path = tmp_path / "school.json"
    file_path.write_text("this is not json", encoding="utf-8")
    assert load_students(file_path) == []
    assert (tmp_path / "school.json.bak").exists()


def test_file_with_invalid_marks_is_not_loaded(tmp_path: Path) -> None:
    file_path = tmp_path / "school.json"
    file_path.write_text('[{"name": "Ali", "roll_number": 1, "marks": [500]}]', encoding="utf-8")
    assert load_students(file_path) == []
