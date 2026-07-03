import pytest

from raztint.detect.debug import _debug_enabled as _debug_enabled
from raztint.detect.debug import clear_debug_cache, debug


@pytest.fixture(autouse=True)
def _reset_cache():
    """Ensure the cached RAZTINT_DEBUG check never leaks between tests."""
    clear_debug_cache()
    yield
    clear_debug_cache()


def test_debug_silent_when_env_var_unset(monkeypatch, capsys):
    monkeypatch.delenv("RAZTINT_DEBUG", raising=False)
    debug("hello")
    captured = capsys.readouterr()
    assert captured.err == ""
    assert captured.out == ""


def test_debug_silent_when_env_var_empty(monkeypatch, capsys):
    monkeypatch.setenv("RAZTINT_DEBUG", "")
    debug("hello")
    captured = capsys.readouterr()
    assert captured.err == ""


def test_debug_prints_when_enabled(monkeypatch, capsys):
    monkeypatch.setenv("RAZTINT_DEBUG", "1")
    debug("hello world")
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == "[raztint] hello world\n"


def test_debug_accepts_any_truthy_value(monkeypatch, capsys):
    monkeypatch.setenv("RAZTINT_DEBUG", "nope")
    debug("still prints")
    captured = capsys.readouterr()
    assert captured.err == "[raztint] still prints\n"


def test_debug_supports_lazy_callable_message(monkeypatch, capsys):
    monkeypatch.setenv("RAZTINT_DEBUG", "1")
    debug(lambda: "computed " + "lazily")
    captured = capsys.readouterr()
    assert captured.err == "[raztint] computed lazily\n"


def test_lazy_callable_not_invoked_when_debug_disabled(monkeypatch, capsys):
    monkeypatch.delenv("RAZTINT_DEBUG", raising=False)
    calls = []

    def expensive():
        calls.append(1)
        return "should not run"

    debug(expensive)
    assert calls == []
    captured = capsys.readouterr()
    assert captured.err == ""


def test_enabled_check_is_cached(monkeypatch, capsys):
    """_debug_enabled() is cached; toggling env mid-run requires clear_debug_cache()."""
    monkeypatch.delenv("RAZTINT_DEBUG", raising=False)
    debug("first")
    assert capsys.readouterr().err == ""

    monkeypatch.setenv("RAZTINT_DEBUG", "1")
    debug("second")
    assert capsys.readouterr().err == ""

    clear_debug_cache()
    debug("third")
    assert capsys.readouterr().err == "[raztint] third\n"


def test_clear_debug_cache_resets_cache_info(monkeypatch):
    monkeypatch.setenv("RAZTINT_DEBUG", "1")
    _debug_enabled()
    assert _debug_enabled.cache_info().currsize == 1
    clear_debug_cache()
    assert _debug_enabled.cache_info().currsize == 0
