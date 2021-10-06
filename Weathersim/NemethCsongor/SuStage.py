import game
import random
import pygame
from Weathersim.NemethCsongor.Actorok import *


class SuStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.S = Sunny()
        self.add_actor(self.S)

        self.Bg = Bg()
        self.add_actor(self.Bg)

        self.Su = Sun()
        self.add_actor(self.Su)
        self.Su.x = 850
        self.Su.y = 5
        self.Su.set_size(width=350, height=350)

        self.set_on_key_down_listener(self.key_down)
        self.set_on_key_down_listener(self.key_down2)

    def key_down(self, sender, event):
        if event.key == pygame.K_KP1:
            self.screen.game.set_r()

    def key_down2(self, sender, event):
        if event.key == pygame.K_KP3:
            self.screen.game.set_sw()
