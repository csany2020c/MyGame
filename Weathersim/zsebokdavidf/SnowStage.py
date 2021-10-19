from Weathersim.zsebokdavidf.MainActors import *
import pygame


class SnowStage(game.scene2d.MyStage):

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

        for i in range(4):
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






