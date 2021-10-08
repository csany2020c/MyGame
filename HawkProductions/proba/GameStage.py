import time
import game
from HawkProductions.proba.Actors import *
import random
from time import sleep


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

        for i in range(2):
            self.P1 = Pile1()
            self.P1.set_hitbox_scale_h = 0.35
            self.P1.set_hitbox_scale_w = 0.2
            self.add_actor(self.P1)
            self.P1.set_size(width=250, height=250)
            self.P1.x = 1280
            self.P1.y = random.randint(0, 720)
            self.P2 = Pile2()
            self.P2.set_hitbox_scale_h = 0.35
            self.P2.set_hitbox_scale_w = 0.2
            self.add_actor(self.P2)
            self.P2.set_size(width=250, height=250)
            self.P2.x = 1280
            self.P2.y = random.randint(0, 720)
            time.sleep(1)

    def click(self, sender, event):
        self.D.y -= 50
