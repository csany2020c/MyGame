import game
from Weathersim.vizdakmate.Actor import *
from game.scene2d import MyTickTimer
import random
import pygame


class SunnyStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.add_actor(Sunny())
        self.add_actor(Snow())
        self.add_actor(Background())
        self.Sun = Sun()
        self.add_actor(self.Sun)

    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("'QUIT'")
            quit()