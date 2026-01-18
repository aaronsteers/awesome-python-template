"""Example submodule demonstrating pdoc3 documentation behavior.

This submodule contains both public and private modules to demonstrate
how pdoc3 handles documentation generation for different visibility levels.

Public modules (without underscore prefix) are included in generated docs.
Private modules (with underscore prefix) are excluded by default.
"""

from awesome_python_template.example_submodule.public_module import (
    PublicClass,
    public_function,
)

__all__ = ["PublicClass", "public_function"]
