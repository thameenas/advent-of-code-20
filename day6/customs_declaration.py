def read_input(input_path="input_data.txt"):
    f = open(input_path)
    input_data = f.read().split('\n\n')
    f.close()
    return input_data


def find_count(group_of_answers):
    count_intersection = 0
    count_union = 0
    for answers in group_of_answers:
        answer_split_by_letter = [set(answer) for answer in answers.split("\n")]
        count_union = count_union + len(answer_split_by_letter[0].union(*answer_split_by_letter[1:]))
        count_intersection = count_intersection + len(
            answer_split_by_letter[0].intersection(*answer_split_by_letter[1:]))

    return count_union, count_intersection


if __name__ == '__main__':
    input_text = read_input()
    print(find_count(input_text))
