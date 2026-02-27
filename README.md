![Logo](https://raw.githubusercontent.com/razbuild/raztint/master/assets/logo.png)

![GitHub License](https://img.shields.io/github/license/razbuild/raztint?logoColor=ffffff&logoSize=auto&label=License&labelColor=1b1b1b&color=ab0000&cacheSeconds=3600)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/razbuild/raztint/ci.yml?branch=master&event=push&logo=githubactions&logoColor=ffffff&logoSize=auto&label=Build&labelColor=1b1b1b&color=ffc500&cacheSeconds=3600)
![Codecov](https://img.shields.io/codecov/c/github/razbuild/raztint?logo=codecov&logoColor=ffffff&logoSize=auto&label=Coverage&labelColor=1b1b1b&color=0d55cd&cacheSeconds=3600)
![PyPI - Version](https://img.shields.io/pypi/v/raztint?pypiBaseUrl=https%3A%2F%2Fpypi.org&logo=pypi&logoColor=ffffff&logoSize=auto&label=PyPi&labelColor=1b1b1b&color=ab0000&cacheSeconds=3600)
![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Frazbuild%2Fraztint%2Fmaster%2Fpyproject.toml&logo=python&logoColor=ffffff&logoSize=auto&label=Python&labelColor=1b1b1b&color=ffc500&cacheSeconds=3600)

A zero-dependency Python library for ANSI coloring and smart CLI icons that automatically adapt to your environment.

---

## Table of Contents
- [Preview](#preview)
- [What is RazTint?](#what-is-raztint)
- [Why RazTint?](#why-raztint)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [API Reference](#api-reference)
- [Icons & Detection](#icons--detection)
- [Performance & Debugging](#performance--debugging)
- [Development](#development)
- [Support](#support)
- [License](#license)

---
## Preview

| ASCII Icons                                                                          | Nerd Font Icons                                                                             | Unicode Icons                                                                            |
|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| ![ASCII](https://raw.githubusercontent.com/razbuild/raztint/master/assets/ascii.png) | ![Nerd Font](https://raw.githubusercontent.com/razbuild/raztint/master/assets/nerdfont.png) | ![Unicode](https://raw.githubusercontent.com/razbuild/raztint/master/assets/unicode.png) |

---

## What is RazTint?
RazTint is a zero-dependency Python library for colored terminal output and smart CLI icons that automatically adapt to your environment.

---

## Why RazTint?

If you need a lightweight alternative to colorama or rich for simple CLI tools, RazTint focuses on:

- Zero dependencies
- Automatic icon fallback (Nerd → Unicode → ASCII)
- Automatic color detection
- Cross-platform behavior
- Minimal runtime overhead

---

## Features

- Zero dependencies (standard library only)
- Smart icon fallback (Nerd → Unicode → ASCII)
- Automatic color detection
- Windows VT support
- Fully typed API
- Environment-based configuration

---

## Requirements

- Python 3.9 or newer

---

## Installation

### From PyPI

```bash
pip install raztint
```

### With pipx

```bash
pipx install raztint
```

### From source

```bash
git clone https://github.com/razbuild/raztint.git
cd raztint

pip install -e .  # -e allows you to modify the source code in place
```

---

## Quick Start

You can import functions directly for quick usage, or instantiate the class for more control.

### Functional Usage

The easiest way to use RazTint is importing the pre-instantiated helpers:

```python
from raztint import green, red, ok, err, info, warn

# Coloring text
print(green("Success! The operation completed."))
print(red("Critical Error: Database not found."))

# Using Icons (Auto-adapts to Nerd Font/Unicode/ASCII)
print(f"{ok()} File saved successfully.")
print(f"{err()} Connection failed.")
print(f"{info()} Analysis in progress...")
print(f"{warn()} Disk space low.")
```

### Using the `tint` Instance

```python
from raztint import tint

print(tint.red("text"))
print(tint.ok(), "hello")
```

### Class-based Usage

Useful if you need to toggle color support dynamically within an application instance or want a scoped instance.

```python
from raztint import RazTint

tint = RazTint()

# Toggle features manually if needed
tint.set_color(False) 

print(tint.blue("This will be plain text now because color is disabled."))
```

---
## Icons & Detection

### Icon Functions

```python
from raztint import ok, err, warn, info

print(ok(), "Operation completed")
print(err(), "An error happened")
print(warn(), "Be careful")
print(info(), "For your information")
```

### Icon Modes
RazTint attempts to make your CLI look as good as possible by detecting the font capabilities of the terminal.

| Mode  | ok   | err   | warn   | info   | Condition                           |
|-------|------|-------|--------|--------|-------------------------------------|
| Nerd  | [󰄬] | [󰅖]  | [󰈅]   | [󰙎]   | Detected Nerd Font via Env/Registry |
| Std   | [✓]  | [✗]   | [!]    | [i]    | UTF-8 supported, no Nerd Font       |
| ASCII | [OK] | [ERR] | [WARN] | [INFO] | Fallback                            |

> Note: Icons may not render correctly in GitHub preview depending on your browser font.

### Detection Logic

RazTint determines the best available icon and color mode using the following rules:

1. Nerd Font Mode:
   - Enabled if:
     - `RAZTINT_USE_NERD_ICONS` environment variable is set to `1`, `true`, `yes`, or `on`, OR
     - `NERDFONTS` or `NERD_FONTS` environment variable is set, OR
     - `FONT_NAME` or `TERM_FONT` environment variable contains "nerd" or "nf-", OR
     - A Nerd Font is detected via system checks:
       - **Linux**: Uses `fc-list` (fontconfig) to check installed fonts
       - **macOS**: Checks via `system_profiler` and font directories (`~/Library/Fonts`, `/Library/Fonts`)
       - **Windows**: Checks `C:\Windows\Fonts` directory via PowerShell

2. Standard Unicode Mode:
   - Enabled when UTF-8 encoding is available AND
   - `RAZTINT_NO_NERD_ICONS` is set (explicitly disables Nerd Fonts), OR
   - Nerd Fonts are not detected and not forced via `RAZTINT_USE_NERD_ICONS`

3. ASCII Mode:
   - Used when:
     - Output encoding is not UTF-8 (cannot encode Nerd Font or Unicode characters), OR
     - System encoding test fails for Unicode characters

### How to install Nerd Font?

To install Nerd Fonts, visit the official [website](https://www.nerdfonts.com/font-downloads).

---

## Configuration

You can control **RazTint** behavior using environment variables. This is useful for CI/CD pipelines or user overrides.

| Environment Variable             | Value                    | Description                                                                 |
|----------------------------------|--------------------------|-----------------------------------------------------------------------------|
| `NO_COLOR`                       | any                      | Disables all color output (standard specification).                         |
| `RAZTINT_NO_COLOR`               | any                      | Specific override to disable RazTint colors.                                |
| `RAZTINT_FORCE_COLOR`            | `1`, `true`, `yes`, `on` | Forces color output even if not a TTY.                                      |
| `RAZTINT_USE_NERD_ICONS`         | `1`, `true`, `yes`, `on` | Forces the use of Nerd Font icons.                                          |
| `RAZTINT_NO_NERD_ICONS`          | `1`, `true`, `yes`, `on` | Disables Nerd Font detection (falls back to Standard Unicode mode).         |
| `RAZTINT_SKIP_SYSTEM_FONT_SCAN`  | `1`, `true`, `yes`, `on` | Skips OS-level font scanning; only environment-based nerd font hints used.  |
| `RAZTINT_DEBUG`                  | `1`, `true`, `yes`, `on` | Enables debug logging about color/icon/font detection decisions to stderr.  |


### Programmatically:
```python
from raztint import tint
tint.set_color(False)
```

### Disable Colors

```
NO_COLOR=1
```

## Icon Behavior Configuration

### Always Use Nerd Icons

```
RAZTINT_USE_NERD_ICONS=1
```

### Force-enable Colors

```
RAZTINT_FORCE_COLOR=1
```

### Disable Nerd Icons

```
RAZTINT_NO_NERD_ICONS=1
```

---

## API Reference

### Color Functions

The following functions return strings wrapped with ANSI styling when supported:

- `black(text)`

- `red(text)`

- `green(text)`

- `yellow(text)`

- `blue(text)`

- `magenta(text)`

- `cyan(text)`

- `white(text)`

- `gray(text)`

Internally, these use `tint.color()`.

---

## Icon Functions

These return appropriate status symbols based on environment detection:

- `ok()` - Returns a success icon (green checkmark)

- `err()` - Returns an error icon (red cross)

- `warn()` - Returns a warning icon (yellow exclamation)

- `info()` - Returns an info icon (blue 'i')

RazTint selects the best available style in this order:
1. Nerd Font icons (if installed)
2. Unicode icons (if UTF-8 is supported)
3. ASCII fallback

---

## RazTint Class Methods

When using the `RazTint` class directly, you have access to additional methods:

### `color(text: str, fg_code: str) -> str`

Low-level method to apply ANSI color codes to text. Returns the text with ANSI escape sequences when color is enabled, otherwise returns plain text.

**Parameters:**
- `text`: The text to colorize
- `fg_code`: ANSI color code (e.g., "31" for red, "32" for green)

**Example:**
```python
from raztint import RazTint

tint = RazTint()
colored = tint.color("Hello", "31")  # Red text
```

### `set_color(enabled: bool) -> None`

Enable or disable color output programmatically.

**Parameters:**
- `enabled`: `True` to enable colors, `False` to disable

**Example:**
```python
from raztint import RazTint

tint = RazTint()
tint.set_color(False)  # Disable colors
print(tint.red("This will be plain text"))
```

## RazTint Class Attributes

### `use_color: bool`

Boolean indicating whether color output is currently enabled. This is automatically set based on environment detection but can be modified via `set_color()`.

### `icon_mode: str`

Current icon mode being used. Possible values:
- `"nerd"` - Nerd Font icons
- `"std"` - Standard Unicode icons
- `"ascii"` - ASCII fallback icons

---

## Color Detection

Color support is determined by checking (in order):
1. `NO_COLOR` or `RAZTINT_NO_COLOR` environment variables (disables colors)
2. `RAZTINT_FORCE_COLOR` environment variable (forces colors)
3. Whether output is connected to a TTY (`sys.stdout.isatty()`)
4. On Windows: Attempts to enable Virtual Terminal processing
5. `TERM` environment variable (must not be "dumb")

If color is not supported, all color functions return plain text.

---

## Performance & Debugging

In most environments, RazTint's detection overhead is negligible thanks to internal caching. However, in restricted or slow environments you can:

- Disable OS-level font scanning while still allowing env-based nerd font hints:

  ```bash
  RAZTINT_SKIP_SYSTEM_FONT_SCAN=1
  ```

- Inspect why a particular mode was chosen (color on/off, icon mode, font detection) by enabling debug logs:

  ```bash
  RAZTINT_DEBUG=1
  ```

Debug messages are printed to standard error and are disabled by default.

---

## Development

If you want to work on RazTint locally:

1. Clone the repository and install in editable mode with development tools:

   ```bash
   git clone https://github.com/razbuild/raztint.git
   cd raztint
   pip install -e .[dev]
   ```

2. Run the test suite:

   ```bash
   python -m pytest
   ```

3. Run formatting, linting, and type checking (kept in sync with CI):

   ```bash
   black src tests
   ruff check src tests
   ty check src tests
   ```

---

## Support

- 🐛 **Found a bug?** [Open an issue](https://github.com/razbuild/raztint/issues)
- 💡 **Have a suggestion?** [Open an issue](https://github.com/razbuild/raztint/issues)
- 📧 **Questions?** Check the [Documentation](https://github.com/razbuild/raztint/blob/master/docs/)

---

## License

MIT License

