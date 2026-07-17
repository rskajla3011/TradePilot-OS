"""
TradePilot OS
--------------

File:
    application.py

Purpose:
    Core application runtime.

Author:
    Ravi Kajla

Project:
    TradePilot OS
"""

from __future__ import annotations

from typing import Any

from src.core.application_context import ApplicationContext
from src.core.version import CURRENT_VERSION


class Application:
    """
    Core application runtime.

    This class owns the application lifecycle and provides
    access to the shared ApplicationContext.
    """

    def __init__(self) -> None:
        self._context = ApplicationContext()

        self._is_initialized = False
        self._is_running = False

    @property
    def context(self) -> ApplicationContext:
        """
        Returns the shared application context.
        """
        return self._context

    @property
    def version(self):
        """
        Returns the current application version.
        """
        return CURRENT_VERSION

    @property
    def is_initialized(self) -> bool:
        """
        Returns True once initialization has completed.
        """
        return self._is_initialized

    @property
    def is_running(self) -> bool:
        """
        Returns True while the application is running.
        """
        return self._is_running

    def initialize(self, bootstrap: Any) -> None:
        """
        Initialize the application.

        Parameters
        ----------
        bootstrap:
            Object responsible for registering application services.
        """
        if self._is_initialized:
            return

        bootstrap.initialize(self._context)

        self._is_initialized = True

    def start(self) -> None:
        """
        Start the application.
        """
        if not self._is_initialized:
            raise RuntimeError(
                "Application must be initialized before starting."
            )

        self._is_running = True

    def shutdown(self) -> None:
        """
        Shut down the application.
        """
        if not self._is_running:
            return

        self._context.clear()

        self._is_running = False

    def get_service(self, name: str) -> Any:
        """
        Resolve a registered service.
        """
        return self._context.resolve(name)

    def register_service(
        self,
        name: str,
        service: Any,
    ) -> None:
        """
        Register a shared service.
        """
        self._context.register(name, service)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"version={self.version.full_version!r}, "
            f"initialized={self.is_initialized}, "
            f"running={self.is_running})"
        )