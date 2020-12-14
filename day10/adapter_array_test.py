from unittest import TestCase
from .adapter_array import read_input
from .adapter_array import part1
from .adapter_array import part2


class Test(TestCase):
    def test_find_jolts(self):
        input_data1 = read_input("day10/test_input.txt")
        self.assertEqual(part1(input_data1), 35)
        target1 = max(input_data1) + 3
        input_data1.insert(0, 0)
        input_data1.append(target1)
        self.assertEqual(part2(input_data1, target1, {}), 8)

    def test_find_jolts2(self):
        input_data = read_input("day10/test_input2.txt")
        self.assertEqual(part1(input_data), 220)
        target = max(input_data) + 3
        input_data.insert(0, 0)
        input_data.append(target)
        self.assertEqual(part2(input_data, target, {}), 19208)
