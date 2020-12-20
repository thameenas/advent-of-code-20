from unittest import TestCase
from .docking_data import read_input
from .docking_data import part1
from .docking_data import part2


class Test(TestCase):
    def test_find_bus(self):
        input_data = read_input("day14/test_input.txt")
        self.assertEqual(part1(input_data), 165)

    def test_part2(self):
        input_data = read_input("day14/test_input2")
        self.assertEqual(part2(input_data), 208)
