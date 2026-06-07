# Configuration

[← Documentation index](index.md)

Control RazTint behavior with environment variables. Useful for CI/CD pipelines, user overrides, and troubleshooting.

---

## Environment variables

| Variable | Value | Description |
|---|---|---|
| `NO_COLOR` | any | Disables all color output ([standard spec](https://no-color.org/)). |
| `RAZTINT_NO_COLOR` | any | RazTint-specific override to disable colors. |
| `RAZTINT_FORCE_COLOR` | `1`, `true`, `yes`, `on` | Forces color output even if not a TTY. |
| `RAZTINT_USE_NERD_ICONS` | `1`, `true`, `yes`, `on` | Forces Nerd Font icons. |
| `RAZTINT_NO_NERD_ICONS` | `1`, `true`, `yes`, `on` | Disables Nerd Font detection (falls back to Unicode). |
| `RAZTINT_SKIP_SYSTEM_FONT_SCAN` | `1`, `true`, `yes`, `on` | Skips OS font scanning; env-based hints only. |
| `RAZTINT_DEBUG` | `1`, `true`, `yes`, `on` | Logs color/icon/font decisions to stderr. |

Additional hints recognized during font detection (not RazTint-prefixed):

| Variable | Effect |
|---|---|
| `NERDFONTS`, `NERD_FONTS` | Treat as Nerd Font available |
| `FONT_NAME`, `TERM_FONT` | If value contains `nerd` or `nf-`, enable Nerd mode |

---

## Common scenarios

### CI / piped output

Colors are off by default when stdout is not a TTY. Force them when needed:

```bash
RAZTINT_FORCE_COLOR=1 pytest --tb=short
```

### Disable colors entirely

```bash
NO_COLOR=1 python app.py
# or
RAZTINT_NO_COLOR=1 python app.py
```

### Force ASCII icons in restricted environments

If encoding cannot represent Unicode, RazTint falls back automatically. To force Unicode without Nerd Fonts:

```bash
RAZTINT_NO_NERD_ICONS=1 python app.py
```

### Faster startup (skip font scan)

```bash
RAZTINT_SKIP_SYSTEM_FONT_SCAN=1 python app.py
```

Nerd mode still activates if `RAZTINT_USE_NERD_ICONS` or other env hints are set.

### Debug detection decisions

```bash
RAZTINT_DEBUG=1 python app.py
```

Messages go to stderr and are disabled by default.

---

## Programmatic control

```python
from raztint import RazTint, tint

# Module singleton
tint.set_color(False)
print(tint.use_color)   # False
print(tint.icon_mode)   # "nerd", "std", or "ascii"

# Scoped instance
local = RazTint()
local.set_color(True)
```

`use_color` and `icon_mode` are read/write on the instance. Changing `icon_mode` affects subsequent icon calls that do not pass an explicit `icon_mode`.

---

## Performance

Detection results are cached (`lru_cache` for encoding probes, module-level font scan). Overhead is negligible in normal use. Use `RAZTINT_SKIP_SYSTEM_FONT_SCAN=1` in slow or sandboxed environments where OS font enumeration is expensive.

---

## See also

- [Icons & Detection](icons-and-detection.md)
- [Development](development.md)
