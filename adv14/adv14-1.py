from aocd import get_data

input = get_data(year=2021,day=14).split("\n\n")
template = [input[0]]
rules = input[1].split("\n")
rules_dict = {}

for r in rules:
    left = r.split(" -> ")[0]
    right = r.split(" -> ")[1]
    rules_dict[left] = right

def step(template):
    molecule = template[0]
    pairs = []

    for i in range(0, len(molecule) - 1):
        pair = molecule[i] + molecule[i + 1]
        pairs.append(pair)

    for i in range(0, len(pairs)):
        pairs[i] = pairs[i][0] + rules_dict[pairs[i]] + pairs[i][1]

    molecule = pairs[0]

    for i in range(1, len(pairs)):
        molecule += pairs[i][1:]

    template[0] = molecule

num_steps = 10

for i in range(1, num_steps + 1):
    step(template)

counts = [template[0].count(x) for x in template[0]]
min_amount = min(counts)
max_amount = max(counts)
print(max_amount - min_amount)
