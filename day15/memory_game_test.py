from unittest import TestCase
from .memory_game import game


class Test(TestCase):
    def test_game1(self):
        self.assertEqual(game([0, 3, 6], 10), 0)
        self.assertEqual(game([1, 3, 2], 2020), 1)
        self.assertEqual(game([2, 1, 3], 2020), 10)
        self.assertEqual(game([1, 2, 3], 2020), 27)
        self.assertEqual(game([2, 3, 1], 2020), 78)
        self.assertEqual(game([3, 2, 1], 2020), 438)
        self.assertEqual(game([3, 1, 2], 2020), 1836)

    def test_game2(self):
        self.assertEqual(game([0, 3, 6], 30000000), 175594)
