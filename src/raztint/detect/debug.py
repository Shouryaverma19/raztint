import os
import sys


def debug(message: str) -> None:
    """Emit debug output when RAZTINT_DEBUG is set."""
    if os.getenv("RAZTINT_DEBUG"):
        print(f"[raztint] {message}", file=sys.stderr)
