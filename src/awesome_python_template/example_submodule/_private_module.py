"""Private module demonstrating pdoc3 documentation behavior.

This module is private (underscore prefix) and will be excluded
from the generated documentation by pdoc3 by default.

Private modules are useful for internal implementation details
that should not be part of the public API documentation.
"""


class _PrivateClass:
    """A private class that is excluded from generated documentation.

    This class demonstrates how pdoc3 handles private classes.
    By default, classes with underscore prefixes are not documented.
    """

    def __init__(self, secret: str) -> None:
        """Initialize a _PrivateClass instance.

        Args:
            secret: A secret value for internal use.
        """
        self._secret = secret

    def _internal_method(self) -> str:
        """An internal method for private operations.

        Returns:
            The secret value.
        """
        return self._secret


def _private_helper(data: str) -> str:
    """A private helper function excluded from documentation.

    This function demonstrates how pdoc3 handles private functions.
    Functions with underscore prefixes are not included in docs by default.

    Args:
        data: Input data to process.

    Returns:
        The processed data (uppercased).
    """
    return data.upper()
