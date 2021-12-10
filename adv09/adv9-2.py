from aocd import get_data
from collections import defaultdict
import numpy as np

input = get_data(year=2021,day=9).split("\n")

def is_low_pt(pt, height):
    i,j = list(pt)
    return min([height[(i,j+1)], height[(i+1,j)], height[(i-1,j)], height[(i,j-1)]]) > height[(i,j)]

def get_low_pts(pt, height, visited_list, low_pts_visited_list, low_pts):
    i,j = list(pt)
    visited_list.append(pt)

    if(pt in low_pts):
        low_pts_visited_list.append(pt)
        return

    else:
        around = [(i,j+1), (i+1,j), (i-1,j), (i,j-1)]

        for p in around:

            if(height[p] < 10 and height[p] < height[pt] and p not in visited_list):
                get_low_pts(p, height,  visited_list, low_pts_visited_list, low_pts)

height = defaultdict(lambda: 10)

for i in range(0, len(input)):

    for j in range(0, len(input[i])):
        height[(i,j)] = int(input[i][j].strip())

low_pts = [pt for pt in list(height.keys()) if is_low_pt(pt, height)]

basin_sizes = []

for i in range(0, len(low_pts)):
    low_pt = low_pts[i]
    count = 0

    for pt in list(height.keys()):
        low_pts_visited_list = []
        visited_list = []
        get_low_pts(pt, height, visited_list, low_pts_visited_list, low_pts)

        if(len(low_pts_visited_list) == 1 and low_pts_visited_list[0] == low_pt and height[pt] < 9):
            count += 1

    basin_sizes.append(count)

print(np.prod(sorted(basin_sizes)[-3:]))
