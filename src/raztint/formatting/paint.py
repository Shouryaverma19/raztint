from functools import lru_cache

from typing_extensions import Sentinel

from ..core.protocols import FormatTarget
from ..data import INTENTS
from ..data.types import (
    BackgroundColorName,
    ColorName,
    IconMode,
    IconName,
    IntentName,
    StyleName,
)
from ..icons.resolve import resolve_icon
from ..security.masking import MaskRule
from ..security.masking import redact as mask_sensitive
from .codes import (
    get_background_code,
    get_color_code,
    get_style_codes,
    normalize_styles,
)

_RESET_FULL = "\033[0m"

UNSET = Sentinel("UNSET")
type IconArg = IconName | None | UNSET


def _icon_prefix(
    instance: FormatTarget,
    icon: IconName,
    icon_mode: IconMode | None,
) -> str:
    return resolve_icon(
        instance,
        icon,
        mode=icon_mode,
        has_nerd_fonts=instance._has_nerd_fonts,
    )


@lru_cache(maxsize=1024)
def _resolve_codes(
    color: ColorName | int | None,
    bg: BackgroundColorName | int | None,
    style_list: tuple[str, ...],
    reset: bool,
) -> tuple[str, str]:
    codes: list[str] = []

    fg_code = get_color_code(color)
    if fg_code:
        codes.append(fg_code)

    bg_code = get_background_code(bg)
    if bg_code:
        codes.append(bg_code)

    style_offs: list[str] = []
    for style_name in style_list:
        on, off = get_style_codes(style_name)
        codes.append(on)
        if not reset:
            style_offs.append(off)

    if not codes:
        return "", ""

    opening = f"\033[{';'.join(codes)}m"
    if reset:
        closing = _RESET_FULL
    elif style_offs:
        closing = f"\033[{';'.join(style_offs)}m"
    else:
        closing = ""

    return opening, closing


def format_text(
    instance: FormatTarget,
    text: str,
    color: ColorName | int | None = None,
    bg: BackgroundColorName | int | None = None,
    styles: StyleName | list[StyleName] | None = None,
    reset: bool = True,
    icon: IconArg = UNSET,
    icon_mode: IconMode | None = None,
    redact: bool = False,
    redact_rules: list[MaskRule] | None = None,
    intent: IntentName | None = None,
) -> str:
    """Format text with color, background, styles, and an optional icon."""
    if intent is not None:
        cfg = INTENTS.get(intent.lower())
        if cfg is None:
            raise ValueError(
                f"Unknown intent: {intent!r}. "
                f"Valid intents: {', '.join(sorted(INTENTS.keys()))}"
            )
        if color is None:
            color = cfg.color
        if icon is UNSET:
            icon = cfg.icon
        if styles is None:
            styles = cfg.styles

    active_icon = None if icon is UNSET else icon

    if redact:
        text = mask_sensitive(text, redact_rules)

    has_icon = active_icon is not None

    if not instance.use_color:
        if not has_icon:
            return text
        assert active_icon is not None
        return f"{_icon_prefix(instance, active_icon, icon_mode)} {text}"

    if not has_icon and color is None and bg is None and not styles:
        return text

    prefix = ""
    if has_icon:
        assert active_icon is not None
        prefix = f"{_icon_prefix(instance, active_icon, icon_mode)} "

    style_list = normalize_styles(styles)
    opening, closing = _resolve_codes(color, bg, style_list, reset)

    if not opening:
        return f"{prefix}{text}" if prefix else text

    return f"{prefix}{opening}{text}{closing}"
