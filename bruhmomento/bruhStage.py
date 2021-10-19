import pygame
import random
from bruhmomento.bruhScreen import *
from bruhmomento.bruhActor import *
from game.scene2d import MyPermanentTimer, MyOneTickTimer, MyBaseActor, MyTickTimer, MyIntervalTimer
import game


class bruhstage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.add_actor(map())
        self.fohos = fohos()
        self.add_actor(self.fohos)
        self.kapu = kapu()
        self.add_actor(self.kapu)
        self.kapu.x = 70
        self.kapu.y = 200
        self.enemy1 = enemy1()
        self.add_actor(self.enemy1)
        self.enemy1.x = 1000
        self.enemy1.y = 300

    def act(self, delta_time: float):
        super().act(delta_time)
        overlapsASD: bool = False
        for actorASD in self.actors:
            if isinstance(actorASD, kapu):
                if self.fohos.overlaps(actorASD):
                    overlapsASD = True
                    break
        if overlapsASD:
            print("asdasdasd")

class level2(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.add_actor(map())
        self.bumsteve = enemy2()
        self.add_actor(self.bumsteve)
        self.bumsteve.x = 1000
        self.bumsteve.y = 300
        self.add_actor(fohos())