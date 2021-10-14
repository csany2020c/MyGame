import pygame
import game
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
        self.felhos = felhos()
        self.felhos.z_index = 4
        self.taj = taj()
        self.taj.z_index = 6
        self.add_actor(self.taj)
        self.add_actor(self.felhos)
        for x in range(0, random.randint(100, 180)):
            s = ho()
            s.y = random.randint(-500, 300)
            s.x = random.randint(30, 1280) - s.width
            self.add_actor(ho)


class EsoStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.eso = eso()
        self.eso.z_index = 6
        self.felhos = felhos()
        self.felhos.z_index = 4
        self.taj = taj()
        self.taj.z_index = 5
        self.add_actor(self.taj)
        self.add_actor(self.felhos)
        for x in range(0, random.randint(100, 190)):
            r = eso()
            r.y = random.randint(-500, 200)
            r.x = random.randint(30, 1280) - r.width
            self.add_actor(eso)


class HavasesoStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.ho = ho()
        self.ho.z_index = 5
        self.felhos = felhos()
        self.felhos.z_index = 4
        self.taj = taj()
        self.taj.z_index = 6
        self.eso = eso()
        self.eso.z_index = 6
        self.add_actor(self.taj)
        self.add_actor(self.felhos)
        for x in range(0, random.randint(100, 190)):
            r = eso()
            r.y = random.randint(-500, 200)
            r.x = random.randint(30, 1280) - r.width
            self.add_actor(eso)
        for i in range(0, random.randint(100, 190)):
            s = ho()
            s.y = random.randint(-500, 200)
            s.x = random.randint(30, 1280) - s.width
            self.add_actor(ho)