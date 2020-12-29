def read_input(input_path="input.txt"):
    f = open(input_path)
    input_lines = f.read().split('\n\n')
    tile_dict = {}
    for tile in input_lines:
        tile_lines = tile.split("\n")
        tile_number = tile_lines[0].split()[1].replace(":", "")
        tile_dict[tile_number] = find_borders(tile_lines[1:])
    f.close()
    return tile_dict


def find_borders(tile):
    border_top = tile[0]
    border_bottom = tile[- 1]
    border_right = ""
    border_left = ""
    for line in tile:
        border_left = border_left + line[0]
        border_right = border_right + line[-1]
    return [border_top, border_bottom, border_left, border_right]


def find_odd_one(tile_dict):
    entire_borders = []
    for v in tile_dict.values():
        for each_border in v:
            entire_borders.append(each_border)
            entire_borders.append(each_border[::-1])
    border_tiles = []
    for k, v in tile_dict.items():
        single_border_count = 0
        for each_border in v:
            if entire_borders.count(each_border) == 1:
                single_border_count += 1

        if single_border_count == 2:
            border_tiles.append(k)
    product = 1
    for t in border_tiles:
        product = product * int(t)
    return product


if __name__ == '__main__':
    input_tiles = read_input()
    print(find_odd_one(input_tiles))
