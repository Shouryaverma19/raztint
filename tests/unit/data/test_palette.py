from raztint.data import BACKGROUND_COLORS, COLORS, STYLES


def test_foreground_palette_size() -> None:
    assert len(COLORS) == 16


def test_background_palette_size() -> None:
    assert len(BACKGROUND_COLORS) == 16


def test_styles_have_on_off_pairs() -> None:
    for on, off in STYLES.values():
        assert on.isdigit()
        assert off.isdigit()
