from aocd import get_data
from functools import lru_cache

input = get_data(year=2021,day=21).split("\n")
player_1_start_pos = int(input[0].split(" ")[-1])
player_2_start_pos = int(input[1].split(" ")[-1])

def get_next_pos(current_pos, increase):
    new_pos = current_pos
    new_pos += increase

    if (new_pos % 10 != 0):
        new_pos = new_pos % 10
    else:
        new_pos = 10

    return new_pos

@lru_cache(maxsize=None)
def find_outcomes(curr_player, playerpos, playerscore, num_wins1, num_wins2,  otherplayerpos, otherplayerscore):


    if(curr_player == 2 and playerscore >= 21):
        return 2, playerpos, playerscore, num_wins1, num_wins2 + 1, otherplayerpos, otherplayerscore

    elif(curr_player == 1 and playerscore >= 21):
        return 1, playerpos, playerscore, num_wins1 + 1, num_wins2, otherplayerpos, otherplayerscore

    elif(curr_player == 2):

        total_wins1_list = []
        total_wins2_list = []
        for r1 in range(1, 4):
            for r2 in range(1, 4):
                for r3 in range(1, 4):
                    r = r1+r2+r3
                    next_pos = get_next_pos(otherplayerpos, r)
                    outcomes = find_outcomes(1, next_pos, otherplayerscore + next_pos, num_wins1, num_wins2, playerpos, playerscore)
                    total_wins1_list.append(outcomes[3])
                    total_wins2_list.append(outcomes[4])


        total_wins1 = sum(total_wins1_list)
        total_wins2 = sum(total_wins2_list)

        return curr_player, playerpos, playerscore, total_wins1, total_wins2, otherplayerpos, otherplayerscore

    elif(curr_player == 1):

            total_wins1_list = []
            total_wins2_list = []

            for r1 in range(1, 4):

                for r2 in range(1, 4):

                    for r3 in range(1, 4):
                        r = r1+r2+r3
                        next_pos = get_next_pos(otherplayerpos, r)
                        outcomes = find_outcomes(2, next_pos, otherplayerscore + next_pos, num_wins1, num_wins2, playerpos, playerscore)
                        total_wins1_list.append(outcomes[3])
                        total_wins2_list.append(outcomes[4])


            total_wins1 = sum(total_wins1_list)
            total_wins2 = sum(total_wins2_list)

            return curr_player, playerpos, playerscore, total_wins1, total_wins2, otherplayerpos, otherplayerscore

    elif(curr_player == None):

            total_wins1_list = []
            total_wins2_list = []

            for r1 in range(1, 4):

                for r2 in range(1, 4):

                    for r3 in range(1, 4):
                        r = r1+r2+r3
                        next_pos = get_next_pos(playerpos, r)
                        outcomes = find_outcomes(1, next_pos, playerscore + next_pos, num_wins1, num_wins2, otherplayerpos, otherplayerscore)
                        total_wins1_list.append(outcomes[3])
                        total_wins2_list.append(outcomes[4])


            total_wins1 = sum(total_wins1_list)
            total_wins2 = sum(total_wins2_list)

            return curr_player, playerpos, playerscore, total_wins1, total_wins2, otherplayerpos, otherplayerscore

print(find_outcomes(None, player_1_start_pos, 0, 0, 0, player_2_start_pos, 0))
