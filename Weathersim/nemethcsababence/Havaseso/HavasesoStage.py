import game
import random
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
        self.add_actor(self.taj)
        self.add_actor(self.eg)
        for i in range(40):
            self.eso = eso()
            self.add_actor(self.eso)
            self.eso.y = random.Random().randint(-50, 800)
            self.eso.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.eso.w)
            self.eso.width = 50
            self.eso.height = 50
            self.eso.z_index = 3
            self.ho = ho()
            self.add_actor(self.ho)
            self.ho.y = random.Random().randint(-50, 800)
            self.ho.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.eso.w)
            self.ho.width = 50
            self.ho.height = 50
            self.ho.z_index = 3