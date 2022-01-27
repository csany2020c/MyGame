import game
import pygame
from Nike.NikeScreen import *
from Nike.NikeStage import *

class Game(game.scene2d.MyGame):
    def __init__(self, width: int = 1280, height: int = 720):
        super().__init__(width, height)
        self.screen = Menu()
        pygame.display.set_caption('FatJordan')
        T = pygame.image.load('images/lebronjames.png')
        pygame.display.set_icon(T)

Game().run()