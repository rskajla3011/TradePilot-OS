"""
===============================================================================
TradePilot OS

Module:
    settings_manager.py

Description:
    User settings manager.

Responsibilities:
    • Provide user settings
    • Supply default settings
    • Configure dependency injection

===============================================================================
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from src.config.base_configuration_manager import BaseConfigurationManager
from src.config.configuration_migration_manager import (
    ConfigurationMigrationManager,
)
from src.config.default_settings import (
    get_default_user_settings,
)
from src.config.migrations.registry import (
    build_migration_manager,
)
from src.shared.serialization.json_storage import JsonStorage
from src.shared.validation.config_validator import ConfigValidator


class SettingsManager(BaseConfigurationManager):
    """
    User settings manager.
    """

    def __init__(
        self,
        settings_file: Path,
        migration_manager: ConfigurationMigrationManager | None = None,
    ) -> None:

        storage = JsonStorage(settings_file)

        validator = ConfigValidator()

        migration_manager = (
            migration_manager
            if migration_manager is not None
            else build_migration_manager()
        )

        super().__init__(
            storage=storage,
            validator=validator,
            migration_manager=migration_manager,
        )

    # ------------------------------------------------------------------
    # Default configuration
    # ------------------------------------------------------------------

    def get_default_data(self) -> dict[str, Any]:
        """
        Return user default settings.
        """

        return get_default_user_settings()

    # ------------------------------------------------------------------
    # Compatibility API
    # ------------------------------------------------------------------

    @property
    def settings(self) -> dict[str, Any]:
        """
        Backward compatibility.

        Existing code can continue using:

            manager.settings
        """

        return self.data