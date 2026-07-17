\
"""
TradePilot OS

File:
    base_configuration_manager.py

Purpose:
    Shared base implementation for configuration managers.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from src.shared.serialization.json_storage import JsonStorage
from src.shared.validation.config_validator import ConfigValidator


class BaseConfigurationManager(ABC):
    """Base class providing common configuration behavior."""

    def __init__(self, storage: JsonStorage) -> None:
        self._storage = storage
        self._data: dict[str, Any] = {}
        self._dirty = False

    @abstractmethod
    def get_default_data(self) -> dict[str, Any]:
        """Return a fresh default configuration."""

    @property
    def data(self) -> dict[str, Any]:
        return self._data

    def load(self) -> dict[str, Any]:
        if not self._storage.exists():
            self._data = self.get_default_data()
            self.save()
            return self._data

        self._data = self._storage.load()
        ConfigValidator.validate_root(self._data)
        self._dirty = False
        return self._data

    def reload(self) -> dict[str, Any]:
        return self.load()

    def save(self) -> None:
        ConfigValidator.validate_root(self._data)
        self._storage.save(self._data)
        self._dirty = False

    def has(self, path: str) -> bool:
        try:
            self.get(path)
            return True
        except KeyError:
            return False

    def get(self, path: str, default: Any = None) -> Any:
        current: Any = self._data
        for key in path.split("."):
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                if default is not None:
                    return default
                raise KeyError(path)
        return current

    def set(self, path: str, value: Any) -> None:
        current = self._data
        keys = path.split(".")
        for key in keys[:-1]:
            current = current.setdefault(key, {})
        current[keys[-1]] = value
        self._dirty = True

    def remove(self, path: str) -> None:
        current = self._data
        keys = path.split(".")
        for key in keys[:-1]:
            current = current[key]
        del current[keys[-1]]
        self._dirty = True

    def reset_to_defaults(self) -> None:
        self._data = self.get_default_data()
        self.save()
