
import game
import pygame
from Kancsalmate27megilyenek.InfoScreen import *
from Kancsalmate27megilyenek.DevActor import *
class InfoStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        pygame.init()
        Dev = DevActor()
        self.add_actor(Dev)
