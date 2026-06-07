# Getting Started

[← Documentation index](index.md)

You can use RazTint in three ways: import helpers directly, call `paint()` for combined formatting, or create a `RazTint` instance for scoped control.

---

## Functional usage

The simplest approach — import pre-bound helpers from the module:

```python
from raztint import bg_blue, green, red, ok, err, info, warn, bold, underline

# Colors
print(green("Success! The operation completed."))
print(red("Critical Error: Database not found."))

# Styles
print(bold("This is bold text."))
print(underline(red("Underlined red text.")))
print(red(bg_blue("Red text on a blue background.")))

# Icons (auto-adapts to Nerd Font / Unicode / ASCII)
print(f"{ok()} File saved successfully.")
print(f"{err()} Connection failed.")
print(f"{info()} Analysis in progress...")
print(f"{warn()} Disk space low.")
```

---

## Using `paint()`

`paint()` combines color, background, styles, and an icon in a single call. It is an alias for `tint.format_text()`.

```python
from raztint import paint

# Color + style
print(paint("Done!", color="green", styles="bold"))

# Color + background + multiple styles
print(paint("Alert", color="white", bg="red", styles=["bold", "underline"]))

# With icon (uses environment-detected mode)
print(paint("File saved.", color="green", styles="bold", icon="ok"))
print(paint("Connection failed.", color="red", icon="err"))

# Override icon mode explicitly
print(paint("Done!", color="green", icon="ok", icon_mode="nerd"))
print(paint("Done!", color="green", icon="ok", icon_mode="std"))
print(paint("Done!", color="green", icon="ok", icon_mode="ascii"))
print(paint("Done!", color="green", icon="ok", icon_mode="auto"))
```

### Nested calls vs. `paint()`

```python
# Nested helpers
from raztint import red, bold, underline
print(bold(underline(red("Important message"))))

# Equivalent with paint()
from raztint import paint
print(paint("Important message", color="red", styles=["bold", "underline"]))
print(paint("Important message", color="red", styles=["bold", "underline"], icon="err"))
```

### Concatenation with `reset=False`

When chaining styled segments, disable the trailing reset on intermediate parts:

```python
from raztint import paint

part1 = paint("WARNING:", color="yellow", reset=False)
part2 = paint(" Disk full", color="red")
print(part1 + part2)
```

---

## The `tint` singleton

`tint` is a pre-instantiated `RazTint` for convenience:

```python
from raztint import tint

print(tint.red("text"))
print(tint.ok(), "hello")
print(tint.format_text("Done!", color="green", icon="ok"))
```

Inspect runtime state:

```python
print(tint.use_color)   # True if ANSI output is enabled
print(tint.icon_mode)   # "nerd", "std", or "ascii"
```

---

## Class-based usage

Create your own instance when you need isolated or dynamic settings:

```python
from raztint import RazTint

t = RazTint()
t.set_color(False)
print(t.blue("Plain text — color disabled for this instance."))
```

Each instance carries its own `use_color` and `icon_mode` state.

---

## Intents

Apply semantic presets with a single parameter. See [Intents](intents.md) for the full registry.

```python
from raztint import paint

print(paint("Saved.", intent="success"))
print(paint("Invalid input.", intent="danger"))
print(paint("Waiting for worker...", intent="pending"))
```

Explicit `color`, `icon`, or `styles` arguments override the intent defaults.

---

## Redaction

Mask secrets before they reach the terminal. See [Security & Redaction](security.md).

```python
from raztint import paint, redact

# Standalone
safe = redact("password=supersecret")

# Combined with formatting
print(paint(f"Config: {raw}", intent="debug", redact=True))
```

---

## Next steps

- [API Reference](api-reference.md) — full parameter lists and helper tables
- [Configuration](configuration.md) — environment variables for CI and overrides
- [Icons & Detection](icons-and-detection.md) — how icon modes are chosen
