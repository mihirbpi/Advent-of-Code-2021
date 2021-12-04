from aocd import get_data

list = get_data(year=2021,day=1).split("\n")

previous_measurement = list[0]
count = 0

for i in range(1, len(list)):

    if(int(list[i]) > int(previous_measurement)):
        count += 1
    previous_measurement = list[i]

print(count)
