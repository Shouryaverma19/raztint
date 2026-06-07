from raztint.core.ansi import apply_background, apply_color, apply_style


class TestAnsiHelpers:
    def test_apply_color_disabled(self) -> None:
        assert apply_color("x", "31", use_color=False) == "x"

    def test_apply_color_enabled(self) -> None:
        assert apply_color("x", "31", use_color=True) == "\033[31mx\033[0m"

    def test_apply_background_enabled(self) -> None:
        assert apply_background("x", "44", use_color=True) == "\033[44mx\033[49m"

    def test_apply_style_enabled(self) -> None:
        assert apply_style("x", "1", "22", use_color=True) == "\033[1mx\033[22m"
