import numpy as np


def read_input(input_path="input_data.txt"):
    input_file = open(input_path)
    input_texts = []
    for line in input_file:
        input_texts.append(np.array(list(line.strip("\n")), dtype=str))
    return input_texts


def count_trees(trajectory_map, right_slope, down_slope):
    number_of_rows = len(trajectory_map) - 1
    number_of_columns = len(trajectory_map[0]) - 1
    count_of_trees, down_coordinate, right_coordinate = 0, 0, 0
    while down_coordinate < number_of_rows:
        down_coordinate = down_coordinate + down_slope
        if right_coordinate + right_slope > number_of_columns:
            right_coordinate = right_slope - (number_of_columns - right_coordinate) - 1
        else:
            right_coordinate = right_coordinate + right_slope
        if trajectory_map[down_coordinate][right_coordinate] == '#':
            count_of_trees += 1
    return count_of_trees


if __name__ == '__main__':
    input_data = read_input()
    slope1 = count_trees(input_data, 1, 1)
    slope2 = count_trees(input_data, 3, 1)
    slope3 = count_trees(input_data, 5, 1)
    slope4 = count_trees(input_data, 7, 1)
    slope5 = count_trees(input_data, 1, 2)
    print(slope1 * slope2 * slope3 * slope4 * slope5)
