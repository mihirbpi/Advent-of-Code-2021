from aocd import get_data
from collections import defaultdict

input = get_data(year=2021,day=6).split("\n")

input_fish = list(map(int, input[0].split(",")))
fish_of_each_age_dict = defaultdict(lambda:0)
num_days = 256

def update_fish_of_each_age(fish_of_each_age_dict):
    age0 = fish_of_each_age_dict[0]
    fish_of_each_age_dict[0] = fish_of_each_age_dict[1]
    fish_of_each_age_dict[1] = fish_of_each_age_dict[2]
    fish_of_each_age_dict[2] = fish_of_each_age_dict[3]
    fish_of_each_age_dict[3] = fish_of_each_age_dict[4]
    fish_of_each_age_dict[4] = fish_of_each_age_dict[5]
    fish_of_each_age_dict[5] = fish_of_each_age_dict[6]
    fish_of_each_age_dict[6] = fish_of_each_age_dict[7]+ age0
    fish_of_each_age_dict[7] = fish_of_each_age_dict[8]
    fish_of_each_age_dict[8] = age0

for fish in input_fish:
    fish_of_each_age_dict[fish] += 1

for day in range(1, num_days + 1):
    update_fish_of_each_age(fish_of_each_age_dict)

print(sum(item[1] for item in fish_of_each_age_dict.items()))
