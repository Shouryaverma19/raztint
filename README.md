<div align="center">
  <img src="assets/RazTint.svg" alt="RazTint" width="400" />
  <br><br>
  
[![PyPI Version](https://img.shields.io/pypi/v/raztint)](https://pypi.org/project/raztint/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/raztint)](https://pypi.org/project/raztint/)
[![Python Versions](https://img.shields.io/pypi/pyversions/raztint)](https://pypi.org/project/raztint/)
[![License](https://img.shields.io/pypi/l/raztint)](https://github.com/razbuild/raztint/blob/master/LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-zero-brightgreen)](https://github.com/razbuild/raztint)

  <p>A zero-dependency Python library for ANSI coloring and smart CLI icons that automatically adapt to your environment.</p>
</div>

## Preview

| ASCII Icons | Nerd Font Icons | Unicode Icons |
|---|---|---|
| ![ASCII](https://raw.githubusercontent.com/razbuild/raztint/master/assets/ascii.png) | ![Nerd Font](https://raw.githubusercontent.com/razbuild/raztint/master/assets/nerdfont.png) | ![Unicode](https://raw.githubusercontent.com/razbuild/raztint/master/assets/unicode.png) |

---

## Why RazTint?

- **Zero dependencies** — Python ≥ 3.10 standard library only
- **Smart icons** — Nerd Font → Unicode → ASCII fallback, detected automatically
- **Cross-platform behavior** — Linux, macOS, and Windows, including CI
- **Minimal setup** — import and use; detection is cached and fast

---

## Features

- 🎨 Full ANSI 16-color foreground and background support
- ✨ Text styles: bold, dim, italic, underline, strikethrough
- 🔍 Status icons with three-tier fallback and environment-aware detection
- 🖌️ **`paint()`** — one call for color, background, styles, and icons
- 🎯 **Intents** — semantic presets (`success`, `danger`, `warning`, …)
- 🔒 **Redaction** — mask secrets in logs before printing
- 💡 Fully type-hinted public API (`py.typed`, IDE autocompletion)
- ⚙️ Configurable via environment variables (`NO_COLOR`, `RAZTINT_FORCE_COLOR`, …)

---

## Requirements

- Python 3.10 or newer

---

## Installation

```bash
pip install raztint
```

From source:

```bash
git clone https://github.com/razbuild/raztint.git
cd raztint
uv sync
```

---

## Quick Start

```python
from raztint import green, ok, paint

print(green("Success!"))          # green text
print(f"{ok()} File saved.")      # ✓  File saved.
print(paint("Connection failed.", color="red", icon="err"))  # ✗  Connection failed.

# Semantic intents
print(paint("Deployment complete.", intent="success"))

# Mask secrets before logging
print(paint("password=1234", intent="debug", redact=True))  # password=****
```

Standalone redaction without formatting:

```python
from raztint import redact

print(redact("password=supersecret api_key=ghp_abc123"))
# password=**** api_key=****
```

See [Getting Started](docs/getting-started.md) for more examples.

---

## Documentation

| Guide | Description |
|---|---|
| [Getting Started](docs/getting-started.md) | Functional usage, `paint()`, and the `tint` instance |
| [API Reference](docs/api-reference.md) | Colors, styles, icons, and `RazTint` class methods |
| [Intents](docs/intents.md) | Semantic presets for common CLI messages |
| [Security & Redaction](docs/security.md) | Masking tokens, credentials, and custom rules |
| [Icons & Detection](docs/icons-and-detection.md) | Icon modes and font/color detection logic |
| [Configuration](docs/configuration.md) | Environment variables and runtime toggles |
| [Development](docs/development.md) | Local setup, tests, and linting |

---

## Contributing

PRs and issues are welcome.
If you find a bug or want to add a feature, open an issue first so we can discuss it.
See [CONTRIBUTING.md](https://github.com/razbuild/.github/blob/main/CONTRIBUTING.md) for setup and guidelines.

---

## License

MIT License

<div align="center">
  <img src="https://raw.githubusercontent.com/razbuild/.github/main/profile/svg/badge.svg" alt="Made by RazBuild" width="160">
</div>