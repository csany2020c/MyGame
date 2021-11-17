import pygame
import random
from bruhmomento.bruhActor import *
from game.scene2d import MyPermanentTimer, MyOneTickTimer, MyBaseActor, MyTickTimer, MyIntervalTimer
import game

class level2(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.hatter = map()
        self.add_actor(self.hatter)
        self.bumsteve = enemy2()
        self.add_actor(self.bumsteve)
        self.bumsteve.x = 1000
        self.bumsteve.y = 300
        self.add_actor(fohos())