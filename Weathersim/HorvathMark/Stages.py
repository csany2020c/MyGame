from Weathersim.HorvathMark.Actors import *
import random

class Sunnystage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.sky = Sunnysky()
        self.sun = Sunactor()
        self.bg = Background()
        self.add_actor(self.sky)
        self.add_actor(self.sun)
        self.add_actor(self.bg)
        self.sun.x = 800
        self.sun.y = 200
        self.sun.w = 600

class Snowystage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.sky = Cloudysky()
        self.bg = Background()
        self.ho = Snowactor()
        self.add_actor(self.sky)
        self.add_actor(self.bg)
        for i in range(40):
            self.add_actor(self.ho)
            self.ho.y = random.Random().randint(-10, 100)
            self.ho.x = random.Random().randint(0, 800)

        self.t = game.scene2d.MyTickTimer(interval=2, func=self.tikk)
        self.add_timer(self.t)

    def tikk(self, sender):
        for i in range(20):
            self.add_actor(self.ho)
            self.ho.y = random.Random().randint(-40, 60)
            self.ho.x = random.Random().randint(800, 1000)
