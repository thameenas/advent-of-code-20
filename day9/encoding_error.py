def read_input(input_path="input_data.txt"):
    f = open(input_path)
    input_data = f.read().split('\n')
    f.close()
    return [int(i) for i in input_data]


def combination_search(search_list, target):
    for i in range(len(search_list) - 1):
        for j in range((i + 1), len(search_list)):
            if search_list[i] + search_list[j] == target:
                return True


def part1(input_data, preamble_size):
    while preamble_size < len(input_data):
        search_list = input_data[preamble_size - 25:preamble_size]
        target = input_data[preamble_size]
        if not combination_search(search_list, target):
            return target
        preamble_size += 1


def part2(input_data, invalid_number):
    for i in range(len(input_data)):
        contiguous_numbers = []
        sum_of_numbers = 0
        for j in range(i, len(input_data)):
            sum_of_numbers = sum_of_numbers + input_data[j]
            contiguous_numbers.append(input_data[j])
            if sum_of_numbers == invalid_number:
                sorted_list = sorted(contiguous_numbers)
                return sorted_list[0] + sorted_list[-1]
            if sum_of_numbers > invalid_number:
                break


if __name__ == '__main__':
    input_text = read_input()
    invalid = part1(input_text, 25)
    print(invalid)
    print(part2(input_text, invalid))
