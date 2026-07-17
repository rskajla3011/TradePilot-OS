"""
TradePilot OS
--------------

File:
    bootstrap.py

Purpose:
    Initializes the application's core infrastructure.

Author:
    Ravi Kajla

Project:
    TradePilot OS
"""

from __future__ import annotations

from pathlib import Path

from src.core.application_context import ApplicationContext
from src.core.constants import (
    CONFIG_DIRECTORY,
    DATABASE_DIRECTORY,
    LOG_DIRECTORY,
    RESOURCE_DIRECTORY,
    TEMP_DIRECTORY,
)


class Bootstrap:
    """
    Initializes all application services.

    The bootstrap executes startup tasks in a predefined order and
    registers shared services with the ApplicationContext.
    """

    def initialize(
        self,
        context: ApplicationContext,
    ) -> None:
        """
        Execute the application bootstrap sequence.
        """

        self._create_required_directories()

        context.register("configuration", self._initialize_configuration())

        context.register("settings", self._initialize_settings())

        context.register("logger", self._initialize_logger())

        context.register("database", self._initialize_database())

        context.register(
            "authentication",
            self._initialize_authentication(),
        )

        context.register(
            "service_registry",
            self._initialize_service_registry(),
        )

        context.register(
            "event_bus",
            self._initialize_event_bus(),
        )

        context.register(
            "cache",
            self._initialize_cache(),
        )

    # ------------------------------------------------------------------
    # Infrastructure
    # ------------------------------------------------------------------

    @staticmethod
    def _create_required_directories() -> None:
        """
        Create runtime directories if they do not exist.
        """

        directories: tuple[Path, ...] = (
            CONFIG_DIRECTORY,
            DATABASE_DIRECTORY,
            LOG_DIRECTORY,
            RESOURCE_DIRECTORY,
            TEMP_DIRECTORY,
        )

        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------
    # Service Initializers
    # ------------------------------------------------------------------

    @staticmethod
    def _initialize_configuration():
        """
        Initialize configuration manager.
        """
        return None

    @staticmethod
    def _initialize_settings():
        """
        Initialize settings manager.
        """
        return None

    @staticmethod
    def _initialize_logger():
        """
        Initialize logging framework.
        """
        return None

    @staticmethod
    def _initialize_database():
        """
        Initialize database manager.
        """
        return None

    @staticmethod
    def _initialize_authentication():
        """
        Initialize authentication manager.
        """
        return None

    @staticmethod
    def _initialize_service_registry():
        """
        Initialize service registry.
        """
        return None

    @staticmethod
    def _initialize_event_bus():
        """
        Initialize event bus.
        """
        return None

    @staticmethod
    def _initialize_cache():
        """
        Initialize application cache.
        """
        return None