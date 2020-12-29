def split_input(input_path="input.txt"):
    f = open(input_path)
    input_data = f.read().split('\n\n')
    f.close()
    field_with_range = find_field_with_range(input_data)
    nearby_tickets = get_nearby_tickets(input_data)
    your_ticket = get_your_tickets(input_data)
    return field_with_range, nearby_tickets, your_ticket


def find_field_with_range(input_data):
    field_with_range = {}
    fields = input_data[0].split("\n")
    for line in fields:
        range_elements = []
        field_name = line.split(":")[0]
        field_range = [seats.split("-") for seats in line.split(":")[1].split(" or ")]
        for range_limit in field_range:
            for i in range(int(range_limit[0]), int(range_limit[1]) + 1):
                range_elements.append(i)
        field_with_range[field_name] = range_elements
    return field_with_range


def get_nearby_tickets(input_data):
    nearby_tickets = []
    input_nearby_tickets = input_data[2].split("\n")[1:]
    for ticket in input_nearby_tickets:
        nearby_tickets.append([int(seat) for seat in ticket.split(",")])
    return nearby_tickets


def get_your_tickets(input_data):
    your_ticket = input_data[1].split("\n")[1]
    return [int(seat) for seat in your_ticket.split(",")]


def find_invalid_seats_sum(seat_dict, nearby_tickets):
    total_range = set()
    invalid_tickets = []
    valid_tickets = []
    for seats in seat_dict.values():
        total_range.update(seats)
    for ticket in nearby_tickets:
        remainder = set(ticket).difference(total_range)
        if len(remainder) > 0:
            invalid_tickets.append(*remainder)
        else:
            valid_tickets.append(ticket)

    return sum(invalid_tickets), valid_tickets


def find_possible_columns(valid_tickets, columns, values):
    return [col for col in columns
            if all(ticket[col] in values for ticket in valid_tickets)]


def match_your_ticket(your_ticket, fields):
    ticket = {}
    for i in range(len(your_ticket)):
        ticket[fields[i]] = your_ticket[i]
    return ticket


def find_departure_seats(ticket):
    result = 1
    for field in ticket.keys():
        if field.startswith('departure'):
            result = result * ticket[field]
    return result


def match_seat_to_field(seat_dict, valid_tickets):
    matched = {}
    columns = set(range(len(seat_dict)))

    for _ in range(len(seat_dict)):
        for field, seat_range in seat_dict.items():
            possible_columns = find_possible_columns(valid_tickets, columns, seat_range)
            if len(possible_columns) == 1:
                columns.remove(possible_columns[0])
                matched[possible_columns[0]] = field

    return matched


if __name__ == '__main__':
    field_with_seat_range, nearby_tickets_seats, your_ticket_seats = split_input()
    seats_sum, valid = find_invalid_seats_sum(field_with_seat_range, nearby_tickets_seats)
    print(seats_sum)
    matched_fields = match_seat_to_field(field_with_seat_range, valid)
    matched_your_ticket = match_your_ticket(your_ticket_seats, matched_fields)
    print(find_departure_seats(matched_your_ticket))
