"""
===============================================================================
TradePilot OS

Module:
    configuration_migration_manager.py

Description:
    Configuration schema migration manager.

Responsibilities:
    • Initialize new configurations
    • Execute schema migrations
    • Validate migration chain
    • Upgrade legacy configurations

===============================================================================
"""

from __future__ import annotations

from copy import deepcopy
from typing import Callable

from src.config.schema_version import (
    CONFIG_SCHEMA_VERSION,
    create_schema_header,
    require_supported,
)

MigrationFunction = Callable[[dict], dict]


class ConfigurationMigrationManager:
    """
    Executes configuration schema migrations.
    """

    def __init__(self) -> None:

        self._migrations: dict[int, MigrationFunction] = {}

    # ------------------------------------------------------------------
    # Registration
    # ------------------------------------------------------------------

    def register(
        self,
        from_version: int,
        migration: MigrationFunction,
    ) -> None:
        """
        Register a migration.

        Example

            register(1, migrate_v1_to_v2)
        """

        if from_version in self._migrations:

            raise ValueError(
                f"Migration already registered for schema {from_version}."
            )

        self._migrations[from_version] = migration

    # ------------------------------------------------------------------
    # Initialization
    # ------------------------------------------------------------------

    def initialize(
        self,
        configuration: dict,
    ) -> dict:
        """
        Create a versioned configuration.
        """

        configuration = deepcopy(configuration)

        header = create_schema_header()

        header.update(configuration)

        return header

    # ------------------------------------------------------------------
    # Migration
    # ------------------------------------------------------------------

    def migrate(
        self,
        configuration: dict,
    ) -> dict:
        """
        Upgrade configuration to the latest schema.
        """

        configuration = deepcopy(configuration)

        version = configuration.get("schema_version", 0)

        while version < CONFIG_SCHEMA_VERSION:

            migration = self._migrations.get(version)

            if migration is None:

                raise RuntimeError(
                    f"No migration registered for schema {version}."
                )

            configuration = migration(configuration)

            version = configuration.get(
                "schema_version",
                version + 1,
            )

        require_supported(version)

        return configuration

    # ------------------------------------------------------------------
    # Information
    # ------------------------------------------------------------------

    @property
    def registered_versions(self) -> tuple[int, ...]:
        """
        Registered migration versions.
        """

        return tuple(sorted(self._migrations.keys()))

    def has_migration(
        self,
        version: int,
    ) -> bool:
        """
        True if migration exists.
        """

        return version in self._migrations