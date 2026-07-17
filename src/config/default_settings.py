"""
TradePilot OS
--------------

File:
    default_settings.py

Purpose:
    Defines the default application and user settings used to
    initialize configuration files.
"""

from __future__ import annotations

from typing import Any


DEFAULT_APPLICATION_SETTINGS: dict[str, Any] = {
    "application": {
        "name": "TradePilot OS",
        "version": "0.3.0",
        "theme": "system",
        "language": "en",
        "logging_level": "INFO",
    },
    "database": {
        "type": "sqlite",
        "path": "database/tradepilot.db",
    },
}


DEFAULT_USER_SETTINGS: dict[str, Any] = {
    "workspace": {
        "restore_last_session": True,
        "default_workspace": "Default",
    },
    "watchlist": {
        "default_name": "My Watchlist",
    },
    "trading": {
        "paper_trading": True,
        "default_broker": None,
    },
    "ui": {
        "window_state": "normal",
        "show_status_bar": True,
    },
}
