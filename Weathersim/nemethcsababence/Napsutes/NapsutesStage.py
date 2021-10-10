import Weathersim.nemethcsababence.Menu.menu
from Weathersim.nemethcsababence.Napsutes.NapsutesActors import *


class NapsutesStage(game.scene2d.MyStage):

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
