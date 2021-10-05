from Weathersim.zsebokdavidf.MainActors import *
import random
import pygame
import game


class SnowStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        bg = Background()
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
            size = random.randint(a=50, b=100)
            self.sn.height = size
            self.sn.width = size
            self.sn.x = random.randint(a=0, b=1280)
            self.sn.y = random.randint(a=-0, b=720)
            self.add_actor(self.sn)

    def act(self, delta_time: float):
        super().act(delta_time)
        self.sn.y = self.sn.y + delta_time * 50
        print(self.sn.y)
        if self.sn.y > 820:
            self.sn.y = -100
            self.sn.x = random.randint(a=0, b=1280)



