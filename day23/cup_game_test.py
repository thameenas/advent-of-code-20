from unittest import TestCase

from .cup_game import *


class Test(TestCase):
    def test_part1(self):
        self.assertEqual(part1("389125467", 10), "92658374")
        self.assertEqual(part1("389125467", 100), "67384529")

    def test_part2(self):
        self.assertEqual(part2("389125467"), 149245887792)
