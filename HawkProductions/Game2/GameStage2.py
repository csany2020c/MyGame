import time
import game
import pygame
import random
from HawkProductions.Actors import *
import HawkProductions.menu.MenuScreen
import HawkProductions.over.OverScreen
from game.scene2d import MyBaseActor


class GameStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.Bg = Bg()
        self.add_actor(self.Bg)
        self.Bg.set_size(width=1280, height=720)



        self.arrow = Arrow()
        self.add_actor(self.arrow)
        self.arrow.x = 0
        self.arrow.y = 5
        self.arrow.w = 125
        self.arrow.set_on_mouse_down_listener(self.click2)

        self.set_on_key_down_listener(self.katt)

        f = open("szoveg/map.txt", "r")

        y: int = 0
        while True:
            line = f.read().strip()
            if line:
                x: int = 0
                for c in line:
                    a: MyBaseActor = None
                    if c == "0":
                        a = Pile_f()
                        a.set_hitbox_scale_h(0.1)
                        a.set_hitbox_scale_w(0.1)
                        a.h = random.randint(400, 500)
                    if c == "1":
                        a = Pile_a()
                        a.set_hitbox_scale_h(0.1)
                        a.set_hitbox_scale_w(0.1)
                        a.h = random.randint(400,500)
                    if c == "d":
                        self.D = Deagle_2()
                        self.D.width = 95
                        a = self.D
                    if a is not None:
                        a.y = random.randint(-10, 35)
                        a.x = 10
                        self.add_actor(a)
                        self.add_actor(a)
                        print(c)
                    x += 1
            else:
                break
            y += 1

    def click2(self, sender, event):
         if event.button == 1:
            self.screen.game.set_screen(HawkProductions.menu.MenuScreen.MenuScreen())

    def katt(self, sender, event):
        print(sender)
        if event.key == pygame.K_BACKSPACE:
            self.screen.game.set_screen(HawkProductions.menu.MenuScreen.MenuScreen())
        if event.key == pygame.K_ESCAPE:
            quit()
        if event.key == pygame.K_w:
            self.D.y -= 50
            self.D.r -= 8
        if event.key == pygame.K_s:
            self.D.y += 50
            self.D.r += 8
