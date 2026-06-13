ICONS: dict[str, dict[str, str]] = {
    "OK": {"nerd": "[󰄬]", "std": "[✓]", "ascii": "[OK]", "color": "GREEN"},
    "ERR": {"nerd": "[󰅖]", "std": "[✗]", "ascii": "[ERR]", "color": "RED"},
    "WARN": {"nerd": "[]", "std": "[!]", "ascii": "[WARN]", "color": "YELLOW"},
    "INFO": {"nerd": "[]", "std": "[i]", "ascii": "[INFO]", "color": "BLUE"},
    "PENDING": {
        "nerd": "[󱦟]",
        "std": "[PENDING]",
        "ascii": "[PENDING]",
        "color": "CYAN",
    },
    "DEBUG": {"nerd": "[󰃤]", "std": "[DEBUG]", "ascii": "[DEBUG]", "color": "WHITE"},
}
