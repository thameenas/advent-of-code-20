from unittest import TestCase
from .boarding_pass import read_input
from .boarding_pass import convert_to_binary
from .boarding_pass import convert_to_decimal

from .boarding_pass import compute_seat_id


class Test(TestCase):
    def test_row_number(self):
        input_data = read_input("day5/test_input1.txt")
        binary = convert_to_binary(input_data[0][:7], 'F', 'B')
        self.assertEqual(convert_to_decimal(binary), 44)

    def test_column_number(self):
        input_data = read_input("day5/test_input1.txt")
        binary = convert_to_binary(input_data[0][7:], 'L', 'R')
        self.assertEqual(convert_to_decimal(binary), 5)

    def test_seat_id(self):
        input_data = read_input("day5/test_input1.txt")
        row = convert_to_binary(input_data[0][:7], 'F', 'B')
        column = convert_to_binary(input_data[0][7:], 'L', 'R')

        self.assertEqual(compute_seat_id(convert_to_decimal(row), convert_to_decimal(column)), 357)
