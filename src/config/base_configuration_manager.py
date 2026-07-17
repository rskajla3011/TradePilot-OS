"""
===============================================================================
TradePilot OS

Module:
    base_configuration_manager.py

Description:
    Enterprise base class for all configuration managers.

Responsibilities:
    • Configuration lifecycle
    • JSON persistence
    • Schema migration
    • Validation
    • Dirty-state tracking
    • Nested key access
    • Automatic schema upgrades

Author:
    TradePilot OS

===============================================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from copy import deepcopy
from typing import Any

from src.config.configuration_migration_manager import (
    ConfigurationMigrationManager,
)
from src.shared.serialization.json_storage import JsonStorage
from src.shared.validation.config_validator import ConfigValidator
from src.shared.utilities.deep_merge import deep_merge_dict


class BaseConfigurationManager(ABC):
    """
    Base class for all configuration managers.

    Derived classes only provide:

        • configuration defaults
        • storage location

    All remaining behaviour is implemented here.
    """

    def __init__(
        self,
        *,
        storage: JsonStorage,
        validator: ConfigValidator,
        migration_manager: ConfigurationMigrationManager,
    ) -> None:
        """
        Initialize the configuration manager.

        Parameters
        ----------
        storage
            JSON persistence implementation.

        validator
            Configuration validator.

        migration_manager
            Executes schema upgrades.
        """

        self._storage = storage
        self._validator = validator
        self._migration_manager = migration_manager

        self._data: dict[str, Any] = {}

        self._dirty: bool = False

        self._loaded: bool = False

        self._schema_upgraded: bool = False

    # ------------------------------------------------------------------
    # Abstract API
    # ------------------------------------------------------------------

    @abstractmethod
    def get_default_data(self) -> dict[str, Any]:
        """
        Return a NEW copy of the default configuration.

        Never return shared mutable objects.
        """
        raise NotImplementedError

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------

    @property
    def data(self) -> dict[str, Any]:
        """
        Complete configuration.
        """
        return self._data

    @property
    def is_loaded(self) -> bool:
        """
        True when configuration has been loaded.
        """
        return self._loaded

    @property
    def is_dirty(self) -> bool:
        """
        True when configuration has changed.
        """
        return self._dirty

    @property
    def schema_upgraded(self) -> bool:
        """
        True if migration occurred while loading.
        """
        return self._schema_upgraded

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _mark_dirty(self) -> None:
        """Mark configuration as modified."""
        self._dirty = True

    def _clear_dirty(self) -> None:
        """Clear dirty flag."""
        self._dirty = False

    def _clone_defaults(self) -> dict[str, Any]:
        """
        Return safe copy of defaults.
        """
        return deepcopy(self.get_default_data())

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def load(self) -> dict[str, Any]:
        """
        Load configuration from storage.

        Workflow
        --------
        1. Create defaults if the file does not exist.
        2. Load configuration from disk.
        3. Apply schema migrations if required.
        4. Validate configuration.
        5. Save automatically if migration occurred.
        """

        self._schema_upgraded = False

        # --------------------------------------------------------------
        # First run
        # --------------------------------------------------------------

        if not self._storage.exists():

            self._data = self._migration_manager.initialize(
                self._clone_defaults()
            )

            self._validator.validate_root(self._data)

            self._storage.save(self._data)

            self._loaded = True

            self._clear_dirty()

            return self._data

        # --------------------------------------------------------------
        # Existing configuration
        # --------------------------------------------------------------

        self._data = self._storage.load()

        original_schema = self._data.get("schema_version", 0)

        self._data = self._migration_manager.migrate(self._data)

        current_schema = self._data.get("schema_version", 0)

        self._schema_upgraded = current_schema != original_schema

        # --------------------------------------------------------------
        # Validate migrated configuration
        # --------------------------------------------------------------

        self._validator.validate_root(self._data)

        # --------------------------------------------------------------
        # Persist upgraded configuration
        # --------------------------------------------------------------

        if self._schema_upgraded:

            self._storage.save(self._data)

        self._loaded = True

        self._clear_dirty()

        return self._data

    def reload(self) -> dict[str, Any]:
        """
        Reload configuration from disk.

        Any unsaved in-memory changes are discarded.
        """

        self._loaded = False

        self._dirty = False

        return self.load()

    def save(self) -> None:
        """
        Persist configuration.

        Raises
        ------
        ConfigurationValidationError
            When configuration is invalid.
        """

        self._validator.validate_root(self._data)

        self._storage.save(self._data)

        self._clear_dirty()

    # ------------------------------------------------------------------
    # Configuration Access
    # ------------------------------------------------------------------

    def get(self, path: str, default: Any = None) -> Any:
        """
        Retrieve a configuration value using dot notation.

        Example
        -------
        get("database.path")
        get("ui.theme")
        """

        if not path:
            return self._data

        current: Any = self._data

        for key in path.split("."):

            if not isinstance(current, dict):
                return default

            if key not in current:
                return default

            current = current[key]

        return current

    def has(self, path: str) -> bool:
        """
        Return True if the specified configuration path exists.
        """

        sentinel = object()

        return self.get(path, sentinel) is not sentinel

    def set(self, path: str, value: Any) -> None:
        """
        Set a configuration value using dot notation.

        Missing parent dictionaries are created automatically.

        Example
        -------
        set("database.path", "database/app.db")
        """

        if not path:
            raise ValueError("Configuration path cannot be empty.")

        keys = path.split(".")

        current = self._data

        for key in keys[:-1]:

            node = current.get(key)

            if node is None:

                node = {}

                current[key] = node

            elif not isinstance(node, dict):

                raise TypeError(
                    f"'{key}' is not a configuration section."
                )

            current = node

        current[keys[-1]] = value

        self._mark_dirty()

    def remove(self, path: str) -> bool:
        """
        Remove a configuration value.

        Returns
        -------
        bool
            True if a value was removed.
        """

        if not path:
            return False

        keys = path.split(".")

        current = self._data

        for key in keys[:-1]:

            if key not in current:
                return False

            current = current[key]

            if not isinstance(current, dict):
                return False

        last_key = keys[-1]

        if last_key not in current:
            return False

        del current[last_key]

        self._mark_dirty()

        return True

    def update(
            self,
            values: dict[str, Any],
    ) -> None:
        """
        Recursively update configuration values.
        """

        if not values:
            return

        self._data = deep_merge_dict(
            self._data,
            values,
        )

        self._mark_dirty()

    def clear(self) -> None:
        """
        Remove all configuration values.
        """

        self._data.clear()

        self._mark_dirty()

    # ------------------------------------------------------------------
    # Default Configuration
    # ------------------------------------------------------------------

    def reset_to_defaults(self) -> None:
        """
        Reset configuration to default values.

        The configuration is recreated from the default provider,
        initialized with the current schema metadata, validated,
        and immediately persisted.
        """

        self._data = self._migration_manager.initialize(
            self._clone_defaults()
        )

        self._validator.validate_root(self._data)

        self.save()

        self._loaded = True

    # ------------------------------------------------------------------
    # Utility Methods
    # ------------------------------------------------------------------

    def as_dict(self) -> dict[str, Any]:
        """
        Return a deep copy of the configuration.

        Callers receive a copy so they cannot accidentally modify
        the manager's internal state.
        """

        return deepcopy(self._data)

    def replace(self, configuration: dict[str, Any]) -> None:
        """
        Replace the complete configuration.

        The supplied configuration is validated before becoming
        the active runtime configuration.
        """

        configuration = deepcopy(configuration)

        configuration = self._migration_manager.migrate(configuration)

        self._validator.validate_root(configuration)

        self._data = configuration

        self._mark_dirty()

    # ------------------------------------------------------------------
    # Python Special Methods
    # ------------------------------------------------------------------

    def __contains__(self, path: str) -> bool:
        """
        Support:

            if "database.path" in manager:
        """

        return self.has(path)

    def __getitem__(self, path: str) -> Any:
        """
        Support:

            value = manager["database.path"]
        """

        value = self.get(path)

        if value is None:
            raise KeyError(path)

        return value

    def __setitem__(self, path: str, value: Any) -> None:
        """
        Support:

            manager["database.path"] = "database/app.db"
        """

        self.set(path, value)

    def __len__(self) -> int:
        """
        Number of top-level configuration sections.
        """

        return len(self._data)

    def __repr__(self) -> str:
        """
        Developer-friendly representation.
        """

        return (
            f"{self.__class__.__name__}("
            f"loaded={self._loaded}, "
            f"dirty={self._dirty}, "
            f"schema_upgraded={self._schema_upgraded})"
        )