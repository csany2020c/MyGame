import game
from game.scene2d.MyScreen import *


class Screen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(GameStage())

class taj(game.scene2d.MyActor):
    
    def __init__(self):
        self.map = super().__init__('!_resources/images/landscape.png')

class GameStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.taj = taj()
        self.taj.width = 1280
        self.taj.height = 720
        self.add_actor(self.taj)
        self.taj.set_on_key_down_listener(self.key_down)

    def key_down(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()

class Nap(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = GameScreen()

Nap().run()