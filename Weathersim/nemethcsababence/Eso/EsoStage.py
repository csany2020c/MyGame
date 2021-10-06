from Weathersim.nemethcsababence.Eso.EsoActors import *
import random

class EsoStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.taj = taj()
        self.taj.width = 1280
        self.taj.height = 720
        self.taj.z_index = 2
        self.szurkeeg = szurkeeg()
        self.szurkeeg.width = 1920
        self.szurkeeg.height = 1300
        self.szurkeeg.z_index = 1
        self.add_actor(self.taj)
        for i in range(30):
            self.eso = eso()
            self.add_actor(self.eso)
            self.eso.y = random.Random().randint(-50, 800)
            self.eso.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.eso.w)
            self.eso.width = 50
            self.eso.height = 50
            self.eso.z_index = 3
        self.add_actor(self.szurkeeg)

