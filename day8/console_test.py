from unittest import TestCase
from .console import part1
from .console import read_input
from .console import part2


class Test(TestCase):
    def test_console(self):
        input_data = read_input("day8/test_data.txt")

        self.assertEqual(part1(input_data)[0], 5)
        self.assertEqual(part2(input_data), 8)
