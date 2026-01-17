"""Public module demonstrating pdoc3 documentation.

This module is public (no underscore prefix) and will be included
in the generated documentation by pdoc3.
"""


class PublicClass:
    """A public class that appears in generated documentation.

    This class demonstrates how pdoc3 documents public classes,
    including their methods and attributes.

    Attributes:
        name: The name of the instance.
        value: An optional value associated with the instance.
    """

    def __init__(self, name: str, value: int = 0) -> None:
        """Initialize a PublicClass instance.

        Args:
            name: The name for this instance.
            value: An optional integer value. Defaults to 0.
        """
        self.name = name
        self.value = value

    def greet(self) -> str:
        """Return a greeting message.

        Returns:
            A greeting string including the instance name.
        """
        return f"Hello from {self.name}!"

    def increment(self, amount: int = 1) -> int:
        """Increment the value by the given amount.

        Args:
            amount: The amount to increment by. Defaults to 1.

        Returns:
            The new value after incrementing.
        """
        self.value += amount
        return self.value


def public_function(x: int, y: int) -> int:
    """A public function that appears in generated documentation.

    This function demonstrates how pdoc3 documents public functions,
    including their parameters and return values.

    Args:
        x: The first integer operand.
        y: The second integer operand.

    Returns:
        The sum of x and y.
    """
    return x + y
