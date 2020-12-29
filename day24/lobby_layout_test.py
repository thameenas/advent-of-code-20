from unittest import TestCase

from .lobby_layout import *


class Test(TestCase):
    def test_something(self):
        input_data = read_input("day24/test_input.txt")
        black_tiles_coordinates = find_tiles(input_data)
        self.assertEqual(len(black_tiles_coordinates), 10)

        black_tiles_coordinates = flip_by_rule(black_tiles_coordinates)
        self.assertEqual(len(black_tiles_coordinates), 15)

        black_tiles_coordinates = flip_by_rule(black_tiles_coordinates)
        self.assertEqual(len(black_tiles_coordinates), 12)

        black_tiles_coordinates = flip_by_rule(black_tiles_coordinates)
        self.assertEqual(len(black_tiles_coordinates), 25)

        black_tiles_coordinates = flip_by_rule(black_tiles_coordinates)
        self.assertEqual(len(black_tiles_coordinates), 14)

        black_tiles_coordinates = flip_by_rule(black_tiles_coordinates)
        self.assertEqual(len(black_tiles_coordinates), 23)
