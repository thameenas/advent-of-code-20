from unittest import TestCase
from .encoding_error import read_input
from .encoding_error import part1
from .encoding_error import part2


class Test(TestCase):
    def test_encoding_error(self):
        input_data = read_input("day9/test_input1.txt")
        self.assertEqual(part1(input_data, 5), 127)
        self.assertEqual(part2(input_data, 127), 62)
