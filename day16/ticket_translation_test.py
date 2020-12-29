from unittest import TestCase
from .ticket_translation import *


class Test(TestCase):
    def test_part1(self):
        fields, nearby_ticket, your_ticket = split_input("day16/test_input.txt")
        sum_of_seats, valid_seats = find_invalid_seats_sum(fields, nearby_ticket)
        self.assertEqual(sum_of_seats, 71)

    def test_part2(self):
        fields, nearby_ticket, your_ticket = split_input("day16/test_input2.txt")
        sum_of_seats, valid_seats = find_invalid_seats_sum(fields, nearby_ticket)
        corrected_field = match_seat_to_field(fields, valid_seats)
        self.assertEqual(match_your_ticket(your_ticket, corrected_field), {'class': 12, 'row': 11, 'seat': 13})
