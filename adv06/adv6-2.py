from aocd import get_data
from collections import defaultdict

input = get_data(year=2021,day=6).split("\n")

input_fish = list(map(int, input[0].split(",")))
fish_birth_dict = defaultdict(lambda:0)
num_days = 256

def update_fish_born_on_day(input_fish, fish_birth_dict, curr_day):

    for fish in input_fish:

        if(curr_day % 7 == fish + 1):
            fish_birth_dict[curr_day] += 1

    for day in range(1, curr_day):

        if(curr_day - day - 8 - 1 >= 0 and (curr_day - day - 8 - 1) % 7 == 0):
            fish_birth_dict[curr_day] += fish_birth_dict[day]

for day in range(1, num_days + 1):
    update_fish_born_on_day(input_fish, fish_birth_dict, day)

total_fish = len(input_fish)

for day in range(1, num_days + 1):
    total_fish += fish_birth_dict[day]

print(total_fish)
