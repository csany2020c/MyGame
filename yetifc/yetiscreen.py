import game
from yetistage import MenuStage

class MenuScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(MenuStage())


