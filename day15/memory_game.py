import time


def game(input_data, total_turns):
    start = time.time()
    memory_game = {}
    for i in range(len(input_data)):
        memory_game[input_data[i]] = [i + 1]
    previous_number = input_data[-1]
    for i in range(len(input_data) + 1, total_turns + 1):
        if len(memory_game[previous_number]) == 1:
            next_number = 0
        else:
            next_number = memory_game[previous_number][-1] - memory_game[previous_number][-2]
        if next_number in memory_game.keys():
            memory_game[next_number].append(i)
        else:
            memory_game[next_number] = [i]
        previous_number = next_number
    print("Total time", time.time() - start)
    return previous_number


if __name__ == '__main__':
    print(game([2, 20, 0, 4, 1, 17], 2020))
    print(game([2, 20, 0, 4, 1, 17], 30000000))
