import unittest
from unittest import TestCase
from .report_repair import find_product


class Test(TestCase):

    def test_product1(self):
        self.assertEqual(find_product([1, 2, 3, 7], 3, 6), 6)

    def test_product2(self):
        self.assertEqual(find_product([1, 2, 3, 7], 3, 12), 42)

    def test_product3(self):
        self.assertEqual(find_product([1, 2, 3, 7], 2, 5), 6)

    def test_product4(self):
        self.assertEqual(find_product([1, 2, 3, 7, 1, 5], 2, 6), 5)

    def test_product5(self):
        self.assertEqual(find_product([1, 2, 3, 7, 1, 5], 3, 6), 6)

    def test_product6(self):
        self.assertEqual(find_product([1, 2, 3, 7, 1, 12, 10, 5], 3, 23), 120)

    def test_product7(self):
        self.assertEqual(find_product([1, 2, 3, 7, 1, 12, 10, 5], 4, 13), 42)

    def test_product8(self):
        self.assertEqual(find_product([1, 2, 3, 7, 4, 12, 10, 5], 5, 17), 168)

    def test_product9(self):
        self.assertEqual(find_product([1721, 979, 366, 299, 675, 1456], 2, 2020), 514579)

    def test_product10(self):
        self.assertEqual(find_product([1721, 979, 366, 299, 675, 1456], 3, 2020), 241861950)


if __name__ == '__main__':
    unittest.main()
