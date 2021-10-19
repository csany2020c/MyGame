from HawkProductions.over.OverStage import *


class OverScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 204)
        self.add_stage(OverStage())


"""class OverGame(game.scene2d.MyGame):
    def __init__(self):
        super().__init__()
        self.screen = OverScreen()"""


#OverGame().run()
