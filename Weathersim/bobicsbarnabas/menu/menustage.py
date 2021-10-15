import Weathersim.bobicsbarnabas.stage
import game
import pygame
from Weathersim.bobicsbarnabas.menu.menuactor import *
from Weathersim.bobicsbarnabas.screen import *


class menustage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.menuactor = menuhatter()
        self.exit = exit()
        self.actor1 = menuactor1()
        self.actor2 = menuactor2()
        self.actor3 = menuactor3()
        self.actor4 = menuactor4()
        self.actor1.w = 50
        self.actor1.h = 50
        self.actor1.x = 500
        self.actor1.y = 410

        self.actor2.w = 50
        self.actor2.h = 50
        self.actor2.x = 500
        self.actor2.y = 210

        self.actor3.w = 50
        self.actor3.h = 50
        self.actor3.x = 500
        self.actor3.y = 310

        self.actor4.w = 50
        self.actor4.h = 50
        self.actor4.x = 500
        self.actor4.y = 510

        self.exit.w = 40
        self.exit.h = 40
        self.exit.x = 0
        self.exit.y = 675


        self.add_actor(self.actor1)
        self.add_actor(self.actor2)
        self.add_actor(self.actor3)
        self.add_actor(self.actor4)
        self.add_actor(self.menuactor)
        self.add_actor(self.exit)


        self.actor1.set_on_mouse_down_listener(self.button_down1)
        self.actor2.set_on_mouse_down_listener(self.button_down2)
        self.actor3.set_on_mouse_down_listener(self.button_down3)
        self.actor4.set_on_mouse_down_listener(self.button_down4)
        self.exit.set_on_mouse_down_listener(self.button_down5)

    def button_down1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.bobicsbarnabas.screen.napsutesscreen())

    def button_down2(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.bobicsbarnabas.screen.havazasscreen())

    def button_down3(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.bobicsbarnabas.screen.havasesoscreen())

    def button_down4(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.bobicsbarnabas.screen.esoscreen())

    def button_down5(self, sender, event):
        if event.button == 1:
            quit()