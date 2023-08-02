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


if __name__ == "__main__":
    unittest.main()
