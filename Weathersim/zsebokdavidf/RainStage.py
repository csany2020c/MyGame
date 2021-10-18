from Weathersim.zsebokdavidf.MainActors import *


class RainStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()

        for i in range(10):
            cd = Cloud()
            cd.x = random.randint(a=-640, b=640)
            cd.y = random.randint(a=-720, b=-320)
            self.add_actor(cd)

        bg = Background()
        bg.height = 720
        bg.width = 1280
        self.add_actor(actor=bg)

        for k in range(40):
            self.rain = Rain()
            size = random.randint(a=20, b=50)
            self.rain.height = size
            self.rain.width = size
            self.rain.x = random.randint(a=0, b=1280)
            self.rain.y = random.randint(a=-0, b=720)
            self.add_actor(self.rain)
