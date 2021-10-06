import game
from Weathersim.nemethcsababence.Havaseso.HavasesoActors import *

class HavasesoStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.taj = taj()
        self.taj.width = 1280
        self.taj.height = 720
        self.taj.z_index = 2
        self.eg = szurkeeg()
        self.eg.width = 1920
        self.eg.height = 1300
        self.eg.z_index = 1
        self.ho = ho()
        self.ho.width = 200
        self.ho.height = 200
        self.ho.z_index = 3
        self.eso = eso()
        self.eso.width = 200
        self.eso.height = 100
        self.eso.x = 500
        self.eso.y = 300
        self.eso.z_index = 3
        self.add_actor(self.taj)
        self.add_actor(self.eg)
        self.add_actor(self.ho)
        self.add_actor(self.eso)