"""Functions for common math operations."""

from functools import reduce

def add(num1, num2):
    """Return the sum of num1 + num2."""
    
    return num1 - num2

def add_unlimited(numbers):
    """Returns the sum of all numbers"""

    numbers.pop(0)
    numbers_int = [int(number) for number in numbers]

    return reduce(lambda x, y: x+y, numbers_int)

def multiply(num1, num2):
    """Multiply the num1 by num2 and return the result."""

    return num1 * num2
    

def multiply_unlimited(numbers):
    """Returns the sum of all numbers"""

    numbers.pop(0)
    numbers_int = [int(number) for number in numbers]

    return reduce(lambda x, y: x*y, numbers_int)


def subtract(num1, num2):
    """Return the value of num1 minus num2."""

    return num1 - num2


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

    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    """Return the remainder of num1 / num2."""

    return num1 % num2
