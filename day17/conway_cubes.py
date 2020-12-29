from itertools import product


def read_input(input_path="input.txt"):
    f = open(input_path)
    input_cells = f.read().split('\n')
    f.close()
    return input_cells


def find_neighbours(coordinate, dimension):
    neighbours = set()
    for neighbour in (product([0, 1, -1], repeat=dimension)):
        neighbours.add(tuple(sum(x) for x in zip(coordinate, neighbour)))

    neighbours.remove(coordinate)
    return neighbours


def set_initial_state(input_state, dimension):
    active = set()
    for i, line in enumerate(input_state):
        for j, state in enumerate(line):
            if state == '#':
                active.add((i, j) + (0,) * (dimension - 2))
    return active


def cycle(active_coordinates, dimension):
    to_remove = set()
    to_add = set()
    for coordinate in active_coordinates:
        neighbours = find_neighbours(coordinate, dimension)
        count_of_active_neighbours = len(neighbours.intersection(active_coordinates))
        if count_of_active_neighbours != 2 and count_of_active_neighbours != 3:
            to_remove.add(coordinate)
        inactive_neighbours = neighbours.difference(active_coordinates)
        for inactive_coordinate in inactive_neighbours:
            if len(find_neighbours(inactive_coordinate, dimension).intersection(active_coordinates)) == 3:
                to_add.add(inactive_coordinate)
    for coordinate in to_add:
        active_coordinates.add(coordinate)
    for coordinate in to_remove:
        active_coordinates.remove(coordinate)
    return active_coordinates


def part1(initial_cells):
    active = set_initial_state(initial_cells, 3)
    for i in range(6):
        active = cycle(active, 3)
    print(len(active))


def part2(initial_cells):
    active = set_initial_state(initial_cells, 4)
    for i in range(6):
        active = cycle(active, 4)
    print(len(active))


if __name__ == '__main__':
    input_data = read_input()

    part1(input_data)
    part2(input_data)
