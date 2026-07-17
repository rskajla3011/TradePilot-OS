"""
TradePilot OS

File:
    schema_version.py

Purpose:
    Central definition of the configuration schema version and helpers.
"""

from __future__ import annotations

from dataclasses import dataclass

CONFIG_SCHEMA_VERSION = 1


@dataclass(frozen=True)
class SchemaInfo:
    """Represents configuration schema metadata."""

    version: int
    description: str


CURRENT_SCHEMA = SchemaInfo(
    version=CONFIG_SCHEMA_VERSION,
    description="Initial versioned configuration schema",
)


def create_schema_header() -> dict:
    """Return metadata to be embedded in configuration files."""
    return {
        "schema_version": CURRENT_SCHEMA.version,
    }


def is_supported(version: int) -> bool:
    """Return True if the supplied schema version is supported."""
    return version == CONFIG_SCHEMA_VERSION


def require_supported(version: int) -> None:
    """Raise if the schema version is unsupported."""
    if not is_supported(version):
        raise ValueError(
            f"Unsupported configuration schema version: {version}. "
            f"Expected {CONFIG_SCHEMA_VERSION}."
        )
