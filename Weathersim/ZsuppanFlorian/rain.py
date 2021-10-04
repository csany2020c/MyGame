import game
import game
from game.scene2d.MyScreen import *

class Stage(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = GameScreen()

class taj(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('Weathersim/ZsuppanFlorian/images/rain.png')


class szurkeeg(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('Weathersim/ZsuppanFlorian/images/rain.png')


class rain(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('Weathersim/ZsuppanFlorian/images/rain.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 250

class GameStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.taj = taj()
        self.taj.width = 1280
        self.taj.height = 720
        self.taj.z_index = 2
        self.szeg = szurkeeg()
        self.szeg.width = 1920
        self.szeg.height = 1080
        self.szeg.z_index = 1
        self.rain = rain()
        self.rain.width = 50
        self.rain.height = 50
        self.z_index = 3
        self.add_actor(self.taj)
        self.add_actor(self.szeg)
        self.add_actor(self.rain)


    def key_down(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()


class GameScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(GameStage())

Stage().run()