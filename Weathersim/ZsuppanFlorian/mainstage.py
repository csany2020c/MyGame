import pygame
from Weathersim.ZsuppanFlorian.mainactors import *



class NapStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.nap = nap()
        self.nap.z_index = 5
        self.eg = eg()
        self.eg.z_index = 4
        self.taj = taj()
        self.taj.z_index = 6
        self.add_actor(self.taj)
        self.add_actor(self.nap)
        self.add_actor(self.eg)


class HoStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.ho = ho()
        self.ho.z_index = 5
        self.eg = felhos()
        self.eg.z_index = 4
        self.taj = taj()
        self.taj.z_index = 6
        self.add_actor(self.taj)
        self.add_actor(self.ho)
        self.add_actor(self.eg)
class EsoStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.eso = eso()
        self.eso.z_index = 6
        self.eg = felhos()
        self.eg.z_index = 4
        self.taj = taj()
        self.taj.z_index = 5
        self.add_actor(self.taj)
        self.add_actor(self.eso)
        self.add_actor(self.eg)
        #self.t = MyTickTimer(interval=0.001, func=self.tikk)
        #self.add_timer(self.t)

class HavasesoStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.ho = ho()
        self.ho.z_index = 5
        self.eg = eg()
        self.eg.z_index = 4
        self.taj = taj()
        self.taj.z_index = 6
        self.eso = eso()
        self.eso.z_index = 6
        self.add_actor(self.taj)
        self.add_actor(self.ho)
        self.add_actor(self.eg)
        self.add_actor(self.eso)

        self.t = MyTickTimer(interval=0.001, func=self.tikk)
        self.add_timer(self.t)

    def tikk(self, sender):
        self.csepp = (eso())
        self.add_actor(self.csepp)
        self.csepp.x = random.Random().randint(-500, 1500)