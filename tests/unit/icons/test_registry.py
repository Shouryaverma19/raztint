from raztint.icons.registry import ICONS


def test_icons_registry_has_status_keys() -> None:
    assert set(ICONS) == {"OK", "ERR", "WARN", "INFO", "PENDING", "DEBUG"}


def test_each_icon_has_three_tiers() -> None:
    for data in ICONS.values():
        assert {"nerd", "std", "ascii", "color"} <= set(data)
