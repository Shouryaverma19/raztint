# Changelog

## [0.5.0] - 2026-05-12

### Added
- feat: support for ANSI background colors [#5](https://github.com/razbuild/raztint/pull/5) by [@snoopuppy582](https://github.com/snoopuppy582)
- test: add unit tests for background color parsing

### Docs
- docs: update README with new color examples

---

## [0.4.1] - 2026-05-12

### Fixed
- `__version__` now correctly reflects the installed version using `importlib.metadata`.  
  Previously, it was hardcoded to `0.3.0`, causing confusion with the actual package version.

---

## [0.4.0] - 2026-05-11

### Added
- **Text style support**: New functions `bold`, `dim`, `italic`, `underline`, and `strikethrough` allow applying text styles without breaking existing ANSI colors. Each style uses its own reset code to preserve color when removed. Implemented by [@wangstrider](https://github.com/wangstrider) in [#3](https://github.com/razbuild/raztint/pull/3).
- Comprehensive test coverage for all new style functions.

### Docs
- Full documentation for text styles in README and API reference.

---

## [0.3.0] - 2026-05-04

### Added
- Full ANSI 16-color support: added 7 bright color variants (bright_red, bright_green, bright_yellow, bright_blue, bright_magenta, bright_cyan, bright_white).
- New singleton import (`tint`) now documented explicitly in README.

### Changed / Refactored
- Unified color method naming to snake_case for bright variants (e.g., bright_red) in line with existing naming convention.
- Updated Python support to include 3.14 and adjusted classifiers.

### Docs
- Comprehensive README overhaul: bright colors table, singleton clarification, PyPI badge fix, removed incorrect pipx instructions, improved structure.

---

## [0.2.0] - 2026-02-23

### Added
- Expanded test suite for environment and nerd font detection across platforms.
- Optional debug logging and configuration flags for font scanning behavior.

### Changed / Refactored
- Broadened supported Python versions to 3.9–3.13 and updated classifiers.
- Improved robustness and performance of color, icon, and nerd font detection.

### Docs
- Updated README with new configuration flags, performance/debugging notes, and development workflow.
- Documented release changes for 0.2.0 in the changelog.

### CI
- Updated GitHub Actions to install extras-based dependencies and test against multiple Python versions.

---

## [0.1.1] - 2025-12-20

### Added
- Modular structure for colors and icons to improve maintainability.
- New icons and improved visual representation.

### Changed / Refactored
- Refactored code for better readability and organization.
- Updated icon rendering and layout.

### Removed
- Redundant code from the main module after modularization.

### Docs
- Documentation updated to match the new structure and visuals.

### CI
- Continuous integration updated and synchronized with the latest code changes.
