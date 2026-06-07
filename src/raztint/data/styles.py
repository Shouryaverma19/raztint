"""ANSI style codes for text styling."""

STYLES: dict[str, tuple[str, str]] = {
    "BOLD": ("1", "22"),
    "DIM": ("2", "22"),
    "ITALIC": ("3", "23"),
    "UNDERLINE": ("4", "24"),
    "STRIKETHROUGH": ("9", "29"),
}

STYLE_LOOKUP: dict[str, tuple[str, str]] = {
    **STYLES,
    **{name.lower(): codes for name, codes in STYLES.items()},
}
