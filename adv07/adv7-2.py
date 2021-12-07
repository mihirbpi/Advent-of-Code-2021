from aocd import get_data

input = get_data(year=2021,day=7).split("\n")
pos_list = list(map(int, input[0].split(",")))
fuel_list = [ sum([int(abs(x-y)*(abs(x-y) + 1) / 2) for y in pos_list]) for x in range(0, max(pos_list) + 1)]
print(min(fuel_list))
