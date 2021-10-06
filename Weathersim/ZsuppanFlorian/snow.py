import game
from game.scene2d.MyScreen import *


class hatter(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('resource/images/landscape.png')


class eg(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('resource/images/cloudy.png')


class ho(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('resource/images/snow.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 170


class GameStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.hatter = hatter()
        self.hatter.width = 1280
        self.hatter.height = 720
        self.hatter.z_index = 2
        self.eg = eg()
        self.eg.width = 1920
        self.eg.height = 1300
        self.eg.z_index = 1
        self.ho = ho()
        self.ho.width = 100
        self.ho.height= 100
        self.ho.z_index = 3
        self.ho.x = 800
        self.ho.y = 400
        self.add_actor(self.hatter)
        self.add_actor(self.eg)
        self.add_actor(self.ho)


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