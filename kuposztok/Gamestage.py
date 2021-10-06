import game
from kuposztok.actors import *

class MenuStage(game.scene2d.MyStage):


    def __init__(self):
        super().__init__()
        bg = BgActor()
        a = MenuActor()
        a.y = 0
        self.add_actor(bg)
        self.add_actor(a)
        print(a)