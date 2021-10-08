import game
import random

class menubutton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/menubutton.png')

class minimenubutton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/minimenubutton.png')

class mininapbutton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/mininapbutton.png')

class miniesobutton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/miniesobutton.png')

class minihavasesobutton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/minihavasesobutton.png')

class minihobutton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/minihobutton.png')

