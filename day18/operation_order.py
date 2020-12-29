def read_input(input_path="input.txt"):
    f = open(input_path)
    input_lines = f.read().split('\n')
    f.close()
    return input_lines


def precedence_part1(list_of_ops):
    operators = ['+', '-', '*', '/']
    i = len(list_of_ops) - 1
    list_of_ops.reverse()
    while i > 0:
        character = list_of_ops[i]
        if character in operators:
            operand1 = list_of_ops.pop()
            operator = list_of_ops.pop()
            operand2 = list_of_ops.pop()
            result = eval(operand1 + operator + operand2)
            list_of_ops.append(str(result))
        i = i - 1
    return list_of_ops[0]


def precedence_part2(list_of_ops):
    i = len(list_of_ops) - 1
    list_of_ops.reverse()
    stack = []
    while i >= 0:
        character = list_of_ops[i]
        if character == "+":
            operand1 = stack.pop()
            operator = list_of_ops.pop()
            operand2 = list_of_ops.pop()
            result = eval(operand1 + operator + operand2)
            stack.append(str(result))
            i = i - 2
        else:
            stack.append(character)
            list_of_ops.pop()
            i = i - 1
    return precedence_part1(stack)


def evaluate(lines, evaluation_method):
    results = []
    for line in lines:
        stack = []
        for character in line.replace(" ", "")[::-1]:
            if character == '(':
                new_str = []
                while True:
                    popped_char = stack.pop()
                    if popped_char != ')':
                        new_str.append(popped_char)
                    else:
                        break
                stack.append(evaluation_method(new_str))
            else:
                stack.append(str(character))
        stack.reverse()
        results.append(int(evaluation_method(stack)))
    return sum(results)


def part1(input_lines):
    return evaluate(input_lines, precedence_part1)


def part2(input_lines):
    return evaluate(input_lines, precedence_part2)


if __name__ == '__main__':
    input_data = read_input()
    print(part1(input_data))
    print(part2(input_data))
