import Weathersim
import game
import random
import pygame
from Weathersim.NemethCsongor.Actorok import *


class SwStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.C = Cloudy()
        self.add_actor(self.C)

        self.Bg = Bg()
        self.add_actor(self.Bg)

        for i in range(30):
            self.S = Snow()
            self.add_actor(self.S)
            self.S.set_size(width=30, height=30)
            self.S.x = random.randint(a=0, b=1280)
            self.S.y = random.randint(a=-0, b=720)

        self.set_on_key_down_listener(self.key_down)
        self.set_on_key_down_listener(self.key_down2)

    def key_down(self, sender, event):
        if event.key == pygame.K_KP1:
            self.screen.game.set_r()

    def key_down2(self, sender, event):
        if event.key == pygame.K_KP2:
            self.screen.game.set_su()
