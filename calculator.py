"""
Simple Calculator Module

A basic calculator implementation for testing CI/CD pipelines.
All functions are pure and have no side effects.
"""


def add(a: float, b: float) -> float:
    """
    Add two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b

    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Subtract b from a.

    Args:
        a: First number
        b: Second number

    Returns:
        Difference (a - b)

    Examples:
        >>> subtract(5, 3)
        2
        >>> subtract(10, 15)
        -5
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        Product of a and b

    Examples:
        >>> multiply(4, 5)
        20
        >>> multiply(-3, 7)
        -21
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Divide a by b.

    Args:
        a: Numerator
        b: Denominator

    Returns:
        Quotient (a / b)

    Raises:
        ValueError: If b is zero

    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 2)
        3.5
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
