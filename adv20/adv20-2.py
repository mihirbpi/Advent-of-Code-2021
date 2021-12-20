from aocd import get_data
from collections import defaultdict
import copy

input = get_data(year=2021,day=20).split("\n\n")

def string_to_output_pixel(s, enhancement_algorithm):
    bin = ""

    for char in s:

        if(char == "#"):
            bin += "1"

        elif(char  == "."):
            bin += "0"

    return enhancement_algorithm[int(bin, 2)]

def get_output_pixel(position, image_dict, enhancement_algorithm):
    s = ""
    dirs = [ (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

    for i in range(0, len(dirs)):
        dir = dirs[i]
        s += image_dict[(position[0] + dir[0], position[1] + dir[1])]

    return string_to_output_pixel(s, enhancement_algorithm)

def enhance(image_dict, enhancement_algorithm, default_char):

    new_image_dict = defaultdict(lambda: default_char)

    rows = [key[0] for key in image_dict]
    cols = [key[1] for key in image_dict]

    min_row = min(rows)
    min_col = min(cols)
    max_row = max(rows)
    max_col = max(cols)

    for row in range(min_row-4, max_row+4):

        for col in range(min_col-4, max_col+4):

            new_image_dict[(row, col)] = get_output_pixel((row, col), image_dict, enhancement_algorithm)

    return new_image_dict

def count_light_pixels(image_dict):
    count = 0

    for val in image_dict.values():

        if(val == "#"):
            count += 1

    return count

def print_image(image_dict):
    rows = [key[0] for key in image_dict]
    cols = [key[1] for key in image_dict]

    min_row = min(rows)
    min_col = min(cols)
    max_row = max(rows)
    max_col = max(cols)

    for row in range(min_row-1, max_row+1):
        row_string = ""

        for col in range(min_col-1, max_col+1):
            row_string += image_dict[(row, col)]

        print(row_string)

enhancement_algorithm = input[0]
image_string_input = input[1]
image_array_input = image_string_input.split("\n")
image_dict = defaultdict(lambda: ".")

for i in range(0, len(image_array_input)):

    for j in range(0, len(image_array_input[0])):
        image_dict[(i,j)] = image_array_input[i][j]

for i in range(1, 51):

    if(i % 2 == 1):
        default_char = "#"
    else:
        default_char = "."

    image_dict = enhance(image_dict, enhancement_algorithm, default_char)

print(count_light_pixels(image_dict))
