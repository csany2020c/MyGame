import game
from Weathersim.nemethcsababence.Eso.EsoScreen import *
from Weathersim.nemethcsababence.Havazas.HavazasScreen import *
from Weathersim.nemethcsababence.Havaseso.HavasesoScreen import *
from Weathersim.nemethcsababence.Napsutes.NapsutesScreen import *
from game.scene2d.MyScreen import *


class MenuStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.taj = taj()
        self.taj.width = 1280
        self.taj.height = 720
        self.taj.z_index = 3
        self.eg = kekeg()
        self.eg.width = 1920
        self.eg.height = 1300
        self.eg.z_index = 1
        self.nap = nap()
        self.nap.width = 400
        self.nap.height = 400
        self.nap.y = -100
        self.nap.x = 500
        self.nap.z_index = 2
        self.add_actor(self.taj)
        self.add_actor(self.eg)
        self.add_actor(self.nap)


class MenuScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(MenuStage())


