def read_input(input_path="input.txt"):
    f = open(input_path)
    input_data = f.read().split('\n')
    f.close()
    return int(input_data[0]), input_data[1].split(",")


def part1(current_time, bus_ids):
    waiting_time_to_bus_id = {}
    for bus_id in bus_ids:
        if bus_id != 'x':
            remainder = current_time % int(bus_id)
            next_timestamp = current_time + (int(bus_id) - remainder)
            waiting_time_to_bus_id[next_timestamp - current_time] = int(bus_id)
    list_of_waiting_time = list(waiting_time_to_bus_id.keys())
    list_of_waiting_time.sort()
    waiting_time = list_of_waiting_time[0]
    next_bus_id = waiting_time_to_bus_id.get(waiting_time)
    return waiting_time * next_bus_id


def find_product(bus_ids):
    product = 1
    for bus_id in bus_ids:
        if bus_id != 'x':
            product = product * int(bus_id)
    return product


def part2(bus_ids):
    total_product = find_product(bus_ids)
    products = []
    for i in range(1, len(bus_ids[1:]) + 1):
        if bus_ids[i] == 'x':
            continue
        remainder = int(bus_ids[i]) - i
        N = int(total_product / int(bus_ids[i]))
        inverse = pow(N, -1, int(bus_ids[i]))
        products.append(remainder * N * inverse)
    return sum(products) % total_product


if __name__ == '__main__':
    timestamp, ids = read_input()

    print(part1(timestamp, ids))
    print(part2(ids))
