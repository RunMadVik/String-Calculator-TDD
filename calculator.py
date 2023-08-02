"""
This file contains all the calculators.
"""


def string_calculator(number_string: str) -> int:
    if not number_string:
        return 0
    DEFAULT_DELIMITER = ","
    extra_delimiters = ["\n"]

    stripped_string = number_string.lstrip("/")
    if stripped_string != number_string:
        # splitting on newline character since additional delimiters
        # will be given in format "//[delimiter]\n"
        values = stripped_string.split("\n")
        extra_delimiters.extend(values[0])
        number_string = "\n".join(values[1:])

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
