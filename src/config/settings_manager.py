\
"""
TradePilot OS

File:
    settings_manager.py

Purpose:
    Manages user-specific settings.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from src.config.default_settings import DEFAULT_USER_SETTINGS
from src.shared.serialization.json_storage import JsonStorage
from src.shared.validation.config_validator import ConfigValidator


class SettingsManager:
    """Manages user settings stored in a JSON file."""

    def __init__(self, settings_path: Path) -> None:
        self._storage = JsonStorage(settings_path)
        self._settings: dict[str, Any] = {}

    @property
    def settings(self) -> dict[str, Any]:
        return self._settings

    def load(self) -> dict[str, Any]:
        """Load settings or create defaults if missing."""
        if not self._storage.exists():
            self._settings = DEFAULT_USER_SETTINGS.copy()
            self.save()
            return self._settings

        self._settings = self._storage.load()
        ConfigValidator.validate_root(self._settings)
        return self._settings

    def save(self) -> None:
        """Save settings to disk."""
        ConfigValidator.validate_root(self._settings)
        self._storage.save(self._settings)

    def get(self, key: str, default: Any = None) -> Any:
        """Return a top-level setting."""
        return self._settings.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Update a top-level setting."""
        self._settings[key] = value

    def reset_to_defaults(self) -> None:
        """Restore default user settings."""
        self._settings = DEFAULT_USER_SETTINGS.copy()
        self.save()
