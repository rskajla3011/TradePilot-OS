"""
TradePilot OS
--------------

File:
    constants.py

Purpose:
    Defines application-wide immutable constants.

Author:
    Ravi Kajla

Project:
    TradePilot OS
"""

from __future__ import annotations

from pathlib import Path

###############################################################################
# Application Information
###############################################################################

APPLICATION_NAME: str = "TradePilot OS"

APPLICATION_SHORT_NAME: str = "TradePilot"

COMPANY_NAME: str = "TradePilot Technologies"

ORGANIZATION_DOMAIN: str = "tradepilot.local"

###############################################################################
# Folder Structure
###############################################################################

PROJECT_ROOT: Path = Path(__file__).resolve().parents[2]

SRC_DIRECTORY: Path = PROJECT_ROOT / "src"

CONFIG_DIRECTORY: Path = PROJECT_ROOT / "config"

DATABASE_DIRECTORY: Path = PROJECT_ROOT / "database"

RESOURCE_DIRECTORY: Path = PROJECT_ROOT / "resources"

DOCUMENT_DIRECTORY: Path = PROJECT_ROOT / "docs"

LOG_DIRECTORY: Path = PROJECT_ROOT / "logs"

TEMP_DIRECTORY: Path = PROJECT_ROOT / "temp"

###############################################################################
# Resource Folders
###############################################################################

ICON_DIRECTORY: Path = RESOURCE_DIRECTORY / "icons"

IMAGE_DIRECTORY: Path = RESOURCE_DIRECTORY / "images"

STYLE_DIRECTORY: Path = RESOURCE_DIRECTORY / "styles"

TRANSLATION_DIRECTORY: Path = RESOURCE_DIRECTORY / "translations"

###############################################################################
# Database
###############################################################################

SQLITE_DATABASE_NAME: str = "tradepilot.db"

SQLITE_DATABASE_PATH: Path = (
    DATABASE_DIRECTORY
    / "sqlite"
    / SQLITE_DATABASE_NAME
)

###############################################################################
# Configuration Files
###############################################################################

APPLICATION_SETTINGS_FILE: Path = (
    CONFIG_DIRECTORY
    / "application.json"
)

USER_SETTINGS_FILE: Path = (
    CONFIG_DIRECTORY
    / "user.json"
)

###############################################################################
# Logging
###############################################################################

LOG_FILE_NAME: str = "tradepilot.log"

###############################################################################
# Supported Exchanges
###############################################################################

SUPPORTED_EXCHANGES: tuple[str, ...] = (
    "NSE",
    "BSE",
    "MCX",
    "NCDEX",
)

###############################################################################
# Supported Brokers (Phase 1)
###############################################################################

SUPPORTED_BROKERS: tuple[str, ...] = (
    "Upstox",
    "Zerodha",
    "Motilal Oswal",
    "INDmoney",
)

###############################################################################
# Supported Theme Modes
###############################################################################

SUPPORTED_THEMES: tuple[str, ...] = (
    "Light",
    "Dark",
)

###############################################################################
# Date Formats
###############################################################################

DATE_FORMAT: str = "%d-%m-%Y"

TIME_FORMAT: str = "%H:%M:%S"

DATE_TIME_FORMAT: str = "%d-%m-%Y %H:%M:%S"