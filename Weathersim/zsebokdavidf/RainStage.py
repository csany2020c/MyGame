import game
import pygame
from Weathersim.zsebokdavidf.MainActors import *


class RainStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()

        self.add_actor(Cloud())
