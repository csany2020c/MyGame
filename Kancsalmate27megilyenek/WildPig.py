import random
from typing import List

import pygame

import game
from game.scene2d import MyTickTimer


class WildPig(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("wildpig/tile000.png")
        pygame.init()
        self.szelesseg = pygame.display.get_surface().get_width()
        self.magassag = pygame.display.get_surface().get_height()
        self.images:List['str'] = ("wildpig/tile000.png","wildpig/tile001.png","wildpig/tile002.png","wildpig/tile003.png","wildpig/tile004.png","wildpig/tile005.png","wildpig/tile006.png")
        self.timer = MyTickTimer(func=self.timeHandling2, interval=0.14, start_delay=0, repeat=True)
        self.add_timer(self.timer)
        self.set_position(-300,random.randint(0,self.magassag - self.get_height()))

    def timeHandling2(self, sender):
        if self.image_url == self.images[0]:
            self.image_url = self.images[1]
        elif self.image_url == self.images[1]:
            self.image_url = self.images[2]
        elif self.image_url == self.images[2]:
            self.image_url = self.images[3]
        elif self.image_url == self.images[3]:
            self.image_url = self.images[4]
        elif self.image_url == self.images[4]:
            self.image_url = self.images[5]
        elif self.image_url == self.images[5]:
            self.image_url = self.images[6]
        elif self.image_url == self.images[6]:
            self.image_url = self.images[0]

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x = int(self.get_x() + 5)

