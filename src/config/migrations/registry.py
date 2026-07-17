"""
===============================================================================
TradePilot OS

Module:
    registry.py

Description:
    Central migration registry.

===============================================================================
"""

from __future__ import annotations

from src.config.configuration_migration_manager import (
    ConfigurationMigrationManager,
)
from src.config.migrations.v0_to_v1 import migrate
from src.config.schema_version import CONFIG_SCHEMA_VERSION

# ----------------------------------------------------------------------
# Migration Registry
# ----------------------------------------------------------------------

MIGRATIONS: dict[int, callable] = {
    0: migrate,
}


# ----------------------------------------------------------------------
# Validation
# ----------------------------------------------------------------------

def validate_registry() -> None:
    """
    Validate migration chain.
    """

    if not MIGRATIONS:

        raise RuntimeError(
            "Migration registry is empty."
        )

    versions = sorted(MIGRATIONS.keys())

    expected = list(
        range(
            versions[0],
            CONFIG_SCHEMA_VERSION,
        )
    )

    if versions != expected:

        missing = sorted(
            set(expected) - set(versions)
        )

        raise RuntimeError(
            f"Missing migration(s): {missing}"
        )


# ----------------------------------------------------------------------
# Factory
# ----------------------------------------------------------------------

def build_migration_manager(
) -> ConfigurationMigrationManager:
    """
    Build validated migration manager.
    """

    validate_registry()

    manager = ConfigurationMigrationManager()

    for version in sorted(MIGRATIONS):

        manager.register(
            version,
            MIGRATIONS[version],
        )

    return manager