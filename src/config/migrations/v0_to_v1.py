\
"""
TradePilot OS

Migration:
    Schema Version 0 -> 1

Purpose:
    Adds schema_version metadata to legacy configuration files.
"""

from __future__ import annotations

from copy import deepcopy

from src.config.schema_version import CONFIG_SCHEMA_VERSION


def migrate(config: dict) -> dict:
    """Migrate a legacy configuration (v0) to schema version 1."""
    upgraded = deepcopy(config)

    upgraded["schema_version"] = CONFIG_SCHEMA_VERSION

    return upgraded
