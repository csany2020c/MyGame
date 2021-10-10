import Weathersim
from Weathersim.nemethcsababence.Eso.EsoActors import *
import Weathersim.nemethcsababence.Menu.menu
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
            self.eso.width = random.Random().randint(20, 50)
            self.eso.height = random.Random().randint(20, 50)
            self.eso.z_index = 3
        self.add_actor(self.szurkeeg)

        self.felho = felho()
        self.felho.width = 225
        self.felho.height = 125
        self.felho.z_index = 1
        self.felho.y = 50
        self.add_actor(self.felho)

        self.windbag = windbag()
        self.windbag.width = 225
        self.windbag.height = 125
        self.windbag.z_index = 1
        self.windbag.y = 450
        self.windbag.x = 1150
        self.add_actor(self.windbag)
        self.windbag.z_index = 4

        self.button1 = button5()
        self.add_actor(self.button1)
        self.button1.width = 125
        self.button1.height = 75
        self.button1.y = 0
        self.button1.x = 0
        self.button1.set_on_mouse_down_listener(self.Klikk1)

    def Klikk1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.nemethcsababence.Menu.menu.MenuScreen())

