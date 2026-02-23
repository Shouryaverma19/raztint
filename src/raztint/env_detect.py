import os
import sys

from .font_detect import has_nerd_fonts


def _debug(message: str) -> None:
    """Emit debug output when RAZTINT_DEBUG is set."""
    if os.getenv("RAZTINT_DEBUG"):
        print(f"[raztint] {message}", file=sys.stderr)


def enable_windows_vt_mode() -> bool:
    import ctypes

    windll = getattr(ctypes, "windll", None)
    if windll is None or getattr(windll, "kernel32", None) is None:
        _debug("Windows VT: windll/kernel32 not available")
        return False

    handle = windll.kernel32.GetStdHandle(-11)
    if handle in (0, -1):
        _debug(f"Windows VT: invalid handle {handle!r}")
        return False

    mode = ctypes.c_uint32()
    if not windll.kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
        _debug("Windows VT: GetConsoleMode failed")
        return False

    success = bool(windll.kernel32.SetConsoleMode(handle, mode.value | 0x0004))
    _debug(f"Windows VT: SetConsoleMode -> {success}")
    return success


def supports_color() -> bool:
    if os.getenv("NO_COLOR") or os.getenv("RAZTINT_NO_COLOR"):
        _debug("Color disabled by NO_COLOR/RAZTINT_NO_COLOR")
        return False

    force = os.getenv("RAZTINT_FORCE_COLOR", "").lower()
    if force in ("1", "true", "yes", "on"):
        _debug("Color forced by RAZTINT_FORCE_COLOR")
        return True

    if not hasattr(sys.stdout, "isatty") or not sys.stdout.isatty():
        _debug("Color disabled: stdout is not a TTY")
        return False

    if os.name == "nt":
        _debug("Color detection: Windows path")
        return enable_windows_vt_mode()

    term = os.getenv("TERM", "")
    result = bool(term and term.lower() != "dumb")
    _debug(f"Color detection: TERM={term!r} -> {result}")
    return result


def get_icon_mode() -> str:
    encoding = getattr(sys.stdout, "encoding", None) or "utf-8"
    try:
        "[󰄬]".encode(encoding)
    except Exception:
        _debug(
            f"Icon mode: encoding {encoding!r} cannot encode Nerd icons, using ascii"
        )
        return "ascii"

    if os.getenv("RAZTINT_USE_NERD_ICONS", "").lower() in ("1", "true", "yes", "on"):
        _debug("Icon mode forced to 'nerd' via RAZTINT_USE_NERD_ICONS")
        return "nerd"

    if os.getenv("RAZTINT_NO_NERD_ICONS", "").lower() in ("1", "true", "yes", "on"):
        _debug("Icon mode forced to 'std' via RAZTINT_NO_NERD_ICONS")
        return "std"

    if has_nerd_fonts():
        _debug("Icon mode: nerd fonts detected, using 'nerd'")
        return "nerd"

    _debug("Icon mode: defaulting to 'std'")
    return "std"
