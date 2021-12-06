import pygame
import random

import bruhmomento.bruhScreen
from bruhmomento.bruhActor import *
from bruhmomento.bruhScreen import *
from game.scene2d import MyPermanentTimer, MyOneTickTimer, MyBaseActor, MyTickTimer, MyIntervalTimer
import game

class menustage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.add_actor(startgomb())
        self.startgomb = startgomb()
        self.startgomb.set_on_mouse_down_listener(self.inditas)

    #def Click(self, sender,event):
    #    if event.button == 1:
    #        self.screen = bruhScreen()

    def inditas(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.screen.game.set_screen(bruhmomento.bruhScreen.bruhScreen())