import retardszisza.Stage
import game
import pygame
from retardszisza.menu_halal.HalalActor import *
from retardszisza.Screen import *

class halalstage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.actor1 = halalhatter()
        self.add_actor(self.actor1)