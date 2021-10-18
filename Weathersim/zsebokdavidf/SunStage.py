from Weathersim.zsebokdavidf.MainActors import *


class SunStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()

        bg = Background()
        bg.height = 720
        bg.width = 1280
        self.add_actor(actor=bg)
