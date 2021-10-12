import game
import pygame
import random
from Weathersim.FeketeFelix.Actorok import *
from game.scene2d import MyPermanentTimer, MyOneTickTimer, MyBaseActor, MyTickTimer, MyIntervalTimer

class SunnyStage(game.scene2d.MyStage):


    def __init__(self):
        super().__init__()
        self.add_actor(Sunny())
        self.add_actor(Land())
        self.add_actor(Madar())
        self.add_actor(Sunbuttoninfo())
        self.add_actor(Rainbuttoninfo())
        self.add_actor(Snowbuttoninfo())
        self.add_actor(Snowrainbuttoninfo())
        self.Sun = Sun()
        self.add_actor(self.Sun)


class RainStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.add_actor(Cloudy())
        self.add_actor(Land())
        self.add_actor(Sunbuttoninfo())
        self.add_actor(Rainbuttoninfo())
        self.add_actor(Snowbuttoninfo())
        self.add_actor(Snowrainbuttoninfo())

        self.t = MyTickTimer(interval=0.5, func=self.tikk)
        self.add_timer(self.t)

    def tikk(self, sender):
        for i in range(10):
            self.Rain = Rain()
            self.add_actor(self.Rain)
            self.Rain.x = random.Random().randint(-100, 1300)


class SnowStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.add_actor(Cloudy())
        self.add_actor(Land())
        self.add_actor(Sunbuttoninfo())
        self.add_actor(Rainbuttoninfo())
        self.add_actor(Snowbuttoninfo())
        self.add_actor(Snowrainbuttoninfo())

        self.t = MyTickTimer(interval=3, func=self.tikk)
        self.add_timer(self.t)

    def tikk(self, sender,):
        for i in range(6):
            self.Snow = Snow()
            self.add_actor(self.Snow)
            self.Snow.y = random.Random().randint(-40, 700)
            self.Snow.x = random.Random().randint(0, 720)


        if self.Snow.y > 500:
            self.remove_actor(self.Snow)




class SnowRainStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.add_actor(Cloudy())
        self.add_actor(Land())
        self.add_actor(Sunbuttoninfo())
        self.add_actor(Rainbuttoninfo())
        self.add_actor(Snowbuttoninfo())
        self.add_actor(Snowrainbuttoninfo())


        self.t = MyTickTimer(interval=2, func=self.tikk)
        self.add_timer(self.t)

    def tikk(self, sender, ):
        for i in range(4):
            self.Snow = Snow()
            self.add_actor(self.Snow)
            self.Snow.y = random.Random().randint(-40, 700)
            self.Snow.x = random.Random().randint(0, 720)

        if self.Snow.y > 500:
            self.remove_actor(self.Snow)

        for i in range(10):
            self.Rain = Rain()
            self.add_actor(self.Rain)
            self.Rain.x = random.Random().randint(-100, 1300)




