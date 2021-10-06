import game
from HawkProductions.MenuStage import*


class MenuScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(0, 128, 0)
        self.add_stage(MenuStage())
