from aocd import get_data

list = get_data(day=1).split("\n")

previous_measurement_sum = int(list[0]) + int(list[1]) + int(list[2])
count = 0

for i in range(1, len(list) - 2):
    sum = int(list[i]) + int(list[i+1]) + int(list[i+2])

    if(sum > previous_measurement_sum):
        count += 1
    previous_measurement_sum = sum

print(count)
