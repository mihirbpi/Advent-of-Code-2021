from aocd import get_data
from collections import defaultdict

input = get_data(year=2021,day=25).split("\n")
cucumber_dict = defaultdict(lambda: ".")

for row in range(0, len(input)):

    for col in range(0, len(input[row])):
        cucumber_dict[(row, col)] = input[row][col]

def do_step(cucumber_dict):
    after_east_cucumber_dict =  defaultdict(lambda: ".")
    after_south_cucumber_dict = defaultdict(lambda: ".")
    east_facing_poses = []
    south_facing_poses = []
    east_moves = 0
    south_moves = 0

    for pos in cucumber_dict:
        after_east_cucumber_dict[pos] = cucumber_dict[pos]

        if (cucumber_dict[pos] == ">"):
            east_facing_poses.append(pos)

    for pos in east_facing_poses:
        adjacent_pos = (pos[0], (pos[1] + 1) % len(input[0]))

        if(cucumber_dict[adjacent_pos] == "."):
            east_moves += 1
            after_east_cucumber_dict[pos] = "."
            after_east_cucumber_dict[adjacent_pos] = ">"

    for pos in after_east_cucumber_dict:
        after_south_cucumber_dict[pos] = after_east_cucumber_dict[pos]

        if (after_east_cucumber_dict[pos] == "v"):
            south_facing_poses.append(pos)

    for pos in south_facing_poses:
            adjacent_pos = ((pos[0] + 1) % len(input), pos[1])

            if(after_east_cucumber_dict[adjacent_pos] == "."):
                south_moves += 1
                after_south_cucumber_dict[pos] = "."
                after_south_cucumber_dict[adjacent_pos] = "v"

    if(east_moves == 0 and south_moves == 0):
        return None

    return after_south_cucumber_dict


def print_cucumber_dict(cucumber_dict):

    for row in range(0, len(input)):
        print("".join([cucumber_dict[(row, col)] for col in range(0, len(input[0]))]))
    print("\n")

step = 0

while(True):
    step += 1
    result = do_step(cucumber_dict)

    if(result != None):
        cucumber_dict = result

    else:
        print(step)
        break
