from Weathersim.nemethcsababence.Eso.EsoActors import *


class EsoStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.taj = taj()
        self.taj.width = 1280
        self.taj.height = 720
        self.taj.z_index = 3
        self.szurkeeg = szurkeeg()
        self.szurkeeg.width = 1920
        self.szurkeeg.height = 1300
        self.szurkeeg.z_index = 1
        self.eso = eso()
        self.eso.width = 400
        self.eso.height = 400
        self.eso.y = -130
        self.eso.x = 500
        self.eso.z_index = 2
        self.add_actor(self.taj)
        self.add_actor(self.eso)
        self.add_actor(self.szurkeeg)
