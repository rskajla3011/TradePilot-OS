"""
TradePilot OS
--------------

File:
    config_validator.py

Purpose:
    Shared configuration validation framework.
"""

from __future__ import annotations

from typing import Any

from src.shared.exceptions.config_exceptions import (
    ConfigurationValidationError,
)


class ConfigValidator:
    """Utility methods for validating configuration data."""

    @staticmethod
    def validate_root(data: Any) -> None:
        if not isinstance(data, dict):
            raise ConfigurationValidationError(
                "Configuration root must be a dictionary."
            )

    @staticmethod
    def require_keys(data: dict[str, Any], keys: list[str]) -> None:
        missing = [k for k in keys if k not in data]
        if missing:
            raise ConfigurationValidationError(
                f"Missing required configuration keys: {', '.join(missing)}"
            )

    @staticmethod
    def validate_type(
        data: dict[str, Any],
        key: str,
        expected_type: type,
    ) -> None:
        if key in data and not isinstance(data[key], expected_type):
            raise ConfigurationValidationError(
                f"'{key}' must be of type {expected_type.__name__}."
            )

    @staticmethod
    def validate_string(
        data: dict[str, Any],
        key: str,
        *,
        allow_empty: bool = False,
    ) -> None:
        ConfigValidator.validate_type(data, key, str)
        if key in data and not allow_empty and not data[key].strip():
            raise ConfigurationValidationError(
                f"'{key}' cannot be empty."
            )

    @staticmethod
    def validate_number_range(
        value: int | float,
        *,
        minimum: int | float | None = None,
        maximum: int | float | None = None,
    ) -> None:
        if minimum is not None and value < minimum:
            raise ConfigurationValidationError(
                f"Value must be >= {minimum}."
            )
        if maximum is not None and value > maximum:
            raise ConfigurationValidationError(
                f"Value must be <= {maximum}."
            )

    @staticmethod
    def validate_boolean(
        data: dict[str, Any],
        key: str,
    ) -> None:
        ConfigValidator.validate_type(data, key, bool)

    @staticmethod
    def require_nested_key(
        data: dict[str, Any],
        *path: str,
    ) -> None:
        current: Any = data
        for key in path:
            if not isinstance(current, dict) or key not in current:
                raise ConfigurationValidationError(
                    f"Missing nested configuration key: {' -> '.join(path)}"
                )
            current = current[key]
