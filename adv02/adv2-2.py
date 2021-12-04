from aocd import get_data

list = get_data(year=2021,day=2).split("\n")
depth = 0
horiz = 0
aim = 0

for i in range(0, len(list)):
    split = list[i].split(" ")
    dir = split[0]
    amount = int(split[1])

    if (dir == "down"):
        aim += amount
    elif (dir == "up"):
        aim -= amount
    elif(dir == "forward"):
        horiz += amount
        depth += aim * amount

print(depth * horiz)
