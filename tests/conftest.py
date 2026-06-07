import pytest

from raztint.core import RazTint
from raztint.detect.env import clear_env_cache
from raztint.detect.fonts import check_installed_nerd_fonts, has_nerd_fonts


@pytest.fixture
def raztint() -> RazTint:
    """Fresh RazTint instance for isolated tests."""
    return RazTint()


@pytest.fixture
def raztint_color_on(raztint: RazTint) -> RazTint:
    raztint.set_color(True)
    return raztint


@pytest.fixture
def raztint_color_off(raztint: RazTint) -> RazTint:
    raztint.set_color(False)
    return raztint


@pytest.fixture(autouse=True)
def _clear_detection_caches() -> None:
    clear_env_cache()
    has_nerd_fonts.cache_clear()
    check_installed_nerd_fonts.cache_clear()
    yield
    clear_env_cache()
    has_nerd_fonts.cache_clear()
    check_installed_nerd_fonts.cache_clear()
