from unittest import TestCase
from .shuttle_search import read_input
from .shuttle_search import part1
from .shuttle_search import part2


class Test(TestCase):
    def test_find_bus(self):
        timestamp, bus_ids = read_input("day13/test_input.txt")
        self.assertEqual(part1(timestamp, bus_ids), 295)
        self.assertEqual(part2(bus_ids), 1068781)

    def test_part2(self):
        self.assertEqual(part2(["17", "x", "13", "19"]), 3417)
        self.assertEqual(part2(["67", "7", "59", "61"]), 754018)
        self.assertEqual(part2(["67", "x", "7", "59", "61"]), 779210)
        self.assertEqual(part2(["67", "7", "x", "59", '61']), 1261476)
        self.assertEqual(part2(["1789", "37", "47", "1889"]), 1202161486)
