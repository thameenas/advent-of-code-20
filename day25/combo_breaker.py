def find_loop_size(public_key, subject_number):
    value = 1
    loop_size = 0
    while value != public_key:
        loop_size += 1
        value = value * subject_number
        value = value % 20201227
    return loop_size


def find_key(subject_number, loop_size):
    value = 1
    for i in range(loop_size):
        value = value * subject_number
        value = value % 20201227
    return value


if __name__ == '__main__':
    card_loop_size = find_loop_size(14012298, 7)
    door_loop_size = find_loop_size(74241, 7)
    print(find_key(74241, card_loop_size))
    print(find_key(14012298, door_loop_size))
