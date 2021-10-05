from Weathersim.zsebokdavidf.MainActors import *


class RainStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()

        for k in range(40):
            self.rain = Rain()
            size = random.randint(a=20, b=50)
            self.rain.height = size
            self.rain.width = size
            self.rain.x = random.randint(a=0, b=1280)
            self.rain.y = random.randint(a=-0, b=720)
            self.add_actor(self.rain)

        self.add_actor(Cloud())
