"""
===============================================================================
TradePilot OS

Module:
    config_manager.py

Description:
    Application configuration manager.

Responsibilities:
    • Provide application configuration
    • Supply default configuration
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
    get_default_application_settings,
)
from src.config.migrations.registry import (
    build_migration_manager,
)
from src.shared.serialization.json_storage import JsonStorage
from src.shared.validation.config_validator import ConfigValidator


class ConfigManager(BaseConfigurationManager):
    """
    Application configuration manager.
    """

    def __init__(
        self,
        config_file: Path,
        migration_manager: ConfigurationMigrationManager | None = None,
    ) -> None:

        storage = JsonStorage(config_file)

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
        Return application default configuration.
        """

        return get_default_application_settings()

    # ------------------------------------------------------------------
    # Compatibility API
    # ------------------------------------------------------------------

    @property
    def config(self) -> dict[str, Any]:
        """
        Backward compatibility.

        Existing code can continue using:

            manager.config
        """

        return self.data