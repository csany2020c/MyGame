import game
from Weathersim.zsebokdavidf.MainStage import MainStage


class MainScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(r=0, b=255, g=50)
        self.add_stage(MainStage())
