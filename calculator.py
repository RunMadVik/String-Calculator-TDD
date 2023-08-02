"""
This file contains all the calculators.
"""
import re


def string_calculator(number_string: str) -> int:
    """
    This function takes a string with numbers and delimiters
    and returns the sum of all the numbers in the string
    """
    if not number_string:
        return 0

    DEFAULT_DELIMITER = ","
    extra_delimiters = ["\n"]

    stripped_string = number_string.lstrip("/")
    if stripped_string != number_string:
        # splitting on newline character since any additional delimiters
        # will be given in format "//[delimiter1][delimiter2]\n"
        values = stripped_string.split("\n")
        delims = re.findall(r"\[(.*?)\]", values[0])
        extra_delimiters.extend(delims)
        number_string = "\n".join(values[1:])

    # replacing every extra delimiter with the default delimiter
    for delim in extra_delimiters:
        number_string = number_string.replace(delim, DEFAULT_DELIMITER)

    try:
        numbers_list = list(map(lambda x: int(x), number_string.split(",")))
    except ValueError:
        raise Exception("Invalid number string")

    negative_numbers = [number for number in numbers_list if number < 0]
    if negative_numbers:
        raise Exception(f"Negative numbers not allowed. {negative_numbers}")

    return sum([number for number in numbers_list if number < 1000])
