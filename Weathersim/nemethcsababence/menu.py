import Weathersim.nemethcsababence.Eso.EsoScreen
import game
from Weathersim.nemethcsababence.Eso.EsoScreen import *
from Weathersim.nemethcsababence.Havazas.HavazasScreen import *
from Weathersim.nemethcsababence.Havaseso.HavasesoScreen import *
from Weathersim.nemethcsababence.Napsutes.NapsutesScreen import *
from game.scene2d.MyScreen import *


class MenuStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.menu = MenuImage()
        self.add_actor(self.menu)
        self.menu.width = 1280
        self.menu.height = 720

        self.button1 = button1()
        self.add_actor(self.button1)
        self.button1.width = 125
        self.button1.height = 75
        self.button1.y = 500
        self.button1.x = 100

        self.button2 = button2()
        self.add_actor(self.button2)
        self.button2.width = 125
        self.button2.height = 75
        self.button2.y = 500
        self.button2.x = 400

        self.button3 = button3()
        self.add_actor(self.button3)
        self.button3.width = 125
        self.button3.height = 75
        self.button3.y = 500
        self.button3.x = 700

        self.button4 = button4()
        self.add_actor(self.button4)
        self.button4.width = 125
        self.button4.height = 75
        self.button4.y = 500
        self.button4.x = 1000

        self.button1.set_on_mouse_down_listener(self.Klikk1)
        self.button2.set_on_mouse_down_listener(self.Klikk2)
        self.button3.set_on_mouse_down_listener(self.Klikk3)
        self.button4.set_on_mouse_down_listener(self.Klikk4)

    def Klikk1(self, sender,event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.nemethcsababence.Eso.EsoScreen.EsoScreen())

    def Klikk2(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.nemethcsababence.Havazas.HavazasScreen.HavazasScreen())

    def Klikk3(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.nemethcsababence.Havaseso.HavasesoScreen.HavasesoScreen())

    def Klikk4(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.nemethcsababence.Napsutes.NapsutesScreen.NapsutesScreen())


class MenuScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(MenuStage())


