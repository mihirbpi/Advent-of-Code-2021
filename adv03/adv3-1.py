from aocd import get_data

list = get_data(year=2021,day=3).split("\n")
num_bits = len(list[0])
most_common = []
least_common = []

for i in range(0, num_bits):
    ith_pos_bits = [x[i] for x in list]
    least = min(ith_pos_bits ,key=lambda x: ith_pos_bits.count(x))
    most = max(ith_pos_bits,key=lambda x: ith_pos_bits.count(x))
    least_common.append(least)
    most_common.append(most)

gamma_rate = int("".join(most_common), base=2)
epsilon_rate = int("".join(least_common), base=2)
print(gamma_rate * epsilon_rate)
