from HawkProductions.Font import *


class OverStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.F = Arial()
        self.add_actor(self.F)
        self.F.set_text("Game Over")
        self.F.set_color(204, 0, 0)
