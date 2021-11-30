import game
import pygame
from Nike.NikeScreen import *
from Nike.NikeStage import *

class Game(game.scene2d.MyGame):
    def __init__(self, width: int = 1280, height: int = 720):
        super().__init__(width, height)
        self.screen = Menu()

Game().run()