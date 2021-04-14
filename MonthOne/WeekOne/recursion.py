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
    pass


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
    pass

def ways_across_river():
    """Returns the number of ways across a river by 1 or 2 steps.

    Problem: There is a frog that wants to cross the river. The frog may either
    jump one OR two spots at a time. Given the length of the river, calculate
    the number of different ways the frog could cross the river.

    >>> ways_across_river(0)
    1
    >>> ways_across_river(1)
    1
    >>> ways_across_river(2)
    2
    >>>ways_across_river(4)
    5
    """
    pass
