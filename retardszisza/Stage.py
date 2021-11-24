import game
from retardszisza.Actor import *
import random
import pygame


class GameStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.c = UtActor()
        self.b = Enemy1Actor()
        self.a = Enemy2Actor()
        self.add_actor(self.c)
        self.add_actor(self.b)
        self.add_actor(self.a)
        self.a.x = 900
        self.a.y = 100
        self.b.y = 70

        self.b.set_on_key_down_listener(self.button_down)

    def button_down(self, sender, event):
        if event.key == pygame.K_w:
            self.b.y -= 170
            print("asd")
        if event.key == pygame.K_s:
            self.b.y += 170

    def act(self, delta_time: float):
        super().__init__()

        if Enemy2Actor.overlaps(Enemy1Actor):
            quit()


