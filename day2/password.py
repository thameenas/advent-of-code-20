def read_input():
    input_file = open("password_input.txt")
    input_texts = []
    for line in input_file:
        input_texts.append((line.strip("\n")))
    return input_texts


def validate_by_count(password_string, letter, first_digit, second_digit):
    if first_digit <= password_string.count(letter) <= second_digit:
        return True


def validate_by_index(password_string, letter, first_digit, second_digit):
    if (password_string[first_digit - 1] == letter) ^ (password_string[second_digit - 1] == letter):
        return True


def split(password):
    password_line = password.split(' ')
    limit = password_line[0].split('-')
    first_digit = int(limit[0])
    second_digit = int(limit[1])
    letter = password_line[1].strip(':')
    password_string = password_line[2]
    return password_string, letter, first_digit, second_digit


def validate_password_by_count(password_policies):
    count = 0
    for password in password_policies:
        password_string, letter, first_digit, second_digit = split(password)
        if validate_by_count(password_string, letter, first_digit, second_digit):
            count = count + 1
    return count


def validate_password_by_index(password_policies):
    count = 0
    for password in password_policies:
        password_string, letter, first_digit, second_digit = split(password)
        if validate_by_index(password_string, letter, first_digit, second_digit):
            count = count + 1
    return count


if __name__ == '__main__':
    input_data = read_input()
    print(validate_password_by_count(input_data))
    print(validate_password_by_index(input_data))
