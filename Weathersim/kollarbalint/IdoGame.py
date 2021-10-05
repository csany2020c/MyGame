import game
import pygame
from Weathersim.kollarbalint.IdoScreen import *

class Ido(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = MenuScr()


Ido().run()