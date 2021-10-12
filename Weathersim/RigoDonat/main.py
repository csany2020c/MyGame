import game
import pygame
from Weathersim.RigoDonat.screen import *
from Weathersim.RigoDonat.stages import *
class Game(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen = Menu()

Game().run()