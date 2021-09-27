import game
#from HawkProductions.Enemy1Actor import *
#from HawkProductions.Enemy2Actor import *
from HawkProductions.menu import *

class GameStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.h1 = Enemy1Actor()
        self.h2 = Enemy2Actor()
        self.add_actor(self.h1)
        self.add_actor(self.h2)
        self.h1.x = 525
        self.h1.y = 250
        self.h1.w = 200
        self.h2.x = 525
        self.h2.y = 400
        self.h2.w = 200
