"""Save and load students to a JSON file."""

import json
import logging
from dataclasses import asdict
from pathlib import Path

from school.models import Student

LOGGER = logging.getLogger(__name__)


def save_students(students: list[Student], path: str | Path) -> None:
    """Write all students to a JSON file."""
    data = [asdict(student) for student in students]   # Student -> dictionary
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    LOGGER.info("Saved %d students to %s", len(students), path)


def backup_bad_file(file_path: Path) -> None:
    """Rename an unreadable data file to .bak so it is not overwritten."""
    backup = file_path.with_name(file_path.name + ".bak")
    try:
        file_path.replace(backup)
        LOGGER.warning("Unreadable file kept as %s", backup)
    except OSError as error:
        LOGGER.error("Could not back up %s: %s", file_path, error)


def load_students(path: str | Path) -> list[Student]:
    """Read students from a JSON file. A missing or broken file gives []."""
    file_path = Path(path)
    if not file_path.exists():
        LOGGER.info("No data file at %s, starting empty", file_path)
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            raw = json.load(file)
        students = [Student(**item) for item in raw]   # dictionary -> Student
    except (json.JSONDecodeError, TypeError, ValueError, KeyError) as error:
        LOGGER.error("Could not read %s: %s", file_path, error)
        backup_bad_file(file_path)
        return []
    except OSError as error:
        LOGGER.error("Could not open %s: %s", file_path, error)
        return []
    LOGGER.info("Loaded %d students from %s", len(students), file_path)
    return students
