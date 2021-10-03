import game
from game.scene2d.MyScreen import *


class taj(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('!_resources/images/landscape.png')


class szurkeeg(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('!_resources/images/cloudy.png')


class eso(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('!_resources/images/rain.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 200




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
        self.eso = eso()
        self.eso.width = 50
        self.eso.height = 50
        self.z_index = 3
        self.add_actor(self.taj)
        self.add_actor(self.szeg)
        self.add_actor(self.eso)


    def key_down(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()


class GameScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(GameStage())


class Program(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = GameScreen()


Program().run()