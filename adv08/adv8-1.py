from aocd import get_data

input = get_data(year=2021,day=8).split("\n")
count =  sum([len([digit for digit in line.strip("\n").split(" | ")[1].split(" ") if len(digit) in [2,4,3,7]]) for line in input])
print(count)
