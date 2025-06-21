# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial release of FaviconX
- Command-line interface for favicon generation
- Support for all standard favicon sizes (16x16 to 1024x1024)
- ICO, SVG, and PNG format generation
- Apple Touch Icons and Android Chrome Icons
- HTML and Web App Manifest generation
- SVG input support with CairoSVG
- Colorized terminal output
- Filtering options (Required, Recommended, Optional, Legacy)
- Custom filename prefix support
- Comprehensive test suite

### Features
- Generate 22 different favicon sizes
- Automatic HTML meta tag generation
- Web App Manifest for PWA support
- High-quality image resizing with LANCZOS algorithm
- Support for various input formats (PNG, JPG, SVG, etc.)
- Cross-platform compatibility
- Professional CLI with help and verbose options

### Technical
- Python 3.7+ compatibility
- Modern packaging with pyproject.toml
- Comprehensive test coverage
- GitHub Actions CI/CD
- MIT License 