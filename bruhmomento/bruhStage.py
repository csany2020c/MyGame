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
        self.add_actor(enemy2())
        self.add_actor(horthy())
        self.enemy1 = enemy1()
        self.add_actor(self.enemy1)
        self.t = MyTickTimer(interval=1.5, func=self.tikk)
        self.enemy1.add_timer(self.t)


    def tikk(self, sender):
        self.enemy1.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.enemy1.w)
        self.enemy1.y = random.Random().randint(0, game.scene2d.MyGame.get_screen_height() - self.enemy1.h)
