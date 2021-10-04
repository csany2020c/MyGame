import game
from Weathersim.horvathboldizsar.GameActors import *

class GameStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.erdo = erdo()
        self.erdo.width = 1280
        self.erdo.height = 720
        self.add_actor(self.erdo)