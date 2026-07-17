# ADR-0003 -- Base Configuration Manager

**Document ID:** ADR-0003\
**Project:** TradePilot OS\
**Status:** Approved\
**Version:** 1.0.0

------------------------------------------------------------------------

# Context

`ConfigManager` and `SettingsManager` have evolved to provide nearly
identical behavior including loading, saving, validation, nested key
access, dirty-state tracking, and reset operations.

Continuing to evolve them independently would duplicate logic and
increase maintenance effort.

------------------------------------------------------------------------

# Decision

Introduce a new abstract base class:

``` text
src/
└── config/
    ├── base_configuration_manager.py
    ├── config_manager.py
    └── settings_manager.py
```

The base class will encapsulate common configuration behavior while
derived classes provide only application-specific defaults and storage
locations.

------------------------------------------------------------------------

# Responsibilities

## BaseConfigurationManager

-   Load
-   Save
-   Reload
-   Get
-   Set
-   Remove
-   Has
-   Dirty-state tracking
-   Validation
-   JSON persistence

## ConfigManager

-   Application defaults
-   Application configuration

## SettingsManager

-   User defaults
-   User settings

------------------------------------------------------------------------

# Benefits

-   Reduced code duplication
-   Consistent API
-   Easier testing
-   Simplified maintenance
-   Better extensibility

------------------------------------------------------------------------

# Consequences

This is an internal refactoring. Public behavior remains unchanged while
the implementation becomes cleaner and easier to evolve.

------------------------------------------------------------------------

# Related Documents

-   ADR-0001 Project Technology Stack
-   ADR-0002 Shared Infrastructure Layer
-   GOV-0001 Project Governance
