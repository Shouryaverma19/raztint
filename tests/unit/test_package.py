import raztint


def test_public_exports() -> None:
    for name in (
        "RazTint",
        "tint",
        "paint",
        "redact",
        "MaskRule",
        "INTENTS",
        "__version__",
    ):
        assert hasattr(raztint, name)


def test_version_is_string() -> None:
    assert isinstance(raztint.__version__, str)
    assert raztint.__version__
