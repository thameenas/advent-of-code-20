from unittest import TestCase
from .trajectory import read_input
from .trajectory import count_trees


class Test(TestCase):
    def test_count_trees1(self):
        input_data = read_input("day3/test_data.txt")
        self.assertEqual(count_trees(input_data, 3, 1), 7)

    def test_count_trees2(self):
        input_data = read_input("day3/test_data.txt")
        self.assertEqual(count_trees(input_data, 1, 1), 2)

    def test_count_trees3(self):
        input_data = read_input("day3/test_data.txt")
        self.assertEqual(count_trees(input_data, 5, 1), 3)

    def test_count_trees4(self):
        input_data = read_input("day3/test_data.txt")
        self.assertEqual(count_trees(input_data, 7, 1), 4)

    def test_count_trees5(self):
        input_data = read_input("day3/test_data.txt")
        self.assertEqual(count_trees(input_data, 1, 2), 2)
