from unittest import TestCase
from .seating_system import read_input
from .seating_system import part1
from .seating_system import part2


class Test(TestCase):
    def test_seating_system(self):
        input_data = read_input("day11/test_input.txt")
        self.assertEqual(part1(input_data), 37)
        self.assertEqual(part2(input_data), 26)
