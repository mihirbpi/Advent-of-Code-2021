from aocd import get_data

input = get_data(year=2021,day=6).split("\n")
l0 = map(int, input[0].split(","))
l = []

class Fish:

    def __init__(self, bday, timer):
        self.bday = bday
        self.timer = timer
        self.can_create_bool = False

    def update_timer(self, day):
        if(day - self.bday >= 1):
            if(self.timer > 0):
                self.can_create_bool = False
                self.timer -= 1
            elif(self.timer == 0):
                self.can_create_bool = True
                self.timer = 6

    def can_create(self):
        return self.can_create_bool

day = 0

for num in l0:
    l.append(Fish(day, num))

while(day < 80):
    day += 1

    for fish in l:
        fish.update_timer(day)

    for fish in l:

        if(fish.can_create() == True):
            l.append(Fish(day, 8))

print(len(l))
