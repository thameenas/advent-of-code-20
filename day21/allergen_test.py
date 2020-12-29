from unittest import TestCase

from .allergen import *


class Test(TestCase):
    def test_find_allergen(self):
        input_lines = read_input("day21/test_input.txt")
        safe_count, dangerous_ingredient = find_allergen(input_lines)
        self.assertEqual(safe_count, 5)
        self.assertEqual(dangerous_ingredient, {'mxmxvkd', 'sqjhc', 'fvjkl'})
