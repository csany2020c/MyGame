import game
from game.scene2d.MyScreen import *


class taj(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('!_resources/images/landscape.png')


class kekeg(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('!_resources/images/cloudy.png')


class ho(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('!_resources/images/snow.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 200


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
        self.eg = kekeg()
        self.eg.width = 1920
        self.eg.height = 1300
        self.eg.z_index = 1
        self.ho = ho()
        self.ho.width = 200
        self.ho.height = 200
        self.ho.z_index = 3
        self.eso = eso()
        self.eso.width = 200
        self.eso.height = 100
        self.eso.x = 500
        self.eso.y = 300
        self.eso.z_index = 3
        self.add_actor(self.taj)
        self.add_actor(self.eg)
        self.add_actor(self.ho)
        self.add_actor(self.eso)
        self.taj.set_on_key_down_listener(self.key_down)

    def key_down(self, event):
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