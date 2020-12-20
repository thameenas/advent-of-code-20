from unittest import TestCase
from .direction_coordinates import *


class Test(TestCase):
    def test_read_input(self):
        input_data = read_input("day12/test_input.txt")
        self.assertEqual(part1(input_data), 25)
        self.assertEqual(part2(input_data), 286)
