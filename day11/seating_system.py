import time


def read_input(input_path="input.txt"):
    f = open(input_path)
    input_data = f.read().split('\n')
    f.close()
    return [list(i) for i in input_data]


def adjacent_seats_count(input_seats, i, j):
    total_adjacent_occupied_seats = 0
    neighbours = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for neighbour in neighbours:
        x_offset = i + neighbour[0]
        y_offset = j + neighbour[1]
        while 0 <= x_offset < len(input_seats) and 0 <= y_offset < len(input_seats[j]):
            if input_seats[x_offset][y_offset] == '.':
                x_offset = x_offset + neighbour[0]
                y_offset = y_offset + neighbour[1]
                continue
            elif input_seats[x_offset][y_offset] == '#':
                total_adjacent_occupied_seats = total_adjacent_occupied_seats + 1
                break
            elif input_seats[x_offset][y_offset] == 'L':
                break

    return total_adjacent_occupied_seats


def immediately_adjacent_seats_count(input_seats, i, j):
    total_adjacent_occupied_seats = 0
    neighbours = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for neighbour in neighbours:
        x_offset = i + neighbour[0]
        y_offset = j + neighbour[1]
        if 0 <= x_offset < len(input_seats) and 0 <= y_offset < len(input_seats[j]):
            if input_seats[x_offset][y_offset] == '#':
                total_adjacent_occupied_seats = total_adjacent_occupied_seats + 1
    return total_adjacent_occupied_seats


def allocate_seats(input_data, adjacent_seat_function, min_visible_occupied_seats):
    new_seats = []
    change_in_seats = False
    occupied_count = 0
    for row in range(len(input_data)):
        new_row = []
        for column in range(len(input_data[0])):
            if input_data[row][column] == 'L' and adjacent_seat_function(input_data, row, column) == 0:
                new_row.append('#')
                change_in_seats = True
            elif input_data[row][column] == '#' and adjacent_seat_function(input_data, row,
                                                                           column) >= min_visible_occupied_seats:
                new_row.append('L')
                change_in_seats = True
            else:
                new_row.append(input_data[row][column])
            if input_data[row][column] == '#':
                occupied_count += 1
        new_seats.append(new_row)
    return new_seats, change_in_seats, occupied_count


def find_occupied_seats(input_data, adjacent_seat_function, min_visible_occupied_seats):
    new_seats, change_in_seats, occupied_count = allocate_seats(input_data, adjacent_seat_function,
                                                                min_visible_occupied_seats)
    if change_in_seats:
        return find_occupied_seats(new_seats, adjacent_seat_function, min_visible_occupied_seats)
    return occupied_count


def part2(input_data):
    return find_occupied_seats(input_data, adjacent_seats_count, 5)


def part1(input_data):
    return find_occupied_seats(input_data, immediately_adjacent_seats_count, 4)


if __name__ == '__main__':
    start = time.time()
    input_text = read_input()
    print(part1(input_text))
    print(part2(input_text))
    print("Total time:", time.time() - start)
