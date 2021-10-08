from Weathersim.ZsuppanFlorian.mainactors import *


class snowStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()

        for k in range(40):
            self.ho = ho()
            size = random.randint(a=20, b=100)
            self.ho.height = size
            self.ho.width = size
            self.ho.x = random.randint(a=0, b=1280)
            self.ho.y = random.randint(a=-0, b=720)
            self.add_actor(self.ho)



