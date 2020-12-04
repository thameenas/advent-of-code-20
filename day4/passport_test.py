from unittest import TestCase
from .passport import count_valid_passports
from .passport import read_input


class Test(TestCase):
    def test_valid_passport1(self):
        input_text = read_input("day4/test_input.txt")
        self.assertEqual(count_valid_passports(input_text), 2)

    def test_valid_passport2(self):
        input_text = read_input("day4/test_input2.txt")
        self.assertEqual(count_valid_passports(input_text), 0)

    def test_valid_passport3(self):
        input_text = read_input("day4/test_input3.txt")
        self.assertEqual(count_valid_passports(input_text), 4)
