import pygame
import game
import random
from bruhmomento.bruhActor import *
from game.scene2d import MyPermanentTimer, MyOneTickTimer, MyBaseActor, MyTickTimer, MyIntervalTimer


class bruhstage(game.scene2d.MyStage):


    def __init__(self):
        super().__init__()
        self.add_actor(map())
        self.add_actor(bruhActor())
        self.enemy1 = enemy1()
        self.add_actor(self.enemy1)
        self.add_actor(kapu())
        self.enemy1.x = 1000
        self.enemy1.y = 300

class level2(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.add_actor(map())
        self.bumsteve = enemy2()
        self.add_actor(self.bumsteve)
        self.bumsteve.x = 1000
        self.bumsteve.y = 300
        self.add_actor(bruhActor())