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
        self.D.x = 50
        self.D.width = 100
        self.set_on_mouse_down_listener(self.click)

        self.arrow = Arrow()
        self.add_actor(self.arrow)
        self.arrow.x = 0
        self.arrow.y = 5
        self.arrow.w = 125
        self.arrow.set_on_mouse_down_listener(self.click2)

        for i in range(20):
            self.P1 = Pile()
            self.add_actor(self.P1)
            self.P1.set_hitbox_scale_h = 0.35
            self.P1.set_hitbox_scale_w = 0.2
            self.P1.set_size(width=250, height=250)
            self.P1.x = random.randint(1280, 5000)
            self.P1.y = random.randint(-250, 720)

        self.set_on_key_down_listener(self.katt)
        self.P2 = Pile()
        self.P2.set_hitbox_scale_h = 0.35
        self.P2.set_hitbox_scale_w = 0.2
        self.add_actor(self.P2)
        self.P2.set_size(width=250, height=250)
        self.P2.x = 1280
        self.P2.y = random.randint(0, 720)


    def click(self, sender, event):
        self.D.y -= 50
        self.D.r -= 3.5

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
            self.D.r -= 3.5

        if event.key == pygame.K_s:
            self.D.y += 50
