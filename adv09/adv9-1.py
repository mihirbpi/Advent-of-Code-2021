from aocd import get_data
from collections import defaultdict

input = get_data(year=2021,day=9).split("\n")

def is_low_pt(pt, height):
    i,j = list(pt)
    return min([height[(i,j+1)], height[(i+1,j)], height[(i-1,j)], height[(i,j-1)]]) > height[(i,j)]

height = defaultdict(lambda: 10)

for i in range(0, len(input)):

    for j in range(0, len(input[i])):
        height[(i,j)] = int(input[i][j].strip())

print(sum([1 + height[pt] for pt in list(height.keys()) if is_low_pt(pt, height)]))
