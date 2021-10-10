import game
import random

class menubutton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/menubutton.png')
        self.z_index = 6

class minimenubutton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/minimenubutton.png')
        self.z_index = 6

class mininapbutton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/mininapbutton.png')
        self.z_index = 6

class miniesobutton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/miniesobutton.png')
        self.z_index = 6

class minihavasesobutton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/minihavasesobutton.png')
        self.z_index = 6

class minihobutton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/minihobutton.png')
        self.z_index = 6

