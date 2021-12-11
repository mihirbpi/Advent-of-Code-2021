from aocd import get_data
from collections import defaultdict

input = get_data(year=2021,day=11).split("\n")

def flash(octopus_dict, octopus, already_flashed, num_flashes):

    if(not octopus in already_flashed):
        i,j = list(octopus)
        already_flashed.append(octopus)
        num_flashes[0] += 1
        around = [(i-1, j-1), (i-1, j), (i-1,j+1), (i,j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1) ]

        for other_octopus in around:

                if(octopus_dict[other_octopus] >= 0):
                    octopus_dict[other_octopus] += 1

                if(octopus_dict[other_octopus] > 9):
                        flash(octopus_dict, other_octopus, already_flashed, num_flashes)

def do_step(octopus_dict, num_flashes):

    for octopus in [oct for oct in list(octopus_dict.keys()) if octopus_dict[oct] != -1]:
        octopus_dict[octopus] += 1

    already_flashed = []

    for octopus in [oct for oct in list(octopus_dict.keys()) if octopus_dict[oct] != -1]:

        if(octopus_dict[octopus] > 9):
            flash(octopus_dict, octopus, already_flashed, num_flashes)

    for oct in already_flashed:
        octopus_dict[oct] = 0

def print_octopuses(octopus_dict, input):

    for i in range(0, len(input)):

        print("".join([ str(octopus_dict[(i,j)]) for j in range(0, len(input[i]))]))
    print("\n")

octopus_dict = defaultdict(lambda: -1)

for i in range(0, len(input)):

    for j in range(0, len(input[i])):
        octopus_dict[(i,j)] = int(input[i][j].strip())

num_steps = 100
num_flashes = [0]

for step in range(1, num_steps + 1):
    print_octopuses(octopus_dict, input)
    do_step(octopus_dict, num_flashes)

print(num_flashes[0])
