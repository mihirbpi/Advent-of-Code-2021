from aocd import get_data
from collections import defaultdict
import numpy as np

input = get_data(year=2021,day=5).split("\n")
vent_map_dict  = defaultdict(lambda: 0)

for i in range(0, len(input)):
    line = input[i]
    p1_string = line.split("->")[0].strip(" ")
    p2_string = line.split("->")[1].strip(" ")
    p1_x, p1_y = map(int, p1_string.split(","))
    p2_x, p2_y = map(int, p2_string.split(","))

    if(p1_y == p2_y):

        for x in range(min(p1_x, p2_x), max(p1_x, p2_x) + 1):
            vent_map_dict[(x, p1_y)] += 1

    elif(p1_x == p2_x):

        for y in range(min(p1_y, p2_y), max(p1_y, p2_y) + 1):
            vent_map_dict[(p1_x, y)] += 1

    else:
        x = p1_x
        y = p1_y
        vent_map_dict[(x, y)] += 1

        while(x != p2_x and y != p2_y):
            x += np.sign(p2_x - p1_x)
            y += np.sign(p2_y - p1_y)
            vent_map_dict[(x, y)] += 1

vent_map_dict_list = list(vent_map_dict.items())
count2_or_more_overlaps = sum(map(lambda x: x[1] >= 2, vent_map_dict_list))
print(count2_or_more_overlaps)
