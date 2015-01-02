"""
Often used methods for Project Euler Problems
"""


def fibonacci_limit(limit):
    a, b = 1, 2
    while a < limit:
        yield a
        a, b = b, a+b


def fibonacci_element(x):
    a, b = 1, 2
    for i in range(x):
        yield a
        a, b = b, a+b


def fibonacci_n(x):
    return round((((1 + 5**0.5) / 2)**x - (1 - ((1 + 5**0.5) / 2))**x) / 5**0.5)