from raztint.core import RazTint


def test_plain_text_skips_ansi_when_no_formatting(raztint_color_on: RazTint) -> None:
    """Hot path: no icon/color/style should return input unchanged."""
    assert raztint_color_on.format_text("hello") == "hello"
