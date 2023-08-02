"""
This file contains all the test cases for calculators.
"""

import unittest
from calculator import string_calculator


class TestStringCalculator(unittest.TestCase):
    """
    This class tests all the possible scenarios for string calculator.
    """

    def test_empty_string(self):
        self.assertEqual(string_calculator(number_string=""), 0)

    def test_single_number_string(self):
        self.assertEqual(string_calculator(number_string="1"), 1)

    def test_two_number_string(self):
        self.assertEqual(string_calculator(number_string="1,2"), 3)

    def test_multiple_number_string(self):
        self.assertEqual(string_calculator(number_string="1,2,3,4,5,6,7,8,9,10"), 55)

    def test_number_string_calculator_with_new_line_characters(self):
        self.assertEqual(string_calculator(number_string="1\n2,3"), 6)

    def test_number_string_calculator_with_different_delimiter(self):
        self.assertEqual(string_calculator(number_string="//;\n1;2"), 3)


if __name__ == "__main__":
    unittest.main()
