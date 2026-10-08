"""A simple calculator supporting basic arithmetic operations."""


def _validate_numbers(*values):
    """Raise TypeError if any value is not an int or float."""
    for value in values:
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"Argument must be a number (int or float), got {type(value).__name__}"
            )


def add(a, b):
    """Return the sum of two numbers.

    Args:
        a: The first number (int or float).
        b: The second number (int or float).

    Returns:
        The sum ``a + b``. An int if both arguments are ints, otherwise a float.

    Raises:
        TypeError: If either argument is not an int or float.
    """
    _validate_numbers(a, b)
    return a + b
