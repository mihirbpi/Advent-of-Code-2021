from aocd import get_data
from collections import defaultdict

input = get_data(year=2021,day=5).split("\n")
grid_dict  = defaultdict(lambda: 0)

for i in range(0, len(input)):
    line = input[i]
    p1_string = line.split("->")[0].strip(" ")
    p2_string = line.split("->")[1].strip(" ")
    p1_x = int(p1_string.split(",")[0])
    p1_y = int(p1_string.split(",")[1])
    p2_x = int(p2_string.split(",")[0])
    p2_y = int(p2_string.split(",")[1])
    min_x = min(p1_x, p2_x)
    max_x = max(p1_x, p2_x)
    min_y = min(p1_y, p2_y)
    max_y = max(p1_y, p2_y)
    p1 = [p1_x, p1_y]
    p2 = [p2_x, p2_y]

    if(p1_y == p2_y):

        for x in range(min_x, max_x + 1):
            grid_dict[(x, p1_y)] += 1

    if(p1_x == p2_x):

        for y in range(min_y, max_y + 1):
            grid_dict[(p1_x, y)] += 1

count2_or_more_overlaps = 0

for item in grid_dict.items():

    if(item[1] >= 2):
        count2_or_more_overlaps += 1

print(count2_or_more_overlaps)
