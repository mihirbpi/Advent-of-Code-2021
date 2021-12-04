from aocd import get_data

input = get_data(day=4).split("\n\n")
draws = input[0].split(",")
boards = input[1:]

def mark(num, boards_list):
    for i in range(0, len(boards_list)):
        for j in range(0, len(boards_list[0])):
            for k in range(0, len(boards_list[0][0])):
                if(boards_list[i][j][k][0] == num):
                    boards_list[i][j][k][1] = True

def get_score(num, board):
    score = 0
    for j in range(0, len(board)):
        row = board[j]
        for x in row:
            if x[1] == False:
                score += int(x[0])

    return score * int(num)


def is_bingo(boards_list):
    for i in range(0, len(boards_list)):
        board = boards_list[i]

        for j in range(0, len(board)):
            bingo = True
            row = board[j]
            for x in row:
                if x[1] == False:
                    bingo = False
            if(bingo):
                return i

        for j in range(0, len(board[0])):
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

for draw in draws:
    mark(draw, boards_list)
    result = is_bingo(boards_list)

    if(result != None):
        win_board = boards_list[result]
        print(get_score(draw, win_board))
        break
