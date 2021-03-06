from aocd import get_data

input = get_data(year=2021,day=4).split("\n\n")
draws = input[0].split(",")
boards_input = map(lambda x: x.split("\n"), input[1:])

class Board:

    def __init__(self, board_input):
        self.board = board_input

    def mark(self, draw):
        for j in range(0, len(self.board)):

            for k in range(0, len(self.board[0])):

                if(self.board[j][k][0] == draw):
                    self.board[j][k][1] = True

    def get_score(self, draw):
        score = 0

        for j in range(0, len(self.board)):
            row = self.board[j]

            for x in row:

                if x[1] == False:
                    score += int(x[0])

        return score * int(draw)


    def has_won(self):

        for j in range(0, len(self.board)):
            bingo = True
            row = self.board[j]

            for x in row:

                if x[1] == False:
                    bingo = False

            if(bingo):
                return True

        for j in range(0, len(self.board[0])):
            bingo = True
            column = [x[j] for x in self.board]

            for x in column:

                if x[1] == False:
                    bingo = False

            if(bingo):
                return True

boards_list = []

for board_input in boards_input:

    for i in range (0, len(board_input)):
        split = board_input[i].split(" ")
        split = [x for x in split if x != ""]

        for j in range(0, len(split)):
            split[j] = [split[j], False]
        board_input[i] = split

    boards_list.append(Board(board_input))


board_wins = []
for draw in draws:

    for i in range(0, len(boards_list)):
        board = boards_list[i]
        board.mark(draw)

        if(i not in [x[0] for x in board_wins] and board.has_won()):
            board_wins.append([i, draw, board.get_score(draw)])

print(board_wins[-1][2])
