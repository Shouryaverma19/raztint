import os
from unittest import mock

from raztint.detect.debug import debug


def test_debug_prints_when_env_set(capsys) -> None:
    with mock.patch.dict(os.environ, {"RAZTINT_DEBUG": "1"}, clear=True):
        debug("hello")
    captured = capsys.readouterr()
    assert "[raztint] hello" in captured.err


def test_debug_silent_by_default(capsys) -> None:
    with mock.patch.dict(os.environ, {}, clear=True):
        debug("hello")
    captured = capsys.readouterr()
    assert captured.err == ""
