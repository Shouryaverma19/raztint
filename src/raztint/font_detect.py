import os
import subprocess
import sys
from functools import lru_cache


def _debug(message: str) -> None:
    """Emit debug output when RAZTINT_DEBUG is set."""
    if os.getenv("RAZTINT_DEBUG"):
        print(f"[raztint] {message}", file=sys.stderr)


@lru_cache(maxsize=1)
def check_installed_nerd_fonts() -> bool:
    """Check if nerd fonts are installed on the system."""
    if os.name == "nt":
        try:
            result = subprocess.run(
                [
                    "powershell",
                    "-Command",
                    (
                        "Get-ChildItem 'C:\\Windows\\Fonts' | "
                        "Where-Object {$_.Name -like 'Nerd'} | "
                        "Select-Object -First 1"
                    ),
                ],
                capture_output=True,
                text=True,
                timeout=2,
            )
            has_fonts = result.returncode == 0 and bool(result.stdout.strip())
            _debug(
                f"Font detection (Windows): returncode={result.returncode}, has_fonts={has_fonts}"
            )
            return has_fonts
        except Exception as exc:
            _debug(f"Font detection (Windows) failed: {exc!r}")
            return False

    elif sys.platform == "darwin":
        try:
            result = subprocess.run(
                ["system_profiler", "SPFontsDataType"],
                capture_output=True,
                text=True,
                timeout=2,
            )
            if result.returncode == 0 and any(
                n in result.stdout.lower() for n in ["nerd", "nf-"]
            ):
                _debug("Font detection (macOS): nerd font found via system_profiler")
                return True
        except Exception as exc:
            _debug(f"Font detection (macOS system_profiler) failed: {exc!r}")

        font_dirs = [
            os.path.expanduser("~/Library/Fonts"),
            "/Library/Fonts",
            "/System/Library/Fonts",
        ]
        for font_dir in font_dirs:
            if os.path.isdir(font_dir):
                try:
                    if any(
                        "nerd" in f.lower() or "nf-" in f.lower()
                        for f in os.listdir(font_dir)
                    ):
                        _debug(f"Font detection (macOS): nerd font found in {font_dir}")
                        return True
                except Exception as exc:
                    _debug(f"Font detection (macOS) failed for {font_dir}: {exc!r}")
                    continue
    else:
        try:
            result = subprocess.run(
                ["fc-list", ":", "family"], capture_output=True, text=True, timeout=2
            )
            if result.returncode == 0:
                found = any(
                    n in result.stdout.lower()
                    for n in ["nerd", "nf-", "hack nerd", "fira code nerd"]
                )
                _debug(
                    f"Font detection (POSIX): returncode={result.returncode}, found={found}"
                )
                return found
        except Exception as exc:
            _debug(f"Font detection (POSIX) failed: {exc!r}")

    _debug("Font detection: no nerd fonts detected")
    return False


@lru_cache(maxsize=1)
def has_nerd_fonts() -> bool:
    """Detect if nerd fonts are available in the terminal."""
    nerd_env = os.getenv("NERDFONTS") or os.getenv("NERD_FONTS")
    if nerd_env and nerd_env.lower() in ("1", "true", "yes", "on"):
        _debug("Nerd fonts: enabled via NERDFONTS/NERD_FONTS")
        return True

    indicators = [
        "nerd",
        "nf-",
        "hack nerd",
        "fira code nerd",
        "jetbrains mono nerd",
        "meslo nerd",
        "cascadia code nerd",
    ]

    font_name = os.getenv("FONT_NAME", "").lower()
    if font_name and any(name in font_name for name in indicators):
        _debug(f"Nerd fonts: enabled via FONT_NAME={font_name!r}")
        return True

    term_font = os.getenv("TERM_FONT", "").lower()
    if term_font and any(name in term_font for name in indicators):
        _debug(f"Nerd fonts: enabled via TERM_FONT={term_font!r}")
        return True

    if os.getenv("RAZTINT_SKIP_SYSTEM_FONT_SCAN", "").lower() in (
        "1",
        "true",
        "yes",
        "on",
    ):
        _debug(
            "Nerd fonts: skipping system font scan due to RAZTINT_SKIP_SYSTEM_FONT_SCAN"
        )
        return False

    return check_installed_nerd_fonts()
