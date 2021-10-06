from Weathersim.nemethcsababence.Havazas.HavazasActors import *
import game
import random


class HavazasStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.taj = taj()
        self.taj.width = 1280
        self.taj.height = 720
        self.taj.z_index = 2
        self.szeg = szurkeeg()
        self.szeg.width = 1920
        self.szeg.height = 1300
        self.szeg.z_index = 1
        self.ho = ho()
        self.ho.width = 100
        self.ho.height = 100
        self.ho.z_index = 3
        self.add_actor(self.taj)
        self.add_actor(self.szeg)
        for i in range(30):
            self.ho = ho()
            self.add_actor(self.ho)
            self.ho.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.ho.w)
            self.ho.y = random.Random().randint(0, 720)