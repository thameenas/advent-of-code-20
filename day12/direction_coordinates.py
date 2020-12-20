def read_input(input_path="input.txt"):
    f = open(input_path)
    input_data = f.read().split('\n')
    f.close()
    return input_data


def get_direction(direction):
    if direction == 'E' or direction == 'W':
        return "EW"
    return "NS"


def part1(input_directions):
    direction_coordinates = {"EW": 0, "NS": 0}
    current_direction = 'E'
    news = ['E', 'S', 'W', 'N']
    positive_direction = ['E', 'N', 'R']
    for instruction in input_directions:
        direction = instruction[0]
        value = instruction[1:]
        if direction == 'R' or direction == 'L':
            val = int(value) if direction in positive_direction else -int(value)
            current_direction = news[(news.index(current_direction) + val // 90) % 4]
            continue
        new_direction = current_direction if direction == 'F' else direction
        val = int(value) if new_direction in positive_direction else -int(value)
        direction_coordinates[get_direction(new_direction)] = direction_coordinates[get_direction(new_direction)] + val

    return sum([abs(value) for value in direction_coordinates.values()])


def part2(input_directions):
    ship = {"EW": 0, "NS": 0}
    way_point = {"EW": 10, "NS": 1}
    positive_direction = ['E', 'N', 'R']
    for instruction in input_directions:
        direction = instruction[0]
        value = instruction[1:]
        if direction == 'F':
            ship["EW"] = ship["EW"] + (way_point["EW"] * int(value))
            ship["NS"] = ship["NS"] + (way_point["NS"] * int(value))
        elif direction == 'R':
            for i in range(int(value) // 90):
                way_point["EW"], way_point["NS"] = way_point["NS"], -way_point["EW"]
        elif direction == 'L':
            for i in range(int(value) // 90):
                way_point["EW"], way_point["NS"] = -way_point["NS"], way_point["EW"]
        else:
            val = int(value) if direction in positive_direction else -int(value)
            way_point[get_direction(direction)] = way_point[get_direction(direction)] + val

    return sum([abs(value) for value in ship.values()])


if __name__ == '__main__':
    input_text = read_input()
    print(part1(input_text))
    print(part2(input_text))
