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
        self.add_actor(self.sky)
        self.add_actor(self.bg)
        for i in range(10):
            self.ho = Snowactor()
            self.add_actor(self.ho)
            self.ho.w = random.Random().randint(50, 150)
            self.ho.y = random.Random().randint(-100, 0)
            self.ho.x = random.Random().randint(0, 1500)

        self.t = game.scene2d.MyTickTimer(interval=1.5, func=self.tikk)
        self.add_timer(self.t)

    def tikk(self, sender):
        for i in range(10):
            self.ho = Snowactor()
            self.add_actor(self.ho)
            self.ho.w = random.Random().randint(50, 150)
            self.ho.y = random.Random().randint(-100, 50)
            self.ho.x = random.Random().randint(0, 1400)


class Rainystage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.sky = Cloudysky()
        self.bg = Background()
        self.add_actor(self.sky)
        self.add_actor(self.bg)
        for i in range(40):
            self.eso = Rainactor()
            self.add_actor(self.eso)
            self.eso.w = random.Random().randint(50, 100)
            self.eso.y = random.Random().randint(-100, 50)
            self.eso.x = random.Random().randint(-350, 1200)

        self.t = game.scene2d.MyTickTimer(interval=0.5, func=self.tikk)
        self.add_timer(self.t)

    def tikk(self, sender):
        for i in range(20):
            self.eso = Rainactor()
            self.add_actor(self.eso)
            self.eso.w = random.Random().randint(50, 100)
            self.eso.y = random.Random().randint(-100, 50)
            self.eso.x = random.Random().randint(-350, 1200)

class SnowyRainstage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.sky = Cloudysky()
        self.bg = Background()
        self.add_actor(self.sky)
        self.add_actor(self.bg)
        for i in range(20):
            self.eso = Rainactor()
            self.add_actor(self.eso)
            self.eso.w = random.Random().randint(50, 100)
            self.eso.y = random.Random().randint(-100, 50)
            self.eso.x = random.Random().randint(-350, 1200)
        for i in range(20):
            self.ho = Snowactor2()
            self.add_actor(self.ho)
            self.ho.w = random.Random().randint(50, 150)
            self.ho.y = random.Random().randint(-100, 50)
            self.ho.x = random.Random().randint(-350, 1200)


        self.t = game.scene2d.MyTickTimer(interval=1.5, func=self.tikk)
        self.t2 = game.scene2d.MyTickTimer(interval=0.5, func=self.tikk2)
        self.add_timer(self.t)
        self.add_timer(self.t2)

    def tikk(self, sender):
        for i in range(15):
            self.ho = Snowactor2()
            self.add_actor(self.ho)
            self.ho.w = random.Random().randint(50, 150)
            self.ho.y = random.Random().randint(-100, 50)
            self.ho.x = random.Random().randint(-350, 1200)

    def tikk2(self, sender):
        for i in range(15):
            self.eso = Rainactor()
            self.add_actor(self.eso)
            self.eso.w = random.Random().randint(50, 100)
            self.eso.y = random.Random().randint(-100, 50)
            self.eso.x = random.Random().randint(-350, 1200)