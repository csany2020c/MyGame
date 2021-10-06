import pygame

import game


class taj(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('!_resources/images/landscape.png')


class kekeg(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('!_resources/images/sunny.png')


class nap(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('!_resources/images/sun.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.x + self.width < game.scene2d.MyGame.get_screen_width():
            self.x += delta_time * 60
            self.rotate_with(delta_time * 20)


class GameStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.taj = taj()
        self.taj.width = 1280
        self.taj.height = 720
        self.taj.z_index = 3
        self.eg = kekeg()
        self.eg.width = 1920
        self.eg.height = 1300
        self.eg.z_index = 1
        self.nap = nap()
        self.nap.width = 600
        self.nap.height = 600
        self.nap.y = -150
        self.nap.x = 500
        self.nap.z_index = 2
        self.add_actor(self.taj)
        self.add_actor(self.eg)
        self.add_actor(self.nap)


class GameScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(GameStage())


class Program(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = GameScreen()


Program().run()