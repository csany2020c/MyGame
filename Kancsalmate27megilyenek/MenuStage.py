import game
from Kancsalmate27megilyenek.MenuActor import *

class Actor1(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("../HelloWorld/fox.png")


class Stage3(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        a = MenuActor1()
        a.y = 50
        self.add_actor(a)