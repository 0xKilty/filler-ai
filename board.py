import random

class Board():

    def __init__(self):
        self.board_data = []
        for i in range(7):
            self.board_data.append([9] * 8)

        self.board_ownership = []
        for i in range(7):
            self.board_ownership.append([0] * 8)
        self.board_ownership[6][0] = 1
        self.board_ownership[0][7] = 2
    
        self.player_1_touching = [(5, 0), (6, 1)]
        self.player_2_touching = [(1, 7), (0, 6)]

    def __str__(self):
        res = ""
        for i in range(7):
            for j in range(8):
                res += f"\033[{self.board_data[i][j] + 40}m  \033[00m"
            res += "\n"
        return res
    
    def get_neighboring_indexes(self, i, j):
        res = []
        if i > 0: res.append((i - 1, j))
        if i < 6: res.append((i + 1, j))
        if j > 0: res.append((i, j - 1))
        if j < 7: res.append((i, j + 1))
        return res
    
    def get_neighboring_colors(self, i, j):
        res = []
        for index in self.get_neighboring_indexes(i, j):
            res.append(self.board_data[index[0]][index[1]])
        return res

    def set_board(self):
        for i in range(7):
            for j in range(8):
                self.board_data[i][j] = random.randint(0, 6)
                while self.board_data[i][j] in self.get_neighboring_colors(i, j):
                    self.board_data[i][j] = random.randint(0, 6)    
        return self.board_data