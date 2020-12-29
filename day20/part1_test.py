from unittest import TestCase

from .part1 import *


class Test(TestCase):

    def test_part1(self):
        input_data = read_input("day20/test_input.txt")
        self.assertEqual(find_odd_one(input_data), 20899048083289)
