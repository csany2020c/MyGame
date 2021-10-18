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
        for i in range(0, random.randint(20, 200)):
            s = ho()
            s.y = random.randint(-500, 300)
            s.x = random.randint(50, 1280) - s.width
            self.add_actor(s)


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
        for i in range(0, random.randint(20, 200)):
            r = eso()
            r.y = random.randint(-500, 200)
            r.x = random.randint(50, 1280) - r.width
            self.add_actor(r)


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
        for i in range(0, random.randint(20, 200)):
            r = eso()
            r.y = random.randint(-500, 200)
            r.x = random.randint(50, 1280) - r.width
            self.add_actor(r)
        for k in range(0, random.randint(20, 200)):
            s = ho()
            s.y = random.randint(-500, 200)
            s.x = random.randint(50, 1280) - s.width
            self.add_actor(s)


class HavasesoNaposStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.nap = nap()
        self.nap.z_index = 5
        self.ho = ho()
        self.ho.z_index = 6
        self.felhos = felhos()
        self.felhos.z_index = 4
        self.taj = taj()
        self.taj.z_index = 7
        self.eso = eso()
        self.eso.z_index = 6
        self.add_actor(self.taj)
        self.add_actor(self.felhos)
        self.add_actor(self.nap)
        for i in range(0, random.randint(20, 100)):
            r = eso()
            r.y = random.randint(-500, 100)
            r.x = random.randint(10, 1280) - r.width
            self.add_actor(r)
        for k in range(0, random.randint(20, 100)):
            s = ho()
            s.y = random.randint(-500, 200)
            s.x = random.randint(10, 1280) - s.width
            self.add_actor(s)

class InfoStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.infohatter = InfoHatter()
        self.i1 = Info1()
        self.i2 = Info2()
        self.i3 = Info3()
        self.i4 = Info4()

        self.infohatter.y = 0
        self.i1.y = 20
        self.i2.y = 100
        self.i3.y = 200
        self.i4.y = 300

        self.add_actor(self.infohatter)
        self.add_actor(self.i1)
        self.add_actor(self.i2)
        self.add_actor(self.i3)
        self.add_actor(self.i4)



