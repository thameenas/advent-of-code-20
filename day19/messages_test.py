from unittest import TestCase
from .messages import *


class Test(TestCase):
    def test_part1(self):
        rule, messages = read_input("day19/test_input.txt")
        self.assertEqual(part1(rule, messages), 2)

    def test_part2(self):
        rule, messages = read_input("day19/test_input2.txt")
        self.assertEqual(part2(rule, messages), 12)
