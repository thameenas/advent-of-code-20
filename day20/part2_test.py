from unittest import TestCase
from .part2 import *


class Test(TestCase):

    def test_part2(self):
        tiles = get_tiles_with_number("day20/test_input.txt")
        self.assertEqual(part2(tiles), 273)
