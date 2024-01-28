from board import Board
from player import Player

class Game:
    def __init__(self):
        self.board = Board()
        self.ownership = []
        for _ in range(7):
            self.ownership.append([0] * 8)

    def make_turn(self, player: Player, color: int):
        for index in player.touching:
            if self.board.board_data[index[0], index[1]] == color:
                

    def is_game_over(self) -> bool:
        return False