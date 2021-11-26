import pygame
import random
from bruhmomento.bruhActor import *
from game.scene2d import MyPermanentTimer, MyOneTickTimer, MyBaseActor, MyTickTimer, MyIntervalTimer
import game

class menustage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.add_actor(startgomb())