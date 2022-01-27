import game
import pygame

class BgActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/snow.png')

class Energy(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/SportDrink.png')

class Trap(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/Trap.png')

class Back(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/back.png')
        self.width = 100
        self.height = 50