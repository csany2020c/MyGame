import game
from Nike.NikeStage import*

class NikeScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(200, 100, 22)
        self.add_stage(NikeStage())


