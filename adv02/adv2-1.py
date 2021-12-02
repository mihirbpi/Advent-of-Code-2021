from aocd import get_data

list = get_data(day=2).split("\n")
depth = 0
horiz = 0

for i in range(0, len(list)):
    split = list[i].split(" ")
    dir = split[0]
    amount = int(split[1])

    if (dir == "down"):
        depth += amount
    elif (dir == "up"):
        depth -= amount
    elif(dir == "forward"):
        horiz += amount

print(depth * horiz)
