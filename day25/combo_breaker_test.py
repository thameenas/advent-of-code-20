from unittest import TestCase

from .combo_breaker import *


class MyTestCase(TestCase):
    def test_transform(self):
        self.assertEqual(find_loop_size(5764801, 7), 8)
        self.assertEqual(find_loop_size(17807724, 7), 11)
        self.assertEqual(find_key(17807724, 8), 14897079)
        self.assertEqual(find_key(5764801, 11), 14897079)
