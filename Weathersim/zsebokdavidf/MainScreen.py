from Weathersim.zsebokdavidf.MainStage import *
from Weathersim.zsebokdavidf.RainStage import *
from Weathersim.zsebokdavidf.SnowStage import *


class MainScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(r=0, b=50, g=0)
        self.add_stage(MainStage())
        self.add_stage(SnowStage())
        self.add_stage(RainStage())






