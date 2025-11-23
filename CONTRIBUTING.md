# Contributing to Awesome Python Template

Thank you for your interest in contributing to the Awesome Python Template! This guide will help you get started with development and testing.

## Development Setup

This project uses [uv](https://docs.astral.sh/uv/) for Python package management and follows modern Python development practices.

### Prerequisites

- Python 3.10 or higher
- [uv](https://docs.astral.sh/uv/) for package management

### Installing uv

If you don't have uv installed yet:

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or with pip
pip install uv
```

### Installing Dependencies

```bash
# Clone the repository
git clone https://github.com/aaronsteers/awesome-python-template.git
cd awesome-python-template

# Install all dependencies including dev dependencies
uv sync --all-extras
```

Note: Unlike Poetry, uv will generally auto-run a sync whenever you use `uv run`. Running `uv sync` explicitly may not be strictly necessary after the first time.

### Installing Poe the Poet

For convenience, install [Poe the Poet](https://poethepoet.natn.io/) task runner globally:

```bash
# Install Poe globally with uv
uv tool install poethepoet

# Verify installation
poe --help
```

If you don't install Poe globally, you can still use it via `uv run poe` instead of just `poe`.

## Development Workflow

The typical development workflow looks like this:

1. Make your changes to the code
2. Run `poe fix` to auto-format and fix linting issues
3. Run `poe test` to ensure tests pass
4. Run `poe check` to run all quality checks
5. Commit your changes
6. Push and create a pull request

## Available Poe Tasks

You can view all available tasks by running:

```bash
poe --help
# Or if Poe is not installed globally:
uv run poe --help
```

### Core Development Tasks

```bash
# Testing
poe test              # Run all tests
poe test-fast         # Run tests with fast exit on first failure
poe test-cov          # Run tests with coverage reporting
poe test-unit         # Run unit tests only
poe test-integration  # Run integration tests only

# Code Quality
poe lint              # Check code style and quality
poe format            # Format code with ruff
poe format-check      # Check if code is properly formatted
poe deps              # Check for unused and missing dependencies

# Convenience
poe check             # Run format check, linting, dependency check, and tests
poe fix               # Auto-format and fix linting issues
poe pre-commit        # Run pre-commit style checks
```

### Build & Install Tasks

```bash
poe install           # Install with development dependencies
poe install-prod      # Install production dependencies only
poe build             # Build the package
```

### Utility Tasks

```bash
poe clean             # Clean up build artifacts and cache
poe version           # Show package version
```

## Running Tests

### Running All Tests

```bash
poe test
```

### Running Specific Test Types

Tests are organized with pytest markers:

```bash
# Run only unit tests
poe test-unit

# Run only integration tests
poe test-integration

# Run tests with coverage
poe test-cov
```

### Running Tests Directly with pytest

If you need to pass custom pytest options:

```bash
uv run pytest tests/ -v
uv run pytest tests/test_specific.py -k test_function_name
```

## Code Quality

### Formatting

This project uses [Ruff](https://docs.astral.sh/ruff/) for both linting and formatting. Ruff is configured in `ruff.toml`.

```bash
# Auto-format all code
poe format

# Check if code is properly formatted (without making changes)
poe format-check
```

### Linting

```bash
# Check for linting issues
poe lint

# Auto-fix linting issues where possible
poe fix
```

### Auto-fixing Issues

The easiest way to fix most issues automatically:

```bash
poe fix
```

This will run both formatting and auto-fixable linting checks.

## Dependency Management

### Adding Dependencies

To add a new dependency:

```bash
# Add a runtime dependency
uv add package-name

# Add a development dependency
uv add --dev package-name
```

### Updating Dependencies

```bash
# Update all dependencies
uv sync --upgrade

# Update a specific package
uv add package-name@latest
```

### Dependency Analysis

This project uses [deptry](https://deptry.com/) to detect unused and missing dependencies.

```bash
# Check for dependency issues
poe deps
```

#### Handling Deptry False Positives

Sometimes deptry may flag packages incorrectly. To ignore specific issues:

1. Identify the rule code (DEP001, DEP002, DEP003, or DEP004)
2. Update the configuration in `pyproject.toml` under `[tool.deptry]`
3. Add a comment explaining why the ignore is needed

Example scenarios requiring ignores:
- Packages imported using a different name than their PyPI package name
- Packages imported dynamically or through submodules
- Test frameworks like pytest (commonly ignored with DEP004)

## GitHub Integration

### Pull Request Automation

When you open a pull request, you'll automatically receive a welcome message with helpful information about available commands.

### Slash Commands

If you have write permissions on the repository, you can use slash commands in PR comments:

- `/autofix` - Auto-format and fix linting issues, then commit changes
- `/lock` - Update the uv.lock file and commit changes
- `/poe <task>` - Run any poe task (e.g., `/poe test`, `/poe check`)

**Security Note**: Slash commands run against the base repository code, not the PR changes. This ensures that untrusted code cannot be executed in a privileged environment.

### Continuous Integration

All pull requests automatically run:
- Format checking
- Linting
- Tests on multiple Python versions (3.10, 3.11, 3.12, 3.13)
- Dependency analysis

Make sure all checks pass before requesting review.

## Project Structure

Understanding the project structure will help you navigate the codebase:

```
awesome-python-template/
├── src/
│   └── awesome_python_template/    # Main source code
│       ├── __init__.py
│       └── py.typed                # Marks package as type-hint compliant
├── tests/                          # Test files
│   ├── __init__.py
│   └── test_awesome_python_template.py
├── .github/
│   └── workflows/                  # GitHub Actions CI/CD
├── pyproject.toml                  # Project metadata and minimal config
├── ruff.toml                       # Ruff configuration
├── pytest.ini                      # Pytest configuration
├── poe_tasks.toml                  # PoeThePoet task definitions (reference)
├── uv.lock                         # Dependency lock file
├── README.md                       # Project documentation
└── CONTRIBUTING.md                 # This file
```

## Configuration Files

This template uses dedicated configuration files for each tool:

- **`ruff.toml`** - Ruff linting and formatting configuration
- **`pytest.ini`** - Pytest testing configuration
- **`pyproject.toml`** - Project metadata and tool configuration
- **`poe_tasks.toml`** - Reference copy of task definitions

This approach keeps configuration organized and easier to maintain than cramming everything into `pyproject.toml`.

## Best Practices

When contributing to this project, please follow these conventions:

1. **Source Layout** - All source code goes in `src/awesome_python_template/`
2. **Testing** - Write tests for new features and bug fixes
3. **Type Hints** - Use modern Python 3.10+ type hints (e.g., `list[str]` not `List[str]`)
4. **Code Style** - Let Ruff handle formatting; don't fight the formatter
5. **Commits** - Write clear, descriptive commit messages
6. **Pull Requests** - Keep PRs focused on a single feature or fix

## Making Your First Contribution

Not sure where to start? Here are some ideas:

1. Look for issues labeled "good first issue"
2. Improve documentation
3. Add more tests
4. Fix typos or improve error messages
5. Suggest new features by opening an issue first

## Getting Help

If you run into issues:

1. Check the [README.md](README.md) for basic usage information
2. Review existing issues and pull requests
3. Open a new issue with a clear description of the problem
4. Include steps to reproduce, expected behavior, and actual behavior

## Code of Conduct

Please be respectful and constructive in all interactions. We're all here to learn and build something useful together.

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.
