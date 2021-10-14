from Weathersim.ZsuppanFlorian.mainactors import *


class snowStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()

        for i in range(60):
            self.ho = ho()
            tag = random.randint(a=20, b=100)
            self.ho.height = tag
            self.ho.width = tag
            self.ho.x = random.randint(a=0, b=1280)
            self.ho.y = random.randint(a=-0, b=720)
            self.add_actor(self.ho)



