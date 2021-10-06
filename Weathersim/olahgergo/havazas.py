from Weathersim.olahgergo.actors import *


class HoStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()

        feg = felhoeg()
        feg.height = 720
        feg.width = 1280
        self.add_actor(actor=feg)

        hk = hatterkep()
        hk.height = 720
        hk.width = 1280
        self.add_actor(actor=hk)


        for i in range(40):
            self.ho = ho()
            size = random.randint(a=20, b=100)
            self.ho.height = size
            self.ho.width = size
            self.ho.x = random.randint(a=0, b=1280)
            self.ho.y = random.randint(a=-0, b=720)
            self.add_actor(self.ho)




