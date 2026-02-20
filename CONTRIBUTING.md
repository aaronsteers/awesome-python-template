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

## Available Commands

View all available tasks:
```bash
poe --help
```

## 🚀 Releasing

This project uses [`semantic-pr-release-drafter`](https://github.com/aaronsteers/semantic-pr-release-drafter) for automated release management. To release, simply click "`Edit`" on the latest release draft from the [releases page](https://github.com/aaronsteers/awesome-python-template/releases), and then click "`Publish release`". This publish operation will trigger all necessary downstream publish operations.

ℹ️ For more detailed instructions, please see the [Releasing Guide](https://github.com/aaronsteers/semantic-pr-release-drafter/blob/main/docs/releasing.md).
