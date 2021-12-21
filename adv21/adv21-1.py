from aocd import get_data

input = get_data(year=2021,day=21).split("\n")
player_1_start_pos = int(input[0].split(" ")[-1])
player_2_start_pos = int(input[1].split(" ")[-1])


class DeterministicDice:

    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_num = 1
        self.num_rolls = 0

    def roll(self):
        old_num = self.current_num
        self.current_num += 1

        if(self.current_num % self.num_sides != 0):
            self.current_num = self.current_num % self.num_sides
        else:
            self.current_num = self.num_sides

        self.num_rolls += 1
        return old_num

class Player:

    def __init__(self, start_pos):
        self.pos = start_pos
        self.score = 0

    def play_turn(self, dice):
        roll_1 = dice.roll()
        roll_2 = dice.roll()
        roll_3 = dice.roll()
        self.pos += roll_1 + roll_2 + roll_3

        if (self.pos % 10 != 0):
            self.pos = self.pos % 10
        else:
            self.pos = 10

        self.score += self.pos

    def has_won(self):
        return self.score >= 1000



Player_1 = Player(player_1_start_pos)
Player_2 = Player(player_2_start_pos)
Dice = DeterministicDice(100)

while(True):
    Player_1.play_turn(Dice)

    if(Player_1.has_won()):
        print(Dice.num_rolls * Player_2.score)
        break

    Player_2.play_turn(Dice)

    if(Player_2.has_won()):
        print(Dice.num_rolls * Player_1.score)
        break
