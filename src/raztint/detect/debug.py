import os
import sys
from collections.abc import Callable
from functools import lru_cache


@lru_cache(maxsize=1)
def _debug_enabled() -> bool:
    return bool(os.getenv("RAZTINT_DEBUG"))


def clear_debug_cache() -> None:
    _debug_enabled.cache_clear()


def debug(message: str | Callable[[], str]) -> None:
    if not _debug_enabled():
        return

    if isinstance(message, str):
        text = message
    else:
        text = message()

    print(f"[raztint] {text}", file=sys.stderr)
