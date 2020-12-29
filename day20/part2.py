import numpy as np
import math


def get_tiles_with_number(input_path="input.txt"):
    f = open(input_path)
    input_lines = f.read().split('\n\n')
    tile_dict = {}
    for tile in input_lines:
        tile_lines = tile.split("\n")
        tile_number = tile_lines[0].split()[1].replace(":", "")
        tile_dict[tile_number] = [list(l) for l in tile_lines[1:]]
    f.close()
    return tile_dict


def flip_tiles(tile):
    flip1 = tile
    flip2 = flip1[::-1]
    flip3 = [l[::-1] for l in tile]
    flip4 = flip3[::-1]
    return flip1, flip2, flip3, flip4


def find_4_rotations(tile):
    possible_rotations = [tile]
    previous_rotation = tile
    row_length = len(tile[0])
    for i in range(3):
        current = np.empty([len(tile), len(tile[0])], dtype='str')
        for row in range(len(tile)):
            for column in range(row_length):
                current[row][column] = previous_rotation[row_length - column - 1][row]
        previous_rotation = current
        possible_rotations.append(current.tolist())
    return possible_rotations


def find_all_combinations(tile):
    combinations_with_duplicates = []
    possible_rotations = find_4_rotations(tile)
    for rotated_tile in possible_rotations:
        flipped_combinations = flip_tiles(rotated_tile)
        combinations_with_duplicates.extend(flipped_combinations)

    final_combinations = []
    [final_combinations.append(combination) for combination in combinations_with_duplicates if
     combination not in final_combinations]

    return final_combinations


def find_borders(tile):
    return tile[0], [edge[-1] for edge in tile], tile[-1], [edge[0] for edge in tile]


def find_valid_orientation_of_tiles(tile_id_with_index, border_orientations, dimension, index=(0, 0),
                                    validated_tiles=set()):
    if index[1] == dimension:
        return tile_id_with_index
    adjacent_x, adjacent_y = adjacent_index(dimension, index[0], index[1])
    for tile_id, tiles in border_orientations.items():
        if tile_id in validated_tiles:
            continue
        validated_tiles.add(tile_id)
        for orientation_number, border in tiles.items():
            top_border, _, _, left_border = border
            if index[0] > 0:
                adjacent_right_border = find_right_adjacent_border(border_orientations, tile_id_with_index, index)
                if adjacent_right_border != left_border:
                    continue
            if index[1] > 0:
                adjacent_bottom_border = find_bottom_adjacent_border(border_orientations, tile_id_with_index, index)
                if adjacent_bottom_border != top_border:
                    continue
            tile_id_with_index[index[0]][index[1]] = (tile_id, orientation_number)
            tile_id_by_index = find_valid_orientation_of_tiles(tile_id_with_index, border_orientations, dimension,
                                                               (adjacent_y, adjacent_x),
                                                               validated_tiles=validated_tiles)
            if tile_id_by_index:
                return tile_id_by_index
        validated_tiles.remove(tile_id)
    tile_id_with_index[index[0]][index[1]] = ''
    return ''


def adjacent_index(dimension, x, y):
    adjacent_x = x + 1
    adjacent_y = y
    if adjacent_x == dimension:
        adjacent_x = 0
        adjacent_y += 1
    return adjacent_y, adjacent_x


def find_bottom_adjacent_border(border_orientations, tile_id_with_index, index):
    neighbor_id, orientation_index = tile_id_with_index[index[0]][index[1] - 1]
    _, _, bottom_border, _ = border_orientations[neighbor_id][orientation_index]
    return bottom_border


def find_right_adjacent_border(border_orientations, tile_id_with_index, index):
    neighbor_id, orientation_index = tile_id_with_index[index[0] - 1][index[1]]
    _, right_border, _, _ = border_orientations[neighbor_id][orientation_index]
    return right_border


def find_tiles_image(tile_orientations):
    possible_orientations_per_tile = find_all_possible_orientations(tile_orientations)
    border_orientations_per_tile = find_border_orientations(possible_orientations_per_tile)
    valid_orientations_by_index = get_valid_orientations(len(possible_orientations_per_tile),
                                                         border_orientations_per_tile)
    final_tile_arrangement = remove_border_and_combine(possible_orientations_per_tile, valid_orientations_by_index)
    return final_tile_arrangement


def get_valid_orientations(total_tile_count, border_orientations_per_tile):
    dimension = math.isqrt(total_tile_count)
    tile_id_with_index = [[''] * dimension for _ in range(dimension)]
    return find_valid_orientation_of_tiles(tile_id_with_index, border_orientations_per_tile, dimension)


def find_all_possible_orientations(tile_orientations):
    possible_orientations_per_tile = {}
    for number, tile_borders in tile_orientations.items():
        possible_orientations_per_tile[number] = find_all_combinations(tile_borders)
    return possible_orientations_per_tile


def find_border_orientations(possible_orientations_per_tile):
    border_orientations_per_tile = {}
    for number, tile_orientations in possible_orientations_per_tile.items():
        for i, tile_orientation in enumerate(tile_orientations):
            if number not in border_orientations_per_tile.keys():
                border_orientations_per_tile[number] = {}
            border_orientations_per_tile[number][i] = find_borders(tile_orientation)
    return border_orientations_per_tile


def remove_border_and_combine(possible_tile_orientations, tiles_with_valid_orientation_index):
    final_tile_arrangement = []
    for row in tiles_with_valid_orientation_index:
        tiles_with_border_removed = []
        for tile_id, valid_index in row:
            valid_border_tile_orientation = possible_tile_orientations[tile_id][valid_index]
            tiles_with_border_removed.append([tile[1:-1] for tile in valid_border_tile_orientation[1:-1]])
        convert_to_rows(final_tile_arrangement, tiles_with_border_removed)
    return final_tile_arrangement


def convert_to_rows(final_tile_arrangement, tiles_with_border_removed):
    for y in range(len(tiles_with_border_removed[0][0])):
        tile_row_wise = []
        for index in range(len(tiles_with_border_removed)):
            for x in range(len(tiles_with_border_removed[index])):
                tile_row_wise.extend(tiles_with_border_removed[index][x][y])
        final_tile_arrangement.append(tile_row_wise)


MONSTER = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''


def get_monster_relative_indices():
    monster_index = []
    j_index = 18
    monster_by_lines = MONSTER.split("\n")
    for i, line in enumerate(monster_by_lines[1:]):
        for j, char in enumerate(line):
            if char == '#':
                monster_index.append((i + 1, j - j_index))
    return monster_index


def validate_if_monster(monster_indexes, current_i, current_j, image):
    for each_index in monster_indexes:
        i = current_i + each_index[0]
        j = current_j + each_index[1]
        if 0 <= i < len(image) and 0 <= j < len(image[0]):
            if image[i][j] != '#':
                return False
        else:
            return False
    return True


def replace_monster(monster_indexes, current_i, current_j, image):
    image[current_i][current_j] = '1'
    for each_index in monster_indexes:
        i = current_i + each_index[0]
        j = current_j + each_index[1]
        if image[i][j] == '#':
            image[i][j] = '1'


def find_monster(image):
    monster_indexes = get_monster_relative_indices()
    for i, row in enumerate(image):
        for j, char in enumerate(row):
            if char == '#':
                if validate_if_monster(monster_indexes, i, j, image):
                    replace_monster(monster_indexes, i, j, image)
    return count_of_hash(image)


def count_of_hash(image):
    count = 0
    for row in image:
        for char in row:
            if char == '#':
                count += 1
    return count


def part2(tiles_by_id):
    actual_image = find_tiles_image(tiles_by_id)

    orientations_of_image = find_all_combinations(actual_image)
    return find_monster(orientations_of_image[0])


if __name__ == '__main__':
    input_tiles = get_tiles_with_number()
    print(part2(input_tiles))
