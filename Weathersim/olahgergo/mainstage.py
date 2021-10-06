from Weathersim.olahgergo.actors import *


class MainStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        hk = hatterkep()
        hk.height = 720
        hk.width = 1280
        self.add_actor(actor=hk)


