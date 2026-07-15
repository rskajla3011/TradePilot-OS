# TradePilot OS

> Enterprise-grade AI-Powered Trading & Investment Operating System for
> the Indian Financial Markets.

## Vision

TradePilot OS is a professional desktop trading platform designed for
serious traders and investors.

The objective is to build an enterprise-grade ecosystem that combines
market analysis, portfolio management, strategy development, risk
management, automation, and AI-assisted decision support into a single
application.

The project emphasizes clean architecture, maintainability, scalability,
and long-term extensibility over short-term shortcuts.

## Project Goals

-   Enterprise-grade software architecture
-   Modular and scalable design
-   AI-assisted trading workflow
-   High-performance desktop application
-   Professional user experience
-   Comprehensive testing
-   Complete documentation
-   Long-term maintainability

## Target Markets

Initial release focuses exclusively on the Indian financial markets.

Supported exchanges: - NSE - BSE - MCX - NCDEX

## Technology Stack

  Component        Technology
  ---------------- --------------------
  Language         Python 3.13
  UI Framework     PySide6
  Architecture     Clean Architecture
  Package Layout   src
  Type Checking    MyPy
  Formatting       Black
  Linting          Ruff
  Testing          pytest
  Logging          Loguru
  Configuration    YAML
  CLI              Typer

## Repository Structure

``` text
TradePilot-OS/
├── src/
├── shared/
├── devtools/
├── docs/
├── blueprint/
├── tests/
├── scripts/
├── tools/
└── ...
```

Application source code lives under:

``` text
src/tradepilot/
```

## Architecture

The project follows a layered architecture.

``` text
Presentation
Application
Domain
Infrastructure
```

Core principles: - SOLID - Dependency Injection - Event-Driven Design -
Modular Components - High Cohesion - Low Coupling

## Development Standards

-   Python 3.13+
-   Type hints for production code
-   Unit tests for business logic
-   Documentation for every feature
-   Architecture Decision Records (ADR)
-   Semantic Versioning
-   Git Feature Branch Workflow

## Repository Workflow

1.  Specification
2.  Implementation
3.  Unit Testing
4.  Documentation
5.  Blueprint Update
6.  Review
7.  Git Commit

## Documentation

Documentation is organized under `docs/`.

## Blueprint

Project blueprint is maintained under `blueprint/`.

## Testing

-   Unit
-   Integration
-   Performance

## Coding Standards

-   Black
-   Ruff
-   MyPy
-   EditorConfig

## Versioning

Semantic Versioning: - 0.1.0a1 - 0.1.0b1 - 0.1.0rc1 - 1.0.0

## License

MIT License during development.

## Project Status

Active Development

Current milestone: DEV-001 -- Repository Foundation

## Contributing

Every change should include: - Tests - Documentation - Architecture
compliance - Review before merge

## Contact

Project Owner: Ravi Kajla
