# ADR-0002 -- Shared Infrastructure Layer

**Document ID:** ADR-0002\
**Project:** TradePilot OS\
**Version:** 1.0.0\
**Status:** Approved

------------------------------------------------------------------------

# 1. Context

During implementation of the Configuration & Settings Framework
(TP-IMP-E002-TSK-0002), it became clear that multiple modules required
common infrastructure such as exception classes, serialization helpers,
validators, and utility functions.

Keeping these components inside individual feature packages would lead
to duplicated code, inconsistent implementations, and circular
dependencies.

------------------------------------------------------------------------

# 2. Decision

A new top-level package named `shared` is introduced under `src/`.

``` text
src/
└── shared/
    ├── exceptions/
    ├── serialization/
    ├── validation/
    ├── utilities/
    └── types/
```

This package will contain reusable infrastructure that is independent of
business domains.

------------------------------------------------------------------------

# 3. What Belongs in `shared`

-   Common exception classes
-   Serialization helpers (JSON, CSV, etc.)
-   Validation utilities
-   Generic helper functions
-   Shared type definitions
-   Reusable infrastructure components

------------------------------------------------------------------------

# 4. What Must NOT Belong in `shared`

-   Trading logic
-   Broker implementations
-   Database repositories
-   UI components
-   Configuration business logic
-   Portfolio or risk calculations

Feature-specific code must remain in its respective package.

------------------------------------------------------------------------

# 5. Dependency Rules

`shared` is a foundational package.

Allowed:

-   core → shared
-   config → shared
-   database → shared
-   authentication → shared
-   ui → shared

Not allowed:

-   shared → config
-   shared → database
-   shared → ui
-   shared → trading
-   shared → portfolio

Dependencies must always point toward `shared`, never away from it.

------------------------------------------------------------------------

# 6. Consequences

Benefits:

-   Reduced duplication
-   Cleaner architecture
-   Improved maintainability
-   Easier testing
-   Consistent error handling

Trade-off:

-   Developers must avoid placing feature-specific logic inside
    `shared`.

------------------------------------------------------------------------

# 7. Related Documents

-   ARCH-0001 Architecture Overview
-   ADR-0001 Project Technology Stack
-   IMP-0001 Implementation Guide

------------------------------------------------------------------------

# Revision History

  Version   Description
  --------- ----------------------------------------
  1.0.0     Introduced Shared Infrastructure Layer
