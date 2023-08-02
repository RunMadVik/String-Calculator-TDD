"""
This file contains all the calculators.
"""


def string_calculator(number_string: str) -> int:
    if not number_string:
        return 0

    return sum(map(lambda x: int(x), number_string.split(",")))
