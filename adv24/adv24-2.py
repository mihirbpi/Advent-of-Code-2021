from aocd import get_data
from itertools import product

input_space = product(range(1, 10, 1), repeat=7)
div_nums =  [1,1,1,26,26,1,26,26,1,1,26,1,26,26]
add_xnums = [12,13,13,-2,-10,13,-14,-5,15,15,-14,10,-14,-5]
add_ynums = [7,8,10,4,4,6,11,13,1,8,4,13,4,14]


def z_output(digit, z, div_num, add_xnum, addy_num):

    if(add_xnum > 0):
        return (None, 26*z + digit + addy_num)
    else:
        return ((z%26)+add_xnum, z // 26)

def get_program_output(test_digits_list, div_nums, add_xnums, add_ynums):

    true_digits = []
    z = 0
    index = 0

    for i in range(0, 14):

        if(add_xnums[i] > 0):
            result = z_output(test_digits_list[index], z, div_nums[i], add_xnums[i], add_ynums[i])
            z = result[1]
            true_digits.append(test_digits_list[index])
            index += 1
            index = index % 7

        else:
            result = z_output(test_digits_list[index], z, div_nums[i], add_xnums[i], add_ynums[i])
            z = result[1]
            true_digits.append(result[0])

            if not ( 1 <= result[0] <= 9):
                return None

    if(z == 0):
        return true_digits

    else:
        return None


for value in input_space:
    test_digits_list = list(value)
    result = get_program_output(test_digits_list, div_nums, add_xnums, add_ynums)

    if(result != None):
        print("".join([str(x) for x in result]))
        break
