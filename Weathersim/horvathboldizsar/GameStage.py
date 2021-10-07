import game
import random
from Weathersim.horvathboldizsar.GameActors import *


class NaposStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.erdo = erdo()
        self.erdo.z_index = 2
        self.add_actor(self.erdo)
        self.naposeg = naposeg()
        self.naposeg.z_index = 1
        self.add_actor(self.naposeg)
        self.nap = nap()
        self.nap.z_index = 3
        self.add_actor(self.nap)


class FelhosStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.erdo = erdo()
        self.erdo.z_index = 2
        self.add_actor(self.erdo)
        self.felhoseg = felhoseg()
        self.felhoseg.z_index = 1
        self.add_actor(self.felhoseg)


class EsosStage(game.scene2d.MyStage, ):
    def __init__(self):
        super().__init__()
        self.erdo = erdo()
        self.erdo.z_index = 2
        self.add_actor(self.erdo)
        self.felhoseg = felhoseg()
        self.felhoseg.z_index = 1
        self.add_actor(self.felhoseg)
        self.esocsepp = esocsepp()
        self.esocsepp.z_index = 3
        for x in range(0, 10):
            e = esocsepp()
            e.width = 30
            e.y = 0
            e.x = random.randint(0, 1280 - e.width)
            self.add_actor(e)

class HavasStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.erdo = erdo()
        self.erdo.z_index = 2
        self.add_actor(self.erdo)
        self.felhoseg = felhoseg()
        self.felhoseg.z_index = 1
        self.add_actor(self.felhoseg)
        self.hopehely = hopehely()
        self.hopehely.z_index = 3
        for j in range(0, 10):
            h = hopehely()
            h.width = 30
            h.height = 30
            h.y = 0
            h.x = random.randint(0, 1280 - h.width)
            self.add_actor(h)




