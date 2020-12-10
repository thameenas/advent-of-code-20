from unittest import TestCase
from .colour_bags import add_to_graph
from .colour_bags import read_input
from .colour_bags import part2
from .colour_bags import part1


class Test(TestCase):
    def test_add_to_graph(self):
        input_data = read_input("day7/test_input.txt")

        self.assertEqual(part1(input_data), 4)
        self.assertEqual(part2(input_data), 32)

    def test_add_to_graph2(self):
        input_data = read_input("day7/test_input2.txt")

        self.assertEqual(part2(input_data), 126)
