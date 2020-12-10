def read_input(input_path="input_data.txt"):
    f = open(input_path)
    input_data = f.read().split('\n')
    f.close()
    return input_data


def part1(input_instructions):
    visited = []
    acc = 0
    index = 0
    repeat_encountered = False
    while index < len(input_instructions):
        if index in visited:
            repeat_encountered = True
            break
        instruction, code = input_instructions[index].split(" ")
        visited.append(index)
        if instruction == 'acc':
            acc += int(code)
            index += 1
        elif instruction == 'nop':
            index += 1
        elif instruction == 'jmp':
            index = index + int(code)
    return acc, repeat_encountered


def part2(input_instructions):
    for index in range(len(input_instructions)):
        instruction = input_instructions[index].split(" ")[0]
        new_instructions = input_instructions.copy()
        if instruction == 'jmp':
            new_instructions[index] = new_instructions[index].replace("jmp", "nop")
        elif instruction == 'nop':
            new_instructions[index] = new_instructions[index].replace("nop", "jmp")
        acc, repeat_encountered = part1(new_instructions)
        if not repeat_encountered:
            return acc


if __name__ == '__main__':
    input_text = read_input()
    response = part1(input_text)
    print(response[0])
    print(part2(input_text))
