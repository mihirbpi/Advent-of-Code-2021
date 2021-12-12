from aocd import get_data

input = get_data(year=2021,day=12).split("\n")

def traverse_graph(vertex, visited_list, path_list, adjacency_dict, small_cave):

    visited_list.append(vertex)

    if(vertex == "end"):

        if(visited_list.copy() not in path_list):
            path_list.append(visited_list.copy())

        return

    for other_vertex in [x for x in adjacency_dict[vertex] if x in adjacency_dict or x == "end"]:

        if(other_vertex == "end"):
            traverse_graph(other_vertex, visited_list.copy(), path_list, adjacency_dict, small_cave)

        elif(other_vertex == small_cave  and visited_list.count(other_vertex) < 2):
            traverse_graph(other_vertex, visited_list.copy(), path_list, adjacency_dict, small_cave)

        elif(other_vertex.islower() and not other_vertex in visited_list):
            traverse_graph(other_vertex, visited_list.copy(), path_list, adjacency_dict, small_cave)

        elif(other_vertex.isupper()):
            traverse_graph(other_vertex, visited_list.copy(), path_list, adjacency_dict, small_cave)

adjacency_dict = {}
small_caves = set()

for line in input:
    start, end = line.split("-")

    if(start.islower() and start not in ["start", "end"]):
        small_caves.add(start)

    if(end.islower() and end not in ["start", "end"]):
        small_caves.add(end)

    if(end == "start"):

        if(end in adjacency_dict):
            adjacency_dict[end].append(start)
        else:
            adjacency_dict[end] = [start]
    else:

        if(start in adjacency_dict):
            adjacency_dict[start].append(end)

            if(end != "end" and start != "start"):

                if(end in adjacency_dict):
                    adjacency_dict[end].append(start)
                else:
                    adjacency_dict[end] = [start]
        else:
            adjacency_dict[start] = [end]

            if(end != "end" and start != "start"):

                if(end in adjacency_dict):
                    adjacency_dict[end].append(start)
                else:
                    adjacency_dict[end] = [start]

path_list = []

for small_cave in list(small_caves):
    visited_list = []
    traverse_graph("start", visited_list, path_list, adjacency_dict, small_cave)

print(len(path_list))
