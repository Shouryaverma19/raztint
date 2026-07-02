from ..data import BACKGROUND_LOOKUP, FOREGROUND_LOOKUP, STYLE_LOOKUP
from ..data.types import StyleName

_VALID_FG = range(30, 38), range(90, 98)
_VALID_BG = range(40, 48), range(100, 108)


def get_color_code(color: str | int | None, colors: dict[str, str]) -> str | None:
    if color is None:
        return None
    if isinstance(color, int):
        if any(color in r for r in _VALID_FG):
            return str(color)
        raise ValueError(
            f"Invalid ANSI foreground color code: {color}. "
            f"Must be 30-37 (standard) or 90-97 (bright)."
        )
    code = FOREGROUND_LOOKUP.get(color) or FOREGROUND_LOOKUP.get(color.upper())
    if code is not None:
        return code
    raise ValueError(
        f"Unknown color: {color!r}. Valid colors: {', '.join(sorted(colors.keys()))}"
    )


def get_background_code(
    bg: str | int | None, backgrounds: dict[str, str]
) -> str | None:
    if bg is None:
        return None
    if isinstance(bg, int):
        if any(bg in r for r in _VALID_BG):
            return str(bg)
        raise ValueError(
            f"Invalid ANSI background color code: {bg}. "
            f"Must be 40-47 (standard) or 100-107 (bright)."
        )
    code = BACKGROUND_LOOKUP.get(bg) or BACKGROUND_LOOKUP.get(bg.upper())
    if code is None and not bg.upper().startswith("BG_"):
        code = BACKGROUND_LOOKUP.get(f"BG_{bg.upper()}")
    if code is not None:
        return code
    raise ValueError(
        f"Unknown background color: {bg!r}. "
        f"Valid colors: {', '.join(sorted(backgrounds.keys()))}"
    )


def get_style_codes(
    style_name: str, styles: dict[str, tuple[str, str]]
) -> tuple[str, str]:
    codes = STYLE_LOOKUP.get(style_name) or STYLE_LOOKUP.get(style_name.lower())
    if codes is not None:
        return codes
    raise ValueError(
        f"Unknown style: {style_name!r}. "
        f"Valid styles: {', '.join(sorted(styles.keys()))}"
    )


def normalize_styles(
    styles: StyleName | list[StyleName] | None,
) -> list[str]:
    if styles is None:
        return []
    if isinstance(styles, str):
        return [styles.lower()]
    if isinstance(styles, list):
        return [s.lower() for s in styles]
    raise TypeError(
        f"styles must be str, list[str], or None, got {type(styles).__name__}"
    )
