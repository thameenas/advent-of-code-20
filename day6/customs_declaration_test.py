from unittest import TestCase
from .customs_declaration import read_input
from .customs_declaration import find_count


class Test(TestCase):
    def test_find_count(self):
        input_data = read_input("day6/test_input.txt")
        self.assertEqual(find_count(input_data), (11, 6))
