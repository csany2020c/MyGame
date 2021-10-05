import game
from Weathersim.KeleLorand.GameStage import *

class Screen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(Stage())