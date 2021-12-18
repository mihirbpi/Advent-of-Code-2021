from aocd import get_data
import json
import re

input = get_data(year=2021,day=18).split("\n")
pattern_explode = re.compile(r"\[\d+,\d+\]")
pattern_number = re.compile(r"\d+")

def get_depth(index, line):
    depth = 0

    for i in range(0, index):

        if(line[i] == "["):
            depth += 1

        elif(line[i] == "]"):
            depth -= 1
    return depth

def can_explode(line, pattern_explode, pattern_number):
    explode_matches = re.finditer(pattern_explode, line)
    number_matches = re.finditer(pattern_number, line)

    for match in explode_matches:
        pre_pair = line[0:match.span()[0]]
        post_pair = line[match.span()[1]:]

        non_cancelled_openers = pre_pair.count('[') - pre_pair.count(']')
        non_cancelled_closers = post_pair.count(']') - post_pair.count('[')

        if(non_cancelled_closers >= 4 and non_cancelled_openers >= 4):
            return True

    return False

def can_split(line, pattern_explode, pattern_number):
    explode_matches = re.finditer(pattern_explode, line)
    number_matches = re.finditer(pattern_number, line)

    for match in number_matches:

        if(int(line[match.span()[0]:match.span()[1]]) >= 10):
            return True
    return False

def reduce(line, pattern_explode, pattern_number):
    #print(line, can_explode(line, pattern_explode, pattern_number), can_split(line, pattern_explode, pattern_number))
    explode_matches = re.finditer(pattern_explode, line)
    number_matches = re.finditer(pattern_number, line)
    return_string = line
    exploded = False
    splitted = False

    if(can_explode(return_string, pattern_explode, pattern_number)):

        for match in explode_matches:

            if(not exploded and get_depth(match.span()[0], return_string) == 4):
                exploded = True
                w = return_string[match.span()[0]:match.span()[1]]
                left = int(w[1:-1].split(",")[0])
                right = int(w[1:-1].split(",")[1])
                left_digit_indices = None
                right_digit_indices = None

                for m in number_matches:

                    if(m.span()[1] < match.span()[0]):
                        left_digit_indices = m.span()

                    if(m.span()[0] >= match.span()[1] and right_digit_indices == None):
                        right_digit_indices = m.span()

                new_return_string = ""

                for i in range(0, len(return_string)):

                    if(i < match.span()[0]):

                        if(left_digit_indices != None and i == left_digit_indices[0]):
                            original_int = int(return_string[left_digit_indices[0]:left_digit_indices[1]])
                            new_return_string += str(original_int + left)
                        elif(left_digit_indices != None and i > left_digit_indices[0] and i < left_digit_indices[1] ):
                            new_return_string += ""
                        else:
                            new_return_string += return_string[i]

                    elif( i == match.span()[0]):
                        new_return_string += "0"

                    elif(i > match.span()[0] and i < match.span()[1]):
                        new_return_string += ""

                    elif(i >= match.span()[1]):

                        if(right_digit_indices != None and i == right_digit_indices[0]):
                            original_int = int(return_string[right_digit_indices[0]:right_digit_indices[1]])
                            new_return_string += str(original_int + right)
                        elif(right_digit_indices != None and i > right_digit_indices[0] and i < right_digit_indices[1] ):
                            new_return_string += ""

                        else:
                            new_return_string += return_string[i]
                    else:
                        new_return_string += return_string[i]

                if(new_return_string != return_string):
                    return_string = new_return_string
                    return reduce(return_string, pattern_explode, pattern_number)

                return return_string

    else:
        if(can_split(return_string, pattern_explode, pattern_number)):
            split_match = None

            for match in number_matches:

                if(int(return_string[match.span()[0]:match.span()[1]]) >= 10):
                    split_match = match
                    break

            if(split_match != None):
                splitted = True
                new_return_string = ""

                for i in range(0, len(return_string)):

                    if(i < split_match.span()[0] or i >= split_match.span()[1]):
                        new_return_string += return_string[i]

                    elif(i == split_match.span()[0]):
                        number = int(return_string[match.span()[0]:match.span()[1]])
                        new_return_string += "[" + str(number//2) + "," + str((number+1)//2) + "]"

                if(new_return_string != return_string):
                    return_string = new_return_string
                    return reduce(return_string, pattern_explode, pattern_number)

                return return_string
        else:
            return return_string


def add(snailfishstring1, snailfishstring2, pattern_explode, pattern_number):
    add_string = "[" + snailfishstring1 + "," + snailfishstring2 + "]"
    reduced_add_string = reduce(add_string, pattern_explode, pattern_number)
    return reduced_add_string

def my_magnitude(snailfishlist):

    if(isinstance(snailfishlist, int)):
        return snailfishlist
    else:
        return 3*my_magnitude(snailfishlist[0]) + 2*my_magnitude(snailfishlist[1])

curr_sum = input[0]

for i in range(1, len(input)):
    curr_sum = add(curr_sum, input[i], pattern_explode, pattern_number)

print(my_magnitude(json.loads(curr_sum)))
