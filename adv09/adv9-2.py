from aocd import get_data
from collections import defaultdict
import numpy as np

input = get_data(year=2021,day=9).split("\n")

def is_low_pt(pt, height):
    i,j = list(pt)
    return min([height[(i,j+1)], height[(i+1,j)], height[(i-1,j)], height[(i,j-1)]]) > height[(i,j)]

def traverse_basin(pt, height, visited_list, basin_list):
    visited_list.append(pt)
    basin_list.append(pt)
    i,j = list(pt)
    around_pts = [(i,j+1), (i+1,j), (i-1,j), (i,j-1)]

    for p in around_pts:

        if(height[p] > height[pt] and height[p] < 9 and not p in visited_list):

            traverse_basin(p, height, visited_list, basin_list)

height = defaultdict(lambda: 10)

for i in range(0, len(input)):

    for j in range(0, len(input[i])):
        height[(i,j)] = int(input[i][j].strip())

low_pts = [pt for pt in list(height.keys()) if is_low_pt(pt, height)]

basin_sizes = []

for low_pt in low_pts:
    visited_list = []
    basin_list = []
    traverse_basin(low_pt, height, visited_list, basin_list)
    basin_sizes.append(len(basin_list))

print(np.prod(sorted(basin_sizes)[-3:]))
