from unittest import TestCase
from .operation_order import *


class Test(TestCase):
    def test_part1(self):
        self.assertEqual(evaluate(["1 + (2 * 3) + (4 * (5 + 6))"], precedence_part1), 51)
        self.assertEqual(evaluate(["2 * 3 + (4 * 5)"], precedence_part1), 26)
        self.assertEqual(evaluate(["5 + (8 * 3 + 9 + 3 * 4 * 3)"], precedence_part1), 437)
        self.assertEqual(evaluate(["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"], precedence_part1), 12240)
        self.assertEqual(evaluate(["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"], precedence_part1), 13632)

    def test_part2(self):
        self.assertEqual(evaluate(["5*3+2*6"], precedence_part2), 150)
        self.assertEqual(evaluate(["1 + (2 * 3) + (4 * (5 + 6))"], precedence_part2), 51)
        self.assertEqual(evaluate(["2 * 3 + (4 * 5)"], precedence_part2), 46)
        self.assertEqual(evaluate(["5 + (8 * 3 + 9 + 3 * 4 * 3)"], precedence_part2), 1445)
        self.assertEqual(evaluate(["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"], precedence_part2), 669060)
        self.assertEqual(evaluate(["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"], precedence_part2), 23340)
