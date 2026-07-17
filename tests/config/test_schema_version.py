"""
===============================================================================
TradePilot OS

Unit Tests

schema_version.py

===============================================================================
"""

from src.config.schema_version import (
    CONFIG_SCHEMA_VERSION,
    create_schema_header,
    is_supported,
)


def test_schema_header():

    header = create_schema_header()

    assert header["schema_version"] == CONFIG_SCHEMA_VERSION


def test_current_schema_supported():

    assert is_supported(CONFIG_SCHEMA_VERSION)


def test_negative_schema_not_supported():

    assert not is_supported(-1)


def test_future_schema_not_supported():

    assert not is_supported(
        CONFIG_SCHEMA_VERSION + 10
    )