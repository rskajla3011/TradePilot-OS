\
"""
TradePilot OS

File:
    config_manager.py

Purpose:
    Central configuration manager for application configuration.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from src.config.default_settings import DEFAULT_APPLICATION_SETTINGS
from src.shared.serialization.json_storage import JsonStorage
from src.shared.validation.config_validator import ConfigValidator


class ConfigManager:
    """Manages the application configuration file."""

    def __init__(self, config_path: Path) -> None:
        self._storage = JsonStorage(config_path)
        self._config: dict[str, Any] = {}

    @property
    def config(self) -> dict[str, Any]:
        return self._config

    def load(self) -> dict[str, Any]:
        """Load the configuration, creating defaults if necessary."""
        if not self._storage.exists():
            self._config = DEFAULT_APPLICATION_SETTINGS.copy()
            self.save()
            return self._config

        self._config = self._storage.load()
        ConfigValidator.validate_root(self._config)
        return self._config

    def save(self) -> None:
        """Persist the current configuration."""
        ConfigValidator.validate_root(self._config)
        self._storage.save(self._config)

    def get(self, key: str, default: Any = None) -> Any:
        """Get a top-level configuration value."""
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set a top-level configuration value."""
        self._config[key] = value

    def reset_to_defaults(self) -> None:
        """Reset configuration to application defaults."""
        self._config = DEFAULT_APPLICATION_SETTINGS.copy()
        self.save()
