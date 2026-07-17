"""
TradePilot OS
--------------

File:
    main.py

Purpose:
    Application entry point.

Author:
    Ravi Kajla

Project:
    TradePilot OS
"""

from __future__ import annotations

import sys
import traceback

from src.core.application import Application
from src.core.bootstrap import Bootstrap


def main() -> int:
    """
    Application entry point.

    Returns
    -------
    int
        Process exit code.
    """

    application = Application()

    bootstrap = Bootstrap()

    try:

        application.initialize(bootstrap)

        application.start()

        print("TradePilot OS started successfully.")
        print(f"Version : {application.version.full_version}")

        # -----------------------------------------------------------------
        # Qt event loop will be started here in a future implementation.
        # -----------------------------------------------------------------

        return 0

    except Exception:

        print("\nApplication failed to start.\n")

        traceback.print_exc()

        return 1

    finally:

        application.shutdown()


if __name__ == "__main__":
    sys.exit(main())