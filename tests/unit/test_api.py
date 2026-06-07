from raztint import err, ok, paint, tint, warn


def test_module_level_icons_distinct() -> None:
    tint.icon_mode = "std"
    tint.set_color(False)
    try:
        assert ok() != err()
        assert warn() != ok()
    finally:
        pass


def test_paint_matches_format_text() -> None:
    original = tint.use_color
    tint.set_color(True)
    try:
        assert paint("x", color="red") == tint.format_text("x", color="red")
    finally:
        tint.set_color(original)
