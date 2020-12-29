def convert_to_list(cup_string):
    return list(int(x) for x in cup_string)


def create_adjacent_to_list_part2(cups, n=1000000):
    adjacent_cup_by_index = [-1] * (n + 1)

    for i in range(len(cups) - 1):
        adjacent_cup_by_index[cups[i]] = cups[i + 1]
    adjacent_cup_by_index[cups[-1]] = max(cups) + 1

    for i in range(max(cups) + 1, n):
        adjacent_cup_by_index[i] = i + 1
    adjacent_cup_by_index[n] = cups[0]
    return adjacent_cup_by_index


def create_adjacent_list_part1(cups, n=9):
    adjacent_cup_by_index = [-1] * (n + 1)

    for i in range(len(cups) - 1):
        adjacent_cup_by_index[cups[i]] = cups[i + 1]
    adjacent_cup_by_index[cups[-1]] = cups[0]

    return adjacent_cup_by_index


def play(current, cup_adjacent_to, n):
    picked_cup = [cup_adjacent_to[current]]
    for i in range(2):
        picked_cup.append(cup_adjacent_to[picked_cup[-1]])

    cup_adjacent_to[current] = cup_adjacent_to[picked_cup[-1]]

    destination_cup = find_destination_cup(current, n, picked_cup)
    cup_adjacent_to[picked_cup[-1]] = cup_adjacent_to[destination_cup]
    cup_adjacent_to[destination_cup] = picked_cup[0]

    return cup_adjacent_to[current]


def find_destination_cup(current, n, removed):
    destination = current - 1
    while destination in removed or destination == 0:
        destination -= 1
        if destination == -1:
            destination = n
    return destination


def part2(input_string):
    cups = convert_to_list(input_string)
    cups_adjacent_to = create_adjacent_to_list_part2(cups)
    current = cups[0]
    for i in range(10 ** 7):
        current = play(current, cups_adjacent_to, 1000000)
    first = cups_adjacent_to[1]
    second = cups_adjacent_to[first]
    return first * second


def part1(input_string, iterations):
    cups = convert_to_list(input_string)
    cups_adjacent_to = create_adjacent_list_part1(cups)
    current = cups[0]
    for i in range(iterations):
        current = play(current, cups_adjacent_to, 9)
    final_str = [cups_adjacent_to[1]]
    for i in range(8):
        final_str.append(cups_adjacent_to[final_str[-1]])
    return "".join(str(x) for x in final_str[:-1])


if __name__ == '__main__':
    print(part1("925176834", 100))
    print(part2("925176834"))
