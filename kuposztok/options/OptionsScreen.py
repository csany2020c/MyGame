import game
from kuposztok.options.OptionsStage import OptionsStage


class OptionsScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(r=0,g=0, b=0)
        self.add_stage(OptionsStage())