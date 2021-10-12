import game
import random
import pygame
from Weathersim.faterlaszlo.Arial import *
from Weathersim.faterlaszlo.f_actors import *
import Weathersim.faterlaszlo.f_screen_m

class f_stage1(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.bg = bg_actor()
        self.sun = napocska()
        self.eg = eg_actor()
        self.add_actor(self.bg)
        self.add_actor(self.sun)
        self.add_actor(self.eg)
        self.sun.x = 50
        self.sun.y = 80
        self.sun.w = 350
        self.eg.z_index = 0
        self.sun.z_index = 2
        self.set_on_key_down_listener(self.key_down)

        self.t = Arial()
        self.add_actor(self.t)
        self.t.set_text("Vissza")
        self.t.x = 0
        self.t.y = 0
        self.t.set_on_mouse_down_listener(self.click)

        for i in range(3):
            self.a = apple()
            self.add_actor(self.a)
            self.a.w = 35
            self.a.x = random.Random().randint(10, 300)
            self.a.y = random.Random().randint(0, 250)

    def click(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.faterlaszlo.f_screen_m.f_screen_m())

    def key_down(self, sender, event):
        if event.key == pygame.K_BACKSPACE:
            self.screen.game.set_screen(Weathersim.faterlaszlo.f_screen_m.f_screen_m())

