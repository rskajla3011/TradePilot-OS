\
"""
TradePilot OS

Migration Registry

Registers all available configuration schema migrations.
"""

from __future__ import annotations

from src.config.configuration_migration_manager import ConfigurationMigrationManager
from src.config.migrations.v0_to_v1 import migrate as migrate_v0_to_v1


def build_migration_manager() -> ConfigurationMigrationManager:
    """Create a migration manager with all supported migrations registered."""
    manager = ConfigurationMigrationManager()

    # Version 0 -> Version 1
    manager.register(0, migrate_v0_to_v1)

    return manager
