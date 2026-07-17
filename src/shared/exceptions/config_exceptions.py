"""
TradePilot OS
--------------

File:
    config_exceptions.py

Purpose:
    Enterprise exception hierarchy for configuration services.
"""

from __future__ import annotations


class ConfigurationError(Exception):
    """Base exception for configuration-related errors."""


class ConfigurationFileNotFoundError(ConfigurationError):
    """Raised when a configuration file cannot be found."""


class ConfigurationLoadError(ConfigurationError):
    """Raised when a configuration file cannot be loaded."""


class ConfigurationSaveError(ConfigurationError):
    """Raised when a configuration file cannot be saved."""


class ConfigurationValidationError(ConfigurationError):
    """Raised when configuration data fails validation."""


class ConfigurationMigrationError(ConfigurationError):
    """Raised when a configuration migration fails."""
