import pygame
import random
from bruhmomento.bruhActor import *
from bruhmomento.bruhScreen import *
from game.scene2d import MyPermanentTimer, MyOneTickTimer, MyBaseActor, MyTickTimer, MyIntervalTimer
import game

class menustage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.add_actor(startgomb())
    def Click(self, sender,event):
        if event.button == 1:
            self.screen.game.set_screen(bruhScreen)