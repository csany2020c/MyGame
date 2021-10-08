import game
import random
import pygame
from Weathersim.NemethCsongor.Actorok import *


class RStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.C = Cloudy()
        self.add_actor(self.C)

        self.Bg = Bg()
        self.add_actor(self.Bg)

        for i in range(23):
            self.R = Rain()
            self.add_actor(self.R)
            self.R.set_size(width=30, height=30)
            self.R.x = random.randint(a=0, b=1280)
            self.R.y = random.randint(a=-0, b=720)

        self.set_on_key_down_listener(self.key_down)
        self.set_on_key_down_listener(self.key_down2)

    def key_down(self, sender, event):
        if event.key == pygame.K_KP3:
            self.screen.game.set_sw()

    def key_down2(self, sender, event):
        if event.key == pygame.K_KP2:
            self.screen.game.set_su()
