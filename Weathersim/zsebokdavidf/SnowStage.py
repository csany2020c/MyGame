from Weathersim.zsebokdavidf.MainActors import *
import pygame


class SnowStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()

        bg = Background()
        bg.height = 720
        bg.width = 1280
        self.add_actor(actor=bg)

        for i in range(3):
            sg = SnowyGround()
            sg.height = 720
            sg.width = 1280
            self.add_actor(actor=sg)

        ice = Ice()
        ice.height = 720
        ice.width = 1280
        self.add_actor(actor=ice)

        for k in range(40):
            self.sn = Snow()
            size = random.randint(a=20, b=100)
            self.sn.height = size
            self.sn.width = size
            self.sn.x = random.randint(a=0, b=1280)
            self.sn.y = random.randint(a=-0, b=720)
            self.add_actor(self.sn)






