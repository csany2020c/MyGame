import game
import random
from game.scene2d.MyScreen import *

class Actor(game.scene2d.MyActor):

    def __init__(self, image_url: str = "images/spiderman.png"):
        super().__init__(image_url)

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 100



class Hatter(game.scene2d.MyActor):

    def __init__(self, image_url: str = "images/hatter.jpg"):
        super().__init__(image_url)


class Stage(game.scene2d.MyStage):


    def __init__(self):
        super().__init__()

        self.hatter_bg = Hatter()
        self.actor1_bg = Actor()
        self.add_actor(self.hatter_bg)
        self.add_actor(self.actor1_bg)

class Screen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(Stage())


class Kep(game.scene2d.MyGame):
    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False):
        super().__init__(width, height, autorun)
        self.screen = Screen()

Kep().run()

