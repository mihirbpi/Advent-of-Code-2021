from aocd import get_data
from collections import defaultdict

input = get_data(year=2021,day=22).split("\n")
reactor_cubes_dict = defaultdict(lambda: 0)


for line in input:
    instruction = int(line.split(" ")[0] == "on")

    x_coords, y_coords, z_coords = line.split(" ")[1].split(",")

    x_min = int(x_coords.split("=")[1].split("..")[0])
    x_max = int(x_coords.split("=")[1].split("..")[1])

    y_min = int(y_coords.split("=")[1].split("..")[0])
    y_max = int(y_coords.split("=")[1].split("..")[1])

    z_min = int(z_coords.split("=")[1].split("..")[0])
    z_max = int(z_coords.split("=")[1].split("..")[1])

    if(not( (x_min > 50 or x_max < -50) or (y_min > 50 or y_max < -50) or (z_min > 50 or z_max < -50) )):

        for x in range(x_min, x_max + 1):

            for y in range(y_min, y_max + 1):

                for z in range(z_min, z_max + 1):

                    if(x >= -50 and x <= 50 and y >= -50 and y <= 50 and z >= -50 and z <= 50):
                        reactor_cubes_dict[(x,y,z)] = instruction

count = 0
for cube in reactor_cubes_dict:

    if(reactor_cubes_dict[cube] == 1):

        if(x >= -50 and x <= 50 and y >= -50 and y <= 50 and z >= -50 and z <= 50):
            count += 1
print(count)
