from Weathersim.olahgergo.actors import *
from Weathersim.olahgergo.napscreen import *


class NapStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()

        nape = vilagoseg()
        nape.height = 720
        nape.width = 1280
        self.add_actor(actor=nape)

        nap = napnap()
        nap.height = 340
        nap.width = 760
        nap.set_x(167)
        nap.set_y(-69)
        self.add_actor(actor=nap)

        hk = hatterkep()
        hk.height = 720
        hk.width = 1280
        self.add_actor(actor=hk)





