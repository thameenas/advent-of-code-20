def read_input(input_path="input.txt"):
    f = open(input_path)
    input_data = f.read().split('\n')
    f.close()
    return sorted([int(i) for i in input_data])


def part1(voltage_list):
    current_voltage = 0
    jolt_dict = {1: 0, 3: 0}
    for voltage in voltage_list:
        voltage_difference = voltage - current_voltage
        current_voltage = voltage
        if voltage_difference == 1 or voltage_difference == 3:
            jolt_dict[voltage_difference] = jolt_dict[voltage_difference] + 1

    return jolt_dict[1] * (jolt_dict[3] + 1)


def part2(voltage_list, target, voltage_dict={}, voltage=0):
    if voltage in voltage_dict:
        return voltage_dict[voltage]
    if voltage == target:
        return 1
    total_adapters = 0
    if voltage + 1 in voltage_list:
        total_adapters += part2(voltage_list, target, voltage_dict, voltage + 1)
    if voltage + 2 in voltage_list:
        total_adapters += part2(voltage_list, target, voltage_dict, voltage + 2)
    if voltage + 3 in voltage_list:
        total_adapters += part2(voltage_list, target, voltage_dict, voltage + 3)
    voltage_dict[voltage] = total_adapters
    return voltage_dict[voltage]


if __name__ == '__main__':
    input_text = read_input()
    print(part1(input_text))
    target = max(input_text) + 3
    input_text.insert(0, 0)
    input_text.append(target)
    print(part2(input_text, target))
