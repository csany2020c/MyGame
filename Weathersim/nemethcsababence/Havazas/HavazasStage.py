import Weathersim.nemethcsababence.Menu.menu
from Weathersim.nemethcsababence.Havazas.HavazasActors import *
import pygame
import game
import random


class HavazasStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.taj = havastaj()
        self.taj.width = 1280
        self.taj.height = 720
        self.taj.z_index = 2
        self.szeg = szurkeeg()
        self.szeg.width = 1920
        self.szeg.height = 1300
        self.szeg.z_index = 1
        self.add_actor(self.taj)
        self.add_actor(self.szeg)
        for i in range(30):
            self.ho = ho()
            self.add_actor(self.ho)
            self.ho.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.ho.w)
            self.ho.y = random.Random().randint(0, 720)
            self.ho.width = 75
            self.ho.height = 75
            self.ho.z_index = 3

        self.button5 = button5()
        self.add_actor(self.button5)
        self.button5.width = 125
        self.button5.height = 75
        self.button5.y = 0
        self.button5.x = 0

        self.set_on_key_down_listener(self.katt1)
        self.button5.set_on_mouse_down_listener(self.Klikk1)

    def Klikk1(self, sender,event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.nemethcsababence.Menu.menu.MenuScreen())

    def katt1(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            self.screen.game.set_screen(Weathersim.nemethcsababence.Menu.menu.MenuScreen())
