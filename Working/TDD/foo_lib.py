from math import *


def foo1(num):
    try:
        return sqrt(num)

    except ValueError:
        raise ValueError("Cannot square root a negative number.")
