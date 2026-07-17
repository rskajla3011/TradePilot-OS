# STD-0001 Coding Standards

**Document ID:** STD-0001\
**Status:** Approved\
**Project:** TradePilot OS\
**Version:** 1.0.0

------------------------------------------------------------------------

# 1. Purpose

This document defines the mandatory coding standards for TradePilot OS.
All source code in the repository must comply with these standards
unless an approved ADR explicitly permits an exception.

# 2. Scope

Applies to:

-   Python source code
-   Unit and integration tests
-   Build scripts
-   Utility scripts

# 3. Guiding Principles

1.  Readability over cleverness.
2.  Consistency over personal preference.
3.  Explicit is better than implicit.
4.  Small, focused modules.
5.  Strong typing where practical.

# 4. Python Version

-   Python 3.13 is the project baseline.
-   New language features may be adopted only after project approval.

# 5. Naming Conventions

  Item       Convention         Example
  ---------- ------------------ ---------------------------
  Module     snake_case         authentication_manager.py
  Class      PascalCase         AuthenticationManager
  Function   snake_case         load_settings()
  Variable   snake_case         session_token
  Constant   UPPER_SNAKE_CASE   DEFAULT_TIMEOUT
  Enum       PascalCase         BrokerType

# 6. Project Structure

-   One responsibility per module.
-   Avoid circular imports.
-   Public APIs should remain stable.

# 7. Imports

Order imports as:

1.  Standard library
2.  Third-party packages
3.  Local packages

Avoid wildcard imports.

# 8. Type Hints

All public functions must include type hints.

Example:

``` python
def load_workspace(path: str) -> dict:
    ...
```

# 9. Dataclasses

Use dataclasses for immutable data models where appropriate.

# 10. Error Handling

-   Never silently ignore exceptions.
-   Raise specific exception types.
-   Log unexpected failures.

# 11. Logging

Use the standard logging framework.

Do not use print() outside debugging or temporary development.

# 12. Documentation

Public classes and functions should include concise docstrings.

# 13. Code Reviews

Every change should verify:

-   Naming
-   Type hints
-   Error handling
-   Logging
-   Tests
-   Documentation

# 14. Security

-   Never hardcode secrets.
-   Validate external input.
-   Escape or parameterize database operations.

# 15. Performance

Optimize only after measuring. Prefer clarity over premature
optimization.

# Revision History

  Version   Notes
  --------- -------------------------
  1.0.0     Initial coding standard
