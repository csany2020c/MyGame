import game
from Weathersim.horvathboldizsar.GameStage import *

class GameScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(HavasStage())

# class GameScreen2(game.scene2d.MyScreen):
#
#     def __init__(self):
#         super().__init__()
#         self.add_stage(FelhosStage())


