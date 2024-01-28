from game import Game
from player import Player
import gymnasium as gym

class Agent(gym.Env):
    def __init__(self, player_num: int):
        self.game = Game()
        self.player = Player()
        self.action_space = gym.spaces.Discrete(4)

        # Our observation space conatins both arrays (color, ownership)
        self.observation_space = gym.spaces.Tuple(
            gym.spaces.Tuple(
                gym.spaces.Discrete(len(self.game.board)),
                gym.spaces.Discrete(len(self.game.board[0]))),
            gym.spaces.Tuple(
                gym.spaces.Discrete(len(self.game.board)),
                gym.spaces.Discrete(len(self.game.board[0]))))

    
    def reset(self):
        self.game = Game()

    def step(self, action: int):
        old_score = self.player.get_score()
        colors, ownership = self.game.make_turn(self.player_num, action)
        reward = self.player.get_score() - old_score
        done = self.game.is_game_over()
        return old_score, colors, ownership, reward, done, {}, {}



