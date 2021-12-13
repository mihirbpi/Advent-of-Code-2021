from aocd import get_data
from collections import defaultdict

input = get_data(year=2021,day=13).split("\n\n")

def fold(fold_instruct, paper_dict):
    axis = fold_instruct[0]
    value = fold_instruct[1]

    if(axis == "y"):
        above = [pt for pt in paper_dict if pt[1] <= value]

        for pt in above:
            refl_pt = (pt[0], value  + (value - pt[1]) )

            if(paper_dict[refl_pt] == 1):
                paper_dict[pt] = paper_dict[refl_pt]

            paper_dict[refl_pt] = 0

    elif(axis == "x"):
        left = [pt for pt in paper_dict if pt[0] <= value]

        for pt in left:
            refl_pt = (value  + (value - pt[0]), pt[1])

            if(paper_dict[refl_pt] == 1):
                paper_dict[pt] = paper_dict[refl_pt]

            paper_dict[refl_pt] = 0

def num_visible(paper_dict):
    return len([x for x in paper_dict if paper_dict[x] == 1])

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

fold(fold_list[0], paper_dict)
print(num_visible(paper_dict))
