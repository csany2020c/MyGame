import game
from game.scene2d.MyScreen import *

class erdo(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/landscape.png')

class naposeg(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/sunny.png')

class felhoseg(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/cloudy.png')

class esocsepp(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/rain.png')

class hopehely(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/snow.png')
