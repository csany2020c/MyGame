from yetifc.Actor import *
import game

class Stage3(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        a = MenuActor1()
        a.y = 50
        self.add_actor(a)
        b = MenuActor2()
        b.y = 400
        self.add_actor(b)

    def kepvaltas(self):
        self.set_screen()
