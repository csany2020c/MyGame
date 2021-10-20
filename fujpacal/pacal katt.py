import game
import random
from game.scene2d.MyScreen import *

class PacalActor(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_images/bogracs.png')

class Hatter(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_images/hatter.jpg')



class PacalStage(game.scene2d.MyStage):
    def __init__(self):
        super(PacalStage).__init__()
        self.actor_bg = PacalActor()
        self.hatter_bg = Hatter()
        self.add_actor(self.actor_bg)
        self.add_actor(self.hatter_bg)

class PacalScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0)
        self.add_stage(PacalStage())


class PacalKep(game.scene2d.MyGame):
    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False):
        super().__init__(width, height, autorun)
        self.screen = PacalScreen()

PacalKep().run()

