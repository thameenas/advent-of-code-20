def read_input(input_path="input_data.txt"):
    f = open(input_path)
    input_data = f.read().split('\n')
    f.close()
    return input_data


def convert_to_binary(seat_code, lower_code, higher_code):
    return seat_code.replace(lower_code, '0').replace(higher_code, '1')


def convert_to_decimal(binary_code):
    return int(binary_code, 2)


def compute_seat_id(row_number, column_number):
    return row_number * 8 + column_number


def find_missing_seat_number():
    for seat in range(sorted(seat_numbers)[0], sorted(seat_numbers)[-1]):
        if seat not in seat_numbers:
            return seat


if __name__ == '__main__':
    boarding_passes = read_input()

    seat_numbers = []
    for boarding_pass in boarding_passes:
        row = convert_to_binary(boarding_pass[:7], 'F', 'B')
        column = convert_to_binary(boarding_pass[7:], 'L', 'R')
        seat_numbers.append(compute_seat_id(convert_to_decimal(row), convert_to_decimal(column)))
    print(max(seat_numbers))
    print(find_missing_seat_number())
