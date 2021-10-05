import game
from Weathersim.TothAkos.actor import *
from game.scene2d import MyTickTimer
import random
import pygame


class Sunnystage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.b = Sun()
        self.add_actor(Sunny())
        self.add_actor(Landscape())
        self.Sun = Sun()
        self.add_actor(self.Sun)
        for j in range(1):
            for i in range(1):
                e = Sun()
                e.y = i * 40
                e.x = j * 40
                # e.width = 10
                # e.height = 10
                self.add_actor(e)

    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("'QUIT'")
            quit()