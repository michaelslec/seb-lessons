#!/bin/env python3

"""
Homework One:
    Here, you will create the proper functions so that each test passes. In
    order to run these tests, please use the command:

        python -m doctest -v recursion.py

    This command will allow you to run the tests that are written inside the
    comments of each function body.

    Example:
        sum_to_n(6) should return 21

    Please note that while the documentation declares what the input and return
    values are, I do not fill that in for you. That will be part of your
    responsibility in writing the function. Please make sure to denote types
    for the input parameters and return values of the function.

    Example:
        def my_func(n: int) -> int:
            return n + 2
"""


def sum_to_n():
    """Returns sum of arithmetic series to N.

    Args:
        n (int): Last number in arithmetic series.

    Returns:
        The Sum of all numbers 1 to N.

    >>> sum_to_n(0)
    0
    >>> sum_to_n(6)
    21
    """


def factorial():
    """Returns the factorial of the given number.

    Args:
        n (int): The number to calculate factorial for.

    Returns:
        The calculated factorial of the given number.

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(6)
    720
    """


def tail_factorial():
    """Same as factorial, but with tail recursion.

    >>> tail_factorial(0)
    1
    >>> tail_factorial(1)
    1
    >>> tail_factorial(6)
    720
    """
