import random

class Board:

    def __init__(self):
        self.board_data = []
        for i in range(7):
            self.board_data.append([0] * 8)

    def __str__(self):
        res = ""
        for i in range(7):
            for j in range(8):
                res += f"\033[{self.board_data[i][j] + 40}m  \033[00m"
            res += "\n"
        return res
    
    def get_neighboring_indexes(self, i, j):
        res = []
        if i > 0: res.append(i - 1)
        if i < 6: res.append(i + 1)
        if j > 0: res.append(j - 1)

    def set_board(self):
        for i in range(7):
            for j in range(8):
                self.board_data[i][j] = random.randint(0, 6)
                '''
                while (self.board_data[i][j] == self.board_data[i - 1][j] or
                       self.board_data[i][j] == self.board_data[i + 1][j] or
                       self.board_data[i][j] == self.board_data[i][j - 1] or
                       self.board_data[i][j] == self.board_data[i][j + 1]):
                    self.board_data[i][j] = random.randint(0, 6)
                '''

board = Board()
board.set_board()
print(board)