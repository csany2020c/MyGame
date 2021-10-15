import game
import Weathersim.nemethcsababence.Menu.menu
import random

from Weathersim.nemethcsababence.Eso.EsoActors import windbag, felho
from Weathersim.nemethcsababence.Havaseso.HavasesoActors import *


class HavasesoStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.taj = havastaj()
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
            self.eso.width = random.Random().randint(20, 40)
            self.eso.height = random.Random().randint(20, 40)
            self.eso.z_index = 3
            self.ho = ho()
            self.add_actor(self.ho)
            self.ho.y = random.Random().randint(-50, 800)
            self.ho.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.eso.w)
            self.ho.width = 50
            self.ho.height = 50
            self.ho.z_index = 3

        self.button5 = button5()
        self.add_actor(self.button5)
        self.button5.width = 125
        self.button5.height = 75
        self.button5.y = 0
        self.button5.x = 0


        self.set_on_key_down_listener(self.nyom1)
        self.button5.set_on_mouse_down_listener(self.Klikk1)

    def Klikk1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.nemethcsababence.Menu.menu.MenuScreen())

    def nyom1(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            self.screen.game.set_screen(Weathersim.nemethcsababence.Menu.menu.MenuScreen())
