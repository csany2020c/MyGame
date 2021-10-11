import game
from game.scene2d.MyGame import *

class NaposActor():
    def __init__(self):
        self.map = super(NaposActor, self).__init__('!_resources/images/sunny.png')

class FelhosActor():
    def __init__(self):
        self.map = super(FelhosActor, self).__init__('!_resources/images/cloudy.png')

class HatterActor():
    def __init__(self):
        self.map = super(HatterActor, self).__init__('!_resources/images/landscape.png')

class EsoActor():
    def __init__(self):
        self.map = super(EsoActor, self).__init__('!_resources/images/rain.png')

class NapActor():
    def __init__(self):
        self.map = super(NapActor, self).__init__('!_resources/images/sun.png')

class HoActor():
    def __init__(self):
        self.map = super(HoActor, self).__init__('!_resources/images/now.png')

class HoEsoActor():
    def __init__(self):
        self.map = super(HoEsoActor, self).__init__('!_resources/images/rain.png/snow.png')

