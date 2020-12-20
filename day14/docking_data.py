def read_input(input_path="input.txt"):
    f = open(input_path)
    input_data = f.read().split('\n')
    f.close()
    return input_data


def part1(input_data):
    mask = ""
    memory = {}
    for line in input_data:
        split_line = line.split()
        if split_line[0] == 'mask':
            mask = split_line[2].lstrip("X")
        else:
            binary_number = bin(int(split_line[2]))[2:]
            binary_number = "0" * (len(mask) - len(binary_number)) + binary_number
            binary_digits = list(binary_number)
            for i in range(len(mask)):
                if mask[i] != 'X':
                    binary_digits[i] = mask[i]
            memory_key = ''.join(filter(lambda i: i.isdigit(), split_line[0]))
            memory[memory_key] = int("".join(binary_digits), 2)
    return sum(list(memory.values()))


def possible_combinations(binary_digits, memory, curr_value):
    floating_bits_count = binary_digits.count('X')

    floating_bits_combinations = []
    for bit_index in range(2 ** floating_bits_count):
        floating_bits_combinations.append(list(bin(bit_index)[2:].zfill(floating_bits_count)))

    for bit in floating_bits_combinations:
        bit_index = 0
        new_combination = ""
        for character in binary_digits:
            if character == "X":
                new_combination += str(bit[bit_index])
                bit_index += 1
            else:
                new_combination += str(character)
        memory[int(new_combination, 2)] = curr_value


def part2(input_data):
    mask = ""
    memory = {}
    for line in input_data:
        split_line = line.split()
        if split_line[0] == 'mask':
            mask = split_line[2].lstrip('0')
        else:
            binary_number = bin(int("".join(filter(lambda i: i.isdigit(), split_line[0]))))[2:]
            if len(mask) > len(binary_number):
                binary_number = "0" * (len(mask) - len(binary_number)) + binary_number
            elif len(mask) < len(binary_number):
                mask = "0" * (len(binary_number) - len(mask)) + mask
            binary_digits = list(binary_number)
            for i in range(len(mask)):
                if mask[i] == 'X' or mask[i] == '1':
                    binary_digits[i] = mask[i]
            possible_combinations(binary_digits, memory, split_line[2])

    return sum(list(int(i) for i in memory.values()))


if __name__ == '__main__':
    input_text = read_input()
    print(part1(input_text))
    print(part2(input_text))
