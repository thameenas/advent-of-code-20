import re


def read_input(input_path="input.txt"):
    f = open(input_path)
    input_data = f.read().split('\n')
    f.close()
    return input_data


def find_neighbours(coordinate):
    neighbours = set()
    neighbour_coord = [(1, 0), (-1, 0), (0.5, 0.5), (-0.5, -0.5), (-0.5, 0.5), (0.5, -0.5)]
    for neighbour in neighbour_coord:
        neighbour_coord = (coordinate[0] + neighbour[0], coordinate[1] + neighbour[1])
        neighbours.add(neighbour_coord)
    return neighbours


def count_of_black_neighbours(coordinate, black_tiles_coordinates):
    return len(find_neighbours(coordinate).intersection(black_tiles_coordinates))


def find_tiles(tile_directions):
    black_tiles_coordinates = set()
    for directions in tile_directions:
        direction_list = re.findall('se|e|sw|w|ne|nw', directions)
        direction_dict = {'e': [1, 0], 'w': [-1, 0],
                          'ne': [0.5, 0.5], 'sw': [-0.5, -0.5],
                          'nw': [-0.5, 0.5], 'se': [0.5, -0.5]}
        current = [0, 0]
        for direction in direction_list:
            current[0] += direction_dict[direction][0]
            current[1] += direction_dict[direction][1]

        if (current[0], current[1]) in black_tiles_coordinates:
            black_tiles_coordinates.remove((current[0], current[1]))
        else:
            black_tiles_coordinates.add((current[0], current[1]))
    return black_tiles_coordinates


def flip_by_rule(black_tiles_coordinates):
    to_remove = set()
    to_add = set()
    for coordinate in black_tiles_coordinates:
        neighbour_count = count_of_black_neighbours(coordinate, black_tiles_coordinates)
        if neighbour_count == 0 or neighbour_count > 2:
            to_remove.add(coordinate)
        for neighbour_tile in find_neighbours(coordinate):
            neighbour_count = count_of_black_neighbours(neighbour_tile, black_tiles_coordinates)
            if neighbour_count == 2:
                to_add.add(neighbour_tile)
    for coordinate in to_remove:
        black_tiles_coordinates.remove(coordinate)
    for coordinate in to_add:
        black_tiles_coordinates.add(coordinate)
    return black_tiles_coordinates


if __name__ == '__main__':
    input_lines = read_input()
    tiles_coordinates = find_tiles(input_lines)
    print(len(tiles_coordinates))
    for i in range(100):
        coord_dict = flip_by_rule(tiles_coordinates)
    print(len(tiles_coordinates))
