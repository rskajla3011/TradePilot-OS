\
"""
TradePilot OS

File:
    configuration_migration_manager.py

Purpose:
    Handles configuration schema migrations.
"""

from __future__ import annotations

from typing import Callable

from src.config.schema_version import (
    CONFIG_SCHEMA_VERSION,
    create_schema_header,
    require_supported,
)

MigrationFunction = Callable[[dict], dict]


class ConfigurationMigrationManager:
    """Executes schema migrations."""

    def __init__(self) -> None:
        self._migrations: dict[int, MigrationFunction] = {}

    def register(self, from_version: int, migration: MigrationFunction) -> None:
        """Register a migration from one schema version to the next."""
        self._migrations[from_version] = migration

    def migrate(self, config: dict) -> dict:
        """Upgrade configuration to the current schema version."""
        version = config.get("schema_version", 0)

        while version < CONFIG_SCHEMA_VERSION:
            migration = self._migrations.get(version)
            if migration is None:
                raise RuntimeError(
                    f"No migration registered for schema version {version}."
                )

            config = migration(config)
            version = config.get("schema_version", version + 1)

        require_supported(version)
        return config

    @staticmethod
    def initialize(config: dict) -> dict:
        """Initialize a brand-new configuration."""
        metadata = create_schema_header()
        metadata.update(config)
        return metadata
