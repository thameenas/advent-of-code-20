from unittest import TestCase

from .conway_cubes import *


class Test(TestCase):
    def test_3_dimension(self):
        input_lines = read_input("day17/test_input.txt")
        active_coordinates = set_initial_state(input_lines, 3)
        for j in range(6):
            active_coordinates = cycle(active_coordinates, 3)
        self.assertEqual(len(active_coordinates), 112)

    def test_4_dimension(self):
        input_lines = read_input("day17/test_input.txt")
        active_coordinates = set_initial_state(input_lines, 4)
        for j in range(6):
            active_coordinates = cycle(active_coordinates, 4)
        self.assertEqual(len(active_coordinates), 848)
