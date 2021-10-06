import game
from game.scene2d.MyScreen import *


class Screen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(GameStage())

class hatter(game.scene2d.MyActor):

    def __init__(self):
        self.hatter = super().__init__('../!_resources/images/sunny.png')

class taj(game.scene2d.MyActor):
    
    def __init__(self):
        self.tajocska = super().__init__('../!_resources/images/landscape.png')

class nap(game.scene2d.MyActor):

    def __init__(self):
        self.nap = super().__init__('../!_resources/images/sun.png')

class GameStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.hatter = hatter()
        self.hatter.width = 1280
        self.hatter.height = 720
        self.taj = taj()
        self.taj.width = 1280
        self.taj.height = 720
        self.taj.set_on_key_down_listener(self.key_down)
        self.nap = nap()
        self.nap.width = 512
        self.nap.height = 512
        self.nap.x = 850
        self.nap.y = -120
        self.add_actor(self.hatter)
        self.add_actor(self.taj)
        self.add_actor(self.nap)

    def key_down(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()

class Napos(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = Screen()

Napos().run()