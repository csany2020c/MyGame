import game
from game.scene2d.MyScreen import *

class erdo(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('!_resources/images/landscape.png')