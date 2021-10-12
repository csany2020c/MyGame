import game
import random
import pygame
from Weathersim.faterlaszlo.Arial import *
from Weathersim.faterlaszlo.f_actors import *
import Weathersim.faterlaszlo.f_screen_m

class f_stage4(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.bg = bg_actor_s()
        self.felho = felhos_actor()
        self.add_actor(self.bg)
        self.add_actor(self.felho)
        self.felho.z_index = 0
        self.set_on_key_down_listener(self.key_down)

        self.t = Arial()
        self.add_actor(self.t)
        self.t.set_text("Vissza")
        self.t.set_color(1, 1, 1)
        self.t.x = 0
        self.t.y = 0
        self.t.set_on_mouse_down_listener(self.click)

        self.snowman = snowman()
        self.add_actor(self.snowman)
        self.snowman.h = 200
        self.snowman.x = 500
        self.snowman.y = 500

        for i in range(24):
            self.havazik = havazas()
            self.add_actor(self.havazik)
            self.havazik.h = 20
            self.havazik.w = 45
            self.havazik.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.havazik.w)
            self.havazik.y = random.Random().randint(0, game.scene2d.MyGame.get_screen_height() - self.havazik.h)


    def click(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.faterlaszlo.f_screen_m.f_screen_m())

    def key_down(self, sender, event):
        if event.key == pygame.K_BACKSPACE:
            self.screen.game.set_screen(Weathersim.faterlaszlo.f_screen_m.f_screen_m())

