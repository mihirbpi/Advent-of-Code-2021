from aocd import get_data
from collections import defaultdict

input = get_data(year=2021,day=13).split("\n\n")

def fold(fold_instruct, paper_dict):
    axis = fold_instruct[0]
    value = fold_instruct[1]

    max_x = max([pt[0] for pt in paper_dict if paper_dict[pt] == 1])
    max_y = max([pt[1] for pt in paper_dict if paper_dict[pt] == 1])

    paper_list = []

    for i in range(0, max_x + 1):

        for j in range(0, max_y + 1):
            paper_list.append((i,j))

    if(axis == "y"):
        above = [pt for pt in paper_list if pt[1] <= value]
        below = [pt for pt in paper_list if pt[1] > value]

        for pt in above:
            refl_pt = (pt[0], value  + (value - pt[1]) )

            if(paper_dict[refl_pt] == 1):
                paper_dict[pt] = paper_dict[refl_pt]
            paper_dict[refl_pt] = 0

        for pt in below:
            paper_dict[pt] = 0

    elif(axis == "x"):
        left = [pt for pt in paper_list if pt[0] <= value]
        right = [pt for pt in paper_list if pt[0] > value]

        for pt in left:
            refl_pt = (value  + (value - pt[0]), pt[1])

            if(paper_dict[refl_pt] == 1):
                paper_dict[pt] = paper_dict[refl_pt]
            paper_dict[refl_pt] = 0

        for pt in right:
            paper_dict[pt] = 0

def num_visible(paper_dict):
    return len([x for x in paper_dict if paper_dict[x] == 1])

def display_image(paper_dict):
    max_x = max([pt[0] for pt in paper_dict if paper_dict[pt] == 1])
    max_y = max([pt[1] for pt in paper_dict if paper_dict[pt] == 1])

    grid = [ ["." for i in range(0, max_x + 1)] for j in range(0, max_y + 1)]

    points = [pt for pt in paper_dict]

    for pt in points:
        if(paper_dict[pt] == 1):
            grid[pt[1]][pt[0]] = "▫️"

    for list in grid:
        print("".join(list))
    print("\n")


paper_dict = defaultdict(lambda: 0)
fold_list = []
dot_coords_input = input[0].split("\n")
fold_input = input[1].split("\n")

for line in dot_coords_input:
    x = int(line.split(",")[0])
    y = int(line.split(",")[1])
    paper_dict[(x, y)] = 1

for line in fold_input:
    axis = line.split("=")[0][-1]
    value = int(line.split("=")[1])
    fold_list.append((axis, value))

for fold_instruct in fold_list:
    fold(fold_instruct, paper_dict)

display_image(paper_dict)
