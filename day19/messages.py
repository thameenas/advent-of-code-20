def read_input(input_path="input.txt"):
    f = open(input_path)
    input_lines = f.read().split('\n\n')
    messages = input_lines[1].split("\n")
    split_rules = {}
    for rule in input_lines[0].split("\n"):
        split_rules[rule.split(":")[0]] = rule.split(":")[1].lstrip().rstrip()
    f.close()
    return split_rules, messages


def validate(rule_key, message, rule_set):
    current_rule = rule_set[rule_key]
    if current_rule == '"a"' or current_rule == '"b"':
        current_rule = current_rule.replace("\"", "")
        if message == "":
            return []
        if message[0] == current_rule:
            return [message[1:]]
        return []
    parsed_messages_by_rule = []
    for sub_rule in current_rule.split('|'):
        message_to_parse = [message]
        for each_sub_rule in sub_rule.split():
            message_to_parse = parse_message(each_sub_rule, message_to_parse, rule_set)
            if len(message_to_parse) == 0:
                break
        parsed_messages_by_rule += message_to_parse
    return parsed_messages_by_rule


def parse_message(each_sub_rule, parsed_message, rule_set):
    parsed_msgs = []
    for msg_string in parsed_message:
        for parsed_strings in validate(each_sub_rule, msg_string, rule_set):
            parsed_msgs.append(parsed_strings)
    return parsed_msgs


def count_valid(messages, rule_set):
    count = 0
    for message in messages:
        parsed_string = validate('0', message, rule_set)
        if '' in parsed_string:
            count += 1
    return count


def part1(rule_set, messages):
    return count_valid(messages, rule_set)


def part2(rule_set, messages):
    rule_set['8'] = '42 | 42 8'
    rule_set['11'] = '42 31 | 42 11 31'
    return count_valid(messages, rule_set)


if __name__ == '__main__':
    rules, msg = read_input()
    print(part1(rules, msg))
    print(part2(rules, msg))
