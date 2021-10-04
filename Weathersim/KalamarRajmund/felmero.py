import game
from game.scene2d.MyScreen import *



class Esozik (game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__ ('!_resources/images/rain.png')

class Szürkehatter(game.scene2d.MyActor):
    def __init__(self):
    self.map = super ().__init__('!resources/images/landscape.png')





Esozik()

