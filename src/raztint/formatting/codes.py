from ..data import BACKGROUND_LOOKUP, FOREGROUND_LOOKUP, STYLE_LOOKUP
from ..data.types import StyleName


def get_color_code(color: str | int | None) -> str | None:
    if color is None:
        return None
    if isinstance(color, int):
        if 30 <= color <= 37 or 90 <= color <= 97:
            return str(color)
        raise ValueError(
            f"Invalid ANSI foreground color code: {color}. Must be 30-37 or 90-97."
        )
    code = FOREGROUND_LOOKUP.get(color)
    if code is not None:
        return code
    raise ValueError(
        f"Unknown color: {color!r}. "
        f"Valid colors: {', '.join(sorted(FOREGROUND_LOOKUP.keys()))}"
    )


def get_background_code(bg: str | int | None) -> str | None:
    if bg is None:
        return None
    if isinstance(bg, int):
        if 40 <= bg <= 47 or 100 <= bg <= 107:
            return str(bg)
        raise ValueError(
            f"Invalid ANSI background color code: {bg}. Must be 40-47 or 100-107."
        )
    code = BACKGROUND_LOOKUP.get(bg)
    if code is not None:
        return code
    raise ValueError(
        f"Unknown background color: {bg!r}. "
        f"Valid colors: {', '.join(sorted(BACKGROUND_LOOKUP.keys()))}"
    )


def get_style_codes(style_name: str) -> tuple[str, str]:
    codes = STYLE_LOOKUP.get(style_name)
    if codes is not None:
        return codes
    raise ValueError(
        f"Unknown style: {style_name!r}. "
        f"Valid styles: {', '.join(sorted(STYLE_LOOKUP.keys()))}"
    )


def normalize_styles(
    styles: StyleName | list[StyleName] | None,
) -> tuple[str, ...]:
    if styles is None:
        return ()
    if isinstance(styles, str):
        return (styles.lower(),)
    if isinstance(styles, list):
        return tuple(s.lower() for s in styles)
    raise TypeError(
        f"styles must be str, list[str], or None, got {type(styles).__name__}"
    )
