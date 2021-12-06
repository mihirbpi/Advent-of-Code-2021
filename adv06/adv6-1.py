from aocd import get_data

input = get_data(year=2021,day=6).split("\n")
input_fish = map(int, input[0].split(","))
fish_list = []
num_days = 80

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

for timer in input_fish:
    fish_list.append(Fish(day, timer))

while(day < num_days):
    day += 1

    for fish in fish_list:
        fish.update_timer(day)

    for fish in fish_list:

        if(fish.can_create() == True):
            fish_list.append(Fish(day, 8))

print(len(fish_list))
