from day7.graph import Graph
import time


def read_input(input_path="day7/input_data.txt"):
    f = open(input_path)
    input_data = f.read().split('\n')
    f.close()
    return input_data


def add_to_graph(input_lines):
    normal_graph = Graph()
    for line in input_lines:
        if "contain no other bags." in line:
            normal_graph.add_wighted_edge(" ".join(line.split()[:2]), "")
            continue
        list_of_bags = line.replace(",", "").replace(".", "").replace("bags", "bag").replace("contain", "").split(
            "bag")
        i = 1
        outer_bag = list_of_bags[0].strip()
        while i < len(list_of_bags) - 1:
            inner_bag_colour = list_of_bags[i].strip()
            normal_graph.add_wighted_edge(outer_bag, inner_bag_colour[1:].strip(), inner_bag_colour[0])
            i += 1
    return normal_graph


def part1(input_lines):
    graph = add_to_graph(input_lines)
    graph.find_bags_that_contain("shiny gold")
    count_of_bags = graph.find_number_of_bags("shiny gold")
    return len(graph.bag_list), count_of_bags


def part2(input_lines):
    graph = add_to_graph(input_lines)
    return graph.find_number_of_bags("shiny gold")


if __name__ == '__main__':
    start_time = time.time()
    input_text = read_input()
    print(part1(input_text))
    # print(part2(input_text))
    print("Total time:", time.time() - start_time)
