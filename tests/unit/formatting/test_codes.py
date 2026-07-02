import pytest

from raztint.formatting.codes import (
    get_background_code,
    get_color_code,
    get_style_codes,
    normalize_styles,
)


class TestFormattingCodes:
    def test_get_color_code_by_name(self) -> None:
        assert get_color_code("red") == "31"

    def test_get_color_code_by_int(self) -> None:
        assert get_color_code(91) == "91"

    def test_get_color_code_none(self) -> None:
        assert get_color_code(None) is None

    def test_get_color_code_invalid_name(self) -> None:
        with pytest.raises(ValueError, match="Unknown color"):
            get_color_code("nope")

    def test_get_color_code_invalid_int(self) -> None:
        with pytest.raises(ValueError, match="Invalid ANSI foreground"):
            get_color_code(50)

    def test_get_background_code_prefixed_and_short(self) -> None:
        assert get_background_code("bg_red") == "41"
        assert get_background_code("red") == "41"

    def test_get_background_code_invalid(self) -> None:
        with pytest.raises(ValueError, match="Unknown background"):
            get_background_code("nope")

    def test_get_style_codes(self) -> None:
        assert get_style_codes("bold") == ("1", "22")

    def test_normalize_styles_list_and_string(self) -> None:
        assert normalize_styles("Bold") == ("bold",)
        assert normalize_styles(["Underline"]) == ("underline",)

    def test_normalize_styles_invalid_type(self) -> None:
        with pytest.raises(TypeError, match="styles must be"):
            normalize_styles(42)  # type: ignore[arg-type]
