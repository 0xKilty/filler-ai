from board import Board
from player import Player

class Game:
    def __init__(self):
        self.board = Board()
        self.board.set_board()

        self.player1 = Player(1)
        self.player2 = Player(2)

        self.ownership = []
        for _ in range(7):
            self.ownership.append([0] * 8)

    def make_turn(self, player: Player, color: int):
        pass
        '''
        for index in player.touching:
            if self.board.board_data[index[0], index[1]] == color:
        '''
                
    def get_move(self):
        for i in range(6):
            print(f"\033[{i + 40}m {i + 1} \033[00m", end="")
        print('\n')
        move = input("> ")

    def is_game_over(self) -> bool:
        return False

game = Game()
print(game.board)
game.get_move()
