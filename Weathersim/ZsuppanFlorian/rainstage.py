from Weathersim.ZsuppanFlorian.mainstage import *


class rainStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()

        for k in range(100):
            self.rain = eso()
            tag = random.randint(a=30, b=60)
            self.rain.height = tag
            self.rain.width = tag
            self.rain.x = random.randint(a=0, b=1280)
            self.rain.y = random.randint(a=-0, b=720)
            self.add_actor(self.rain)

