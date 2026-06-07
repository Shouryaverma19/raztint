"""Smoke checks that typing metadata is shipped for IDEs."""

from pathlib import Path


def test_py_typed_marker_exists() -> None:
    marker = Path(__file__).resolve().parents[2] / "src" / "raztint" / "py.typed"
    assert marker.is_file()


def test_stub_files_exist() -> None:
    pkg = Path(__file__).resolve().parents[2] / "src" / "raztint"
    assert (pkg / "__init__.pyi").is_file()
    assert (pkg / "core" / "instance.pyi").is_file()
