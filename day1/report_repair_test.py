import unittest
from unittest import TestCase
from .report_repair import find_product


class Test(TestCase):

    def test_combinations1(self):
        self.assertEqual(find_product([1, 2, 3, 7], 5, 2), 6)

    def test_combinations2(self):
        self.assertEqual(find_product([1, 2, 3, 7, 1, 5], 6, 2), 5)

    def test_combinations3(self):
        self.assertEqual(find_product([1, 2, 3, 7, 1, 5], 6, 3), 6)

    def test_combinations4(self):
        self.assertEqual(find_product([1, 2, 3, 7, 1, 12, 10, 5], 23, 3), 120)

    def test_combinations5(self):
        self.assertEqual(find_product([1, 2, 3, 7, 1, 12, 10, 5], 13, 4), 42)

    def test_combinations6(self):
        self.assertEqual(find_product([1, 2, 3, 7, 4, 12, 10, 5], 17, 5), 168)


if __name__ == '__main__':
    unittest.main()
