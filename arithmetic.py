"""Functions for common math operations."""

from functools import reduce


def add(numbers):
    """Returns the sum of all numbers"""

    numbers.pop(1)
    numbers_int = [int(number) for number in numbers]

    return reduce(lambda x, y: x+y, numbers_int)


def subtract(num1, num2):
    """Return the value of num1 minus num2."""

    return num1 - num2


def multiply(numbers):
    """Returns the product of all numbers"""

    numbers.pop(1)
    numbers_int = [int(number) for number in numbers]

    return reduce(lambda x, y: x*y, numbers_int)


def divide(num1, num2):
    """Divide the num1 by num2, returning a floating point."""

    return num1 / num2


def square(num1):
    """Return the square of num1."""

    return num1 * num1


def cube(num1):
    """Return the cube of num1."""

    return num1 * num1 * num1


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""

    return num1 ** num2  


def mod(num1, num2):
    """Return the remainder of num1 / num2."""

    return num1 % num2