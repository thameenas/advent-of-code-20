from unittest import TestCase
from .password import validate_password


class Test(TestCase):
    def test_validate_by_count1(self):
        self.assertEqual(validate_password(['1-3 z: zzqj']), (1, 1))

    def test_validate_by_count2(self):
        self.assertEqual(validate_password(['1-3 z: zzqj', '1-5 a: asdazzaaqj']), (2, 2))

    def test_validate_by_index1(self):
        self.assertEqual(validate_password(['1-3 a: abcde']), (1, 1))

    def test_validate_by_index2(self):
        self.assertEqual(validate_password(['1-3 b: cdefg']), (0, 0))

    def test_validate_by_index3(self):
        self.assertEqual(validate_password(['2-9 c: ccccccccc']), (0, 1))
