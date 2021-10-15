import game
import random
import pygame
from Weathersim.faterlaszlo.Arial import *
import Weathersim.faterlaszlo.f_screen_m
from Weathersim.faterlaszlo.f_actors import *


class f_stage3(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.bg = bg_actor()
        self.felhos = felhos_actor()
        self.add_actor(self.bg)
        self.add_actor(self.felhos)
        self.felhos.z_index = 0
        self.set_on_key_down_listener(self.key_down)

        self.t = Arial()
        self.add_actor(self.t)
        self.t.set_text("Vissza")
        self.t.x = 0
        self.t.y = 0
        self.t.set_on_mouse_down_listener(self.click)

        self.cloud = cloud()
        self.add_actor(self.cloud)
        self.cloud.y = 50
        self.cloud.x = 250
        self.cloud.w = 180
        self.cloud.z_index = 2

        for i in range(12):
            self.eso = eso()
            self.add_actor(self.eso)
            self.eso.h = 25
            self.eso.w = 50
            self.eso.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.eso.w)
            self.eso.y = random.Random().randint(0, game.scene2d.MyGame.get_screen_height() - self.eso.h)

    def click(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.faterlaszlo.f_screen_m.f_screen_m())

    def key_down(self, sender, event):
        if event.key == pygame.K_BACKSPACE:
            self.screen.game.set_screen(Weathersim.faterlaszlo.f_screen_m.f_screen_m())


