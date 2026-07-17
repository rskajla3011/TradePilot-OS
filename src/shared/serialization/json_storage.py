"""
TradePilot OS
--------------

File:
    json_storage.py

Purpose:
    Shared JSON persistence layer used by configuration and settings services.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from src.shared.exceptions.config_exceptions import (
    ConfigurationFileNotFoundError,
    ConfigurationLoadError,
    ConfigurationSaveError,
)


class JsonStorage:
    """Provides JSON file read/write operations."""

    def __init__(self, file_path: Path) -> None:
        self._file_path = Path(file_path)

    @property
    def file_path(self) -> Path:
        return self._file_path

    def exists(self) -> bool:
        return self._file_path.exists()

    def load(self) -> dict[str, Any]:
        if not self.exists():
            raise ConfigurationFileNotFoundError(
                f"Configuration file not found: {self._file_path}"
            )
        try:
            with self._file_path.open("r", encoding="utf-8") as file:
                data = json.load(file)
        except json.JSONDecodeError as exc:
            raise ConfigurationLoadError(
                f"Invalid JSON: {self._file_path}"
            ) from exc
        except OSError as exc:
            raise ConfigurationLoadError(
                f"Unable to read: {self._file_path}"
            ) from exc

        if not isinstance(data, dict):
            raise ConfigurationLoadError(
                "Root JSON object must be a dictionary."
            )
        return data

    def save(self, data: dict[str, Any], *, indent: int = 4) -> None:
        try:
            self._file_path.parent.mkdir(parents=True, exist_ok=True)
            with self._file_path.open("w", encoding="utf-8") as file:
                json.dump(data, file, indent=indent, ensure_ascii=False)
                file.write("\n")
        except OSError as exc:
            raise ConfigurationSaveError(
                f"Unable to write: {self._file_path}"
            ) from exc
