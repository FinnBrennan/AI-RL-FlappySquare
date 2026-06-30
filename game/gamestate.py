import pygame as pyg
import gamelogic as gl

# Game State


class Gamestate:
    """Extrapolate gamestate logic from main game, as a gymnasium for the ai model"""

    def __init__(self):
        self.towers = []
        self.frame_count = 0
        self.square = gl.Square()
        self.score = 0
        self.game_active = True


# Instance owned state is a requiremenet because it allows you to create multiple instances
#  of the game running at a time holding multiple variables with different values.
# You can use these instances to be called by a management class which can keep track of each game instance.
