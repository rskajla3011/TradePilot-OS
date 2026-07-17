"""
===============================================================================
TradePilot OS

Unit Tests

deep_merge.py

===============================================================================
"""

from src.shared.utilities.deep_merge import deep_merge_dict


def test_merge_simple_dictionary():

    original = {
        "a": 1,
        "b": 2,
    }

    updated = {
        "b": 10,
        "c": 3,
    }

    result = deep_merge_dict(original, updated)

    assert result == {
        "a": 1,
        "b": 10,
        "c": 3,
    }


def test_nested_merge():

    original = {
        "database": {
            "path": "db.sqlite",
            "timeout": 30,
        }
    }

    updated = {
        "database": {
            "timeout": 60,
        }
    }

    result = deep_merge_dict(original, updated)

    assert result["database"]["path"] == "db.sqlite"

    assert result["database"]["timeout"] == 60


def test_original_dictionary_not_modified():

    original = {
        "database": {
            "timeout": 30,
        }
    }

    updated = {
        "database": {
            "timeout": 60,
        }
    }

    deep_merge_dict(original, updated)

    assert original["database"]["timeout"] == 30


def test_add_nested_dictionary():

    original = {}

    updated = {
        "ui": {
            "theme": "dark",
        }
    }

    result = deep_merge_dict(original, updated)

    assert result["ui"]["theme"] == "dark"