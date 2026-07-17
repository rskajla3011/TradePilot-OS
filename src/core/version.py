"""
TradePilot OS
--------------

File:
    version.py

Purpose:
    Defines application version information and helper utilities.

Author:
    Ravi Kajla

Project:
    TradePilot OS
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from functools import total_ordering


class ReleaseStage(str, Enum):
    """Supported release stages."""

    DEVELOPMENT = "Development"
    ALPHA = "Alpha"
    BETA = "Beta"
    RELEASE_CANDIDATE = "Release Candidate"
    STABLE = "Stable"


@total_ordering
@dataclass(frozen=True)
class Version:
    """
    Represents a semantic application version.
    """

    major: int
    minor: int
    patch: int
    build: int
    stage: ReleaseStage = ReleaseStage.DEVELOPMENT

    def __str__(self) -> str:
        return (
            f"{self.major}."
            f"{self.minor}."
            f"{self.patch}"
        )

    @property
    def full_version(self) -> str:
        """
        Returns the full version string.
        Example:
            0.1.0 Build 1 (Development)
        """
        return (
            f"{self} "
            f"Build {self.build} "
            f"({self.stage.value})"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Version):
            return NotImplemented

        return (
            self.major,
            self.minor,
            self.patch,
            self.build,
        ) == (
            other.major,
            other.minor,
            other.patch,
            other.build,
        )

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Version):
            return NotImplemented

        return (
            self.major,
            self.minor,
            self.patch,
            self.build,
        ) < (
            other.major,
            other.minor,
            other.patch,
            other.build,
        )


###############################################################################
# Product Information
###############################################################################

PRODUCT_NAME = "TradePilot OS"

PRODUCT_DESCRIPTION = (
    "Professional Trading & Investment Platform"
)

COMPANY_NAME = "TradePilot Technologies"

COPYRIGHT = "© 2026 TradePilot Technologies"

###############################################################################
# Current Application Version
###############################################################################

CURRENT_VERSION = Version(
    major=0,
    minor=1,
    patch=0,
    build=1,
    stage=ReleaseStage.DEVELOPMENT,
)


###############################################################################
# Helper Functions
###############################################################################

def get_version() -> Version:
    """
    Returns the current application version.
    """
    return CURRENT_VERSION


def get_version_string() -> str:
    """
    Returns the short version string.

    Example:
        0.1.0
    """
    return str(CURRENT_VERSION)


def get_full_version_string() -> str:
    """
    Returns the complete version string.

    Example:
        0.1.0 Build 1 (Development)
    """
    return CURRENT_VERSION.full_version