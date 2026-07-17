"""
===============================================================================
TradePilot OS

Module:
    deep_merge.py

Description:
    Utility functions for recursively merging dictionaries.

Responsibilities:
    • Preserve nested configuration values
    • Merge only modified values
    • Avoid overwriting entire sections

===============================================================================
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any


def deep_merge_dict(
    destination: dict[str, Any],
    source: dict[str, Any],
) -> dict[str, Any]:
    """
    Recursively merge source into destination.

    Parameters
    ----------
    destination
        Original dictionary.

    source
        Dictionary containing updates.

    Returns
    -------
    dict
        Merged dictionary.
    """

    result = deepcopy(destination)

    for key, value in source.items():

        if (
            key in result
            and isinstance(result[key], dict)
            and isinstance(value, dict)
        ):
            result[key] = deep_merge_dict(
                result[key],
                value,
            )

        else:
            result[key] = deepcopy(value)

    return result