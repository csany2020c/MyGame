import pygame
import Weathersim.nemethcsababence.Eso.EsoScreen
from Weathersim.nemethcsababence.Menu.MenuActors import *
import game
from Weathersim.nemethcsababence.Eso.EsoScreen import *
from Weathersim.nemethcsababence.Havazas.HavazasScreen import *
from Weathersim.nemethcsababence.Havaseso.HavasesoScreen import HavasesoScreen
from Weathersim.nemethcsababence.Havaseso.HavasesoActors import *
from Weathersim.nemethcsababence.Napsutes.NapsutesScreen import *
from game.scene2d.MyScreen import *


class MenuStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.menu = MenuImage()
        self.add_actor(self.menu)
        self.menu.width = 1280
        self.menu.height = 720

        self.tajkep = tajkep()
        self.add_actor(self.tajkep)
        self.tajkep.width = 1280
        self.tajkep.height = 720
        self.tajkep.z_index = 1
        self.tajkep.x = 0
        self.tajkep.y = 0

        self.button1 = button1()
        self.add_actor(self.button1)
        self.button1.height = 97
        self.button1.width = 299
        self.button1.y = 408
        self.button1.x = 6

        self.button2 = button2()
        self.add_actor(self.button2)
        self.button2.height = 77
        self.button2.width = 297
        self.button2.y = 408
        self.button2.x = 330

        self.button3 = button3()
        self.add_actor(self.button3)
        self.button3.height = 97
        self.button3.width = 299
        self.button3.y = 408
        self.button3.x = 650

        self.button4 = button4()
        self.add_actor(self.button4)
        self.button4.height = 97
        self.button4.width = 297
        self.button4.y = 408
        self.button4.x = 973

        self.nap = menunap()
        self.add_actor(self.nap)
        self.nap.x = 875
        self.nap.y = -10
        self.nap.rotate_with(20)

        for i in range(30):
            self.eso = menueso()
            self.add_actor(self.eso)
            self.eso.y = random.Random().randint(100, 375)
            self.eso.x = random.Random().randint(10, 280)
            self.eso.width = 10
            self.eso.height = 20

        for i in range(30):
            self.eso2 = menueso2()
            self.add_actor(self.eso2)
            self.eso2.y = random.Random().randint(100, 375)
            self.eso2.x = random.Random().randint(650, 925)
            self.eso2.width = 10
            self.eso2.height = 20

        for i in range(30):
            self.ho = menuho()
            self.add_actor(self.ho)
            self.ho.y = random.Random().randint(100, 375)
            self.ho.x = random.Random().randint(650, 925)
            self.ho.width = 10
            self.ho.height = 20

        for i in range(30):
            self.ho2 = menuho2()
            self.add_actor(self.ho2)
            self.ho2.y = random.Random().randint(100, 375)
            self.ho2.x = random.Random().randint(325, 600)
            self.ho2.width = 10
            self.ho2.height = 20

        self.button1.set_on_mouse_down_listener(self.Klikk1)
        self.button2.set_on_mouse_down_listener(self.Klikk2)
        self.button3.set_on_mouse_down_listener(self.Klikk3)
        self.button4.set_on_mouse_down_listener(self.Klikk4)
        self.set_on_key_down_listener(self.key_down)

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

    def key_down(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()


class MenuScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0)
        self.add_stage(MenuStage())


