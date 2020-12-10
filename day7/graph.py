class Graph:
    graph_dict = {}
    bag_list = set()

    def add_wighted_edge(self, node, neighbour, weight=None):
        if node not in self.graph_dict:
            if neighbour == "":
                self.graph_dict[node] = {}
            else:
                self.graph_dict[node] = {neighbour: weight}
        else:
            self.graph_dict[node].update({neighbour: weight})

    def find_bags_that_contain(self, bag_colour):
        for outer_bag in self.graph_dict:
            if bag_colour in self.graph_dict[outer_bag].keys():
                self.bag_list.add(outer_bag)
                self.find_bags_that_contain(outer_bag)

    def find_number_of_bags(self, start):
        count = 0
        if len(self.graph_dict[start].keys()) == 0:
            return 0

        for next_ele in set(self.graph_dict[start].keys()):
            number = int(self.graph_dict[start].get(next_ele))
            count = count + number + (number * self.find_number_of_bags(next_ele))

        return count
