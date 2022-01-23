import game
import pygame

class BgActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/menu.png')

class Energy(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/SportDrink.png')

class Trap(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/Trap.png')