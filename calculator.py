"""
This file contains all the calculators.
"""


def string_calculator(number_string: str) -> int:
    if not number_string:
        return 0
    DEFAULT_DELIMITER = ","
    extra_delimiters = ["\n"]
    for delim in extra_delimiters:
        number_string = number_string.replace(delim, DEFAULT_DELIMITER)
    try:
        return sum(map(lambda x: int(x), number_string.split(",")))
    except ValueError:
        raise Exception("Invalid number string")
