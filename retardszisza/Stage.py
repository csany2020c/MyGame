import game
from retardszisza.Actor import *
import random
import pygame


class GameStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.c = UtActor()
        self.add_actor(self.c)
        self.b = Enemy1Actor()
        self.add_actor(self.b)
        self.b.y = 150



    def act(self, delta_time: float):
        super().act(delta_time)

    def halal(self):
        super().__init__()

