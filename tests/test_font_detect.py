import os
from unittest import mock

from raztint.font_detect import (
    check_installed_nerd_fonts,
    has_nerd_fonts,
)


class TestHasNerdFonts:
    def setup_method(self) -> None:
        has_nerd_fonts.cache_clear()
        check_installed_nerd_fonts.cache_clear()

    def teardown_method(self) -> None:
        has_nerd_fonts.cache_clear()
        check_installed_nerd_fonts.cache_clear()

    def test_env_variable_enables_nerd_fonts(self) -> None:
        with mock.patch.dict(os.environ, {"NERDFONTS": "1"}, clear=True):
            assert has_nerd_fonts() is True

    def test_font_name_indicator(self) -> None:
        with mock.patch.dict(os.environ, {"FONT_NAME": "Hack Nerd Font"}, clear=True):
            assert has_nerd_fonts() is True

    def test_term_font_indicator(self) -> None:
        with mock.patch.dict(os.environ, {"TERM_FONT": "JetBrains Mono Nerd"}, clear=True):
            assert has_nerd_fonts() is True

    def test_skip_system_font_scan_env(self) -> None:
        with mock.patch.dict(
            os.environ, {"RAZTINT_SKIP_SYSTEM_FONT_SCAN": "1"}, clear=True
        ):
            with mock.patch(
                "raztint.font_detect.check_installed_nerd_fonts",
                side_effect=AssertionError("should not be called"),
            ):
                assert has_nerd_fonts() is False


class TestCheckInstalledNerdFonts:
    def setup_method(self) -> None:
        check_installed_nerd_fonts.cache_clear()

    def teardown_method(self) -> None:
        check_installed_nerd_fonts.cache_clear()

    @mock.patch("raztint.font_detect.os.name", "nt")
    def test_windows_detection_uses_powershell(self) -> None:
        with mock.patch("raztint.font_detect.subprocess.run") as run:
            run.return_value.returncode = 0
            run.return_value.stdout = "Some Nerd Font"
            assert check_installed_nerd_fonts() is True
            assert run.call_args is not None

    @mock.patch("raztint.font_detect.sys.platform", "darwin")
    def test_macos_detection_uses_system_profiler(self) -> None:
        with mock.patch("raztint.font_detect.subprocess.run") as run:
            run.return_value.returncode = 0
            run.return_value.stdout = "Some nerd Font"
            assert check_installed_nerd_fonts() is True
            assert run.call_args is not None

    @mock.patch("raztint.font_detect.sys.platform", "linux")
    def test_posix_detection_uses_fc_list(self) -> None:
        with mock.patch("raztint.font_detect.subprocess.run") as run:
            run.return_value.returncode = 0
            run.return_value.stdout = "Hack Nerd Font"
            assert check_installed_nerd_fonts() is True
            assert run.call_args is not None

