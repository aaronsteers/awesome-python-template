# Contributing

Thank you for your interest in contributing!

## Quick Start

```bash
# Install uv if needed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Setup
uv sync --all-extras

# Install poe globally (optional)
uv tool install poethepoet
```

## Development Workflow

1. Make your changes
2. Run `poe fix` to auto-format and fix linting
3. Run `poe test` to ensure tests pass
4. Commit and push your changes

## Available Commands

View all available tasks:
```bash
poe --help
```

Key commands:
- `poe test` - Run tests
- `poe lint` - Check code quality
- `poe format` - Format code
- `poe fix` - Auto-format and fix issues
- `poe check` - Run all checks

## GitHub Slash Commands

On PRs, you can use:
- `/autofix` - Auto-format and commit fixes
- `/lock` - Update uv.lock file
- `/poe <task>` - Run any poe task

## Adding Dependencies

```bash
uv add package-name        # Runtime dependency
uv add --dev package-name  # Dev dependency
```

## Project Structure

```
awesome-python-template/
├── src/awesome_python_template/  # Source code
├── tests/                         # Tests
├── pyproject.toml                 # Project config
├── ruff.toml                      # Ruff config
└── pytest.ini                     # Pytest config
```
