from Weathersim.vizdakmate.Screen import *
import game
import pygame
from Weathersim.vizdakmate.Stage import *
class Main(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen = RainScreen()

Main().run()