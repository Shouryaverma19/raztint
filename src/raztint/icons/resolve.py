from collections.abc import Callable

from ..core.protocols import IconHost
from ..detect.env import env_enabled


def resolve_icon(
    ctx: IconHost,
    icon_name: str,
    mode: str | None = None,
    *,
    has_nerd_fonts: Callable[[], bool],
) -> str:
    """Resolve icon symbol by name and render mode."""
    icon_upper = icon_name.upper()
    data = ctx.icons.get(icon_upper)
    if data is None:
        raise ValueError(
            f"Unknown icon: {icon_name!r}. "
            f"Valid icons: {', '.join(sorted(ctx.icons.keys()))}"
        )

    effective_mode = mode if mode is not None else ctx.icon_mode

    if effective_mode == "auto":
        nerd = data.get("nerd")
        std = data.get("std")
        if nerd and (
            env_enabled("RAZTINT_USE_NERD_ICONS")
            or ctx.icon_mode == "nerd"
            or has_nerd_fonts()
        ):
            symbol = nerd
        elif std:
            symbol = std
        else:
            symbol = data["ascii"]
    elif effective_mode == "nerd":
        symbol = data.get("nerd") or data.get("std") or data["ascii"]
    elif effective_mode == "std":
        symbol = data.get("std") or data["ascii"]
    else:
        symbol = data["ascii"]

    color_code = ctx.colors.get(data.get("color", "WHITE"), "37")
    return ctx.color(symbol, color_code)
