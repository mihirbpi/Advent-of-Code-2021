from aocd import get_data
from collections import defaultdict
import copy

input = get_data(year=2021,day=14).split("\n\n")
template = input[0]
rules = input[1].split("\n")
rules_dict = {}
pair_freq_dict = defaultdict(lambda: 0)

for r in rules:
    left = r.split(" -> ")[0]
    right = r.split(" -> ")[1]
    rules_dict[left] = right

for i in range(0, len(template) - 1):
    pair_freq_dict[template[i] + template[i+1]] += 1

def step(pair_freq_dict, rules_dict):

    new_dict = copy.copy(pair_freq_dict)

    for key in pair_freq_dict:
        num = pair_freq_dict[key]
        new_dict[key] -= num
        new_dict[key[0] + rules_dict[key]] += num
        new_dict[rules_dict[key] + key[1]] += num

    return new_dict

num_steps = 40

for i in range(1, num_steps + 1):
    pair_freq_dict = step(pair_freq_dict, rules_dict)

count_letters = defaultdict(lambda: 0)

for key in pair_freq_dict:
    count_letters[key[0]] += pair_freq_dict[key]
    count_letters[key[1]] += pair_freq_dict[key]

count_letters [template[0]] += 1
count_letters [template[-1]] += 1
count_values = [ val //2 for val in count_letters.values()]
print(max(count_values) - min(count_values))
