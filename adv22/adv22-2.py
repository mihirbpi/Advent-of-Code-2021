from aocd import get_data

input = get_data(year=2021,day=22).split("\n")
on_cubes = []
off_cubes = []
volume_on = 0

class Cube:

    def __init__(self, x_min, x_max, y_min, y_max, z_min, z_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.z_min = z_min
        self.z_max = z_max
        self.length = x_max - x_min + 1
        self.width = y_max - y_min + 1
        self.height = z_max - z_min + 1

    def volume(self):
        return self.length * self.width * self.height


def intersect(Cube1: Cube, Cube2: Cube):

    if(Cube1.x_max < Cube2.x_min or Cube2.x_max < Cube1.x_min):
        return None

    elif(Cube1.y_max < Cube2.y_min or Cube2.y_max < Cube1.y_min):
        return None

    elif(Cube1.z_max < Cube2.z_min or Cube2.z_max < Cube1.z_min):
        return None

    else:
        bound_x_min = max(Cube1.x_min, Cube2.x_min)
        bound_x_max = min(Cube1.x_max, Cube2.x_max)

        bound_y_min = max(Cube1.y_min, Cube2.y_min)
        bound_y_max = min(Cube1.y_max, Cube2.y_max)

        bound_z_min = max(Cube1.z_min, Cube2.z_min)
        bound_z_max = min(Cube1.z_max, Cube2.z_max)

        return Cube(bound_x_min, bound_x_max, bound_y_min, bound_y_max, bound_z_min, bound_z_max)


for line in input:

    instruction = int(line.split(" ")[0] == "on")

    x_coords, y_coords, z_coords = line.split(" ")[1].split(",")

    x_min = int(x_coords.split("=")[1].split("..")[0])
    x_max = int(x_coords.split("=")[1].split("..")[1])

    y_min = int(y_coords.split("=")[1].split("..")[0])
    y_max = int(y_coords.split("=")[1].split("..")[1])

    z_min = int(z_coords.split("=")[1].split("..")[0])
    z_max = int(z_coords.split("=")[1].split("..")[1])


    num_on = len(on_cubes)
    num_off = len(off_cubes)

    new_cube = Cube(x_min, x_max, y_min, y_max, z_min, z_max)

    if(instruction == 1):
        on_cubes.append(new_cube)
        volume_on += new_cube.volume()

    for i in range(num_on):
        intersect_cube = intersect(new_cube, on_cubes[i])

        if(intersect_cube != None):
            off_cubes.append(intersect_cube)
            volume_on -= intersect_cube.volume()

    for i in range(num_off):
        intersect_cube = intersect(new_cube, off_cubes[i])

        if(intersect_cube != None):
            on_cubes.append(intersect_cube)
            volume_on += intersect_cube.volume()


print(volume_on)
