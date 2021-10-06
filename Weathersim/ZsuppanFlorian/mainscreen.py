from Weathersim.ZsuppanFlorian.mainstage import *
from Weathersim.ZsuppanFlorian.rainstage import *
from Weathersim.ZsuppanFlorian.snowstage import *


class MainScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(MainStage())
        self.add_stage(snowStage())
        self.add_stage(rainStage())
