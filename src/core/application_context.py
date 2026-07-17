"""
TradePilot OS
--------------

File:
    application_context.py

Purpose:
    Central application dependency container.

Author:
    Ravi Kajla

Project:
    TradePilot OS
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class ApplicationContext:
    """
    Stores references to shared application services.

    Services are registered during application startup and
    can be accessed throughout the application's lifetime.
    """

    configuration: Any = None
    settings: Any = None

    logger: Any = None

    database: Any = None

    authentication: Any = None

    session: Any = None

    service_registry: Any = None

    event_bus: Any = None

    cache: Any = None

    application: Any = None

    metadata: dict[str, Any] = field(default_factory=dict)

    def register(self, name: str, service: Any) -> None:
        """
        Register a service by name.

        If the ApplicationContext already has an attribute with the
        supplied name, that attribute is updated. Otherwise, the
        service is stored in the metadata dictionary.
        """
        if hasattr(self, name):
            setattr(self, name, service)
        else:
            self.metadata[name] = service

    def resolve(self, name: str) -> Any:
        """
        Retrieve a registered service.

        Raises:
            KeyError:
                If the requested service is not registered.
        """
        if hasattr(self, name):
            service = getattr(self, name)

            if service is not None:
                return service

        if name in self.metadata:
            return self.metadata[name]

        raise KeyError(f"Service '{name}' is not registered.")

    def is_registered(self, name: str) -> bool:
        """
        Returns True if a service is registered.
        """
        if hasattr(self, name):
            return getattr(self, name) is not None

        return name in self.metadata

    def unregister(self, name: str) -> None:
        """
        Remove a registered service.
        """
        if hasattr(self, name):
            setattr(self, name, None)
            return

        self.metadata.pop(name, None)

    def clear(self) -> None:
        """
        Reset the application context.
        """

        self.configuration = None
        self.settings = None
        self.logger = None
        self.database = None
        self.authentication = None
        self.session = None
        self.service_registry = None
        self.event_bus = None
        self.cache = None
        self.application = None

        self.metadata.clear()