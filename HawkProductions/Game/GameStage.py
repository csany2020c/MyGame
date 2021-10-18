import time
import game
import pygame
import random
from HawkProductions.Actors import *
import HawkProductions.MenuScreen


class GameStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.Bg = Bg()
        self.add_actor(self.Bg)
        self.Bg.set_size(width=1280, height=720)

        self.D = Deagle()
        self.add_actor(self.D)
        self.D.y = 250
        self.D.x = 300
        self.D.width = 60

        self.arrow = Arrow()
        self.add_actor(self.arrow)
        self.arrow.x = 0
        self.arrow.y = 5
        self.arrow.w = 125
        self.arrow.set_on_mouse_down_listener(self.click2)

        self.add_timer(game.scene2d.MyTickTimer(self.add_asd, 5))
        self.add_timer(game.scene2d.MyTickTimer(self.add_asd2, 5))

        self.set_on_key_down_listener(self.katt)

    def add_asd(self, sender):
        self.P1 = Pile()
        self.add_actor(self.P1)
        self.P1.set_hitbox_scale_h = 0.35
        self.P1.set_hitbox_scale_w = 0.2
        self.P1.set_size(width=250, height=250)
        self.P1.x = 1280
        self.P1.y = random.randint(10, 500)
        self.P1.width = 600

    def add_asd2(self, sender):
        self.C = Coin()
        self.add_actor(self.C)
        self.C.x = 1280
        self.C.y = random.randint(10, 500)
        self.C.width = 300

    def click2(self, sender, event):
         if event.button == 1:
            self.screen.game.set_screen(HawkProductions.MenuScreen.MenuScreen())

    def katt(self, sender, event):
        print(sender)
        if event.key == pygame.K_BACKSPACE:
            self.screen.game.set_screen(HawkProductions.MenuScreen.MenuScreen())
        if event.key == pygame.K_ESCAPE:
            quit()
        if event.key == pygame.K_w:
            self.D.y -= 50
            self.D.r -= 15
        if event.key == pygame.K_s:
            self.D.y += 50
            self.D.r += 15
