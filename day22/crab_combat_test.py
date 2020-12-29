from unittest import TestCase

from .crab_combat import *


class Test(TestCase):
    def test_game(self):
        player1, player2 = read_input("day22/test_input.txt")
        self.assertEqual(part1(player1.copy(), player2.copy()), 306)
        self.assertEqual(part2(player1.copy(), player2.copy()), 291)
