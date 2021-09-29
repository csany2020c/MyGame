import game
from HawkProductions.Enemy1Actor import *
from HawkProductions.Enemy2Actor import *
from HawkProductions.Anything import *

class MenuStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.h1 = Enemy1Actor()
        self.h2 = Enemy2Actor()
        self.b = Anything()
        self.add_actor(self.h1)
        self.add_actor(self.h2)
        self.add_actor(self.b)
        self.h1.x = 525
        self.h1.y = 250
        self.h1.w = 200
        self.h2.x = 525
        self.h2.y = 400
        self.h2.w = 200
        self.b.set_text("Flappy D")
        self.b.set_x(500)
        self.b.set_y(100)



