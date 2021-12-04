from aocd import get_data

input = get_data(day=4).split("\n\n")

draws = input[0].split(",")
boards = input[1:]

def mark(num, boards_list, index):
        board = boards_list[index]
        for j in range(0, len(board)):
            for k in range(0, len(board[0])):
                if(board[j][k][0] == num):
                    board[j][k][1] = True

def get_score(num, boards_list, index):
    score = 0
    board = boards_list[index]
    for j in range(0, len(board)):
        row = board[j]
        for x in row:
            if x[1] == False:
                score += int(x[0])

    return score * int(num)



def is_win(boards_list, index):
    board = boards_list[index]

    for j in range(0, len(board)):
        bingo = True
        row = board[j]
        for x in row:
            if x[1] == False:
                bingo = False
        if(bingo):
            return i

    for j  in range(0, len(board[0])):
        bingo = True
        column = [x[j] for x in board]
        for x in column:
            if x[1] == False:
                bingo = False
        if(bingo):
            return i


boards_list = []
for board in boards:
    boards_list.append(board.split("\n"))

for board in boards_list:
    for i in range (0, len(board)):
        split = board[i].split(" ")
        split = [x for x in split if x != ""]
        for j in range(0, len(split)):
            split[j] = [split[j], False]
        board[i] = split


board_wins = []
for draw in draws:

    for i in range(0, len(boards_list)):
        mark(draw, boards_list, i)

        if (i not in [x[0] for x in board_wins] and is_win(boards_list, i)):
            board_wins.append([i, draw, get_score(draw, boards_list, i)])

print(board_wins[-1][2])
