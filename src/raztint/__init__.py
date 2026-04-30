from .core import RazTint

__version__ = "0.2.0"

tint = RazTint()

ok = tint.ok  # type: ignore
err = tint.err  # type: ignore
warn = tint.warn  # type: ignore
info = tint.info  # type: ignore

black = tint.black  # type: ignore
red = tint.red  # type: ignore
green = tint.green  # type: ignore
yellow = tint.yellow  # type: ignore
blue = tint.blue  # type: ignore
magenta = tint.magenta  # type: ignore
cyan = tint.cyan  # type: ignore
white = tint.white  # type: ignore
gray = tint.gray  # type: ignore

__all__ = [
    "RazTint",
    "tint",
    "ok",
    "err",
    "warn",
    "info",
    "black",
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "white",
    "gray",
    "__version__",
]
