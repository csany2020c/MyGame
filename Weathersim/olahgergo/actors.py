import game
import random


class hatterkep(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('images/landscape.png')


class felhoeg(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('images/cloudy.png')

class vilagoseg(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('images/sunny.png')

class napnap(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('images/sun.png')

class ho(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('images/snow.png')
        self.speed = random.randint(a=20, b=70)

    def act(self, delta_time: float):
        super().act(delta_time)

        self.y = self.y + delta_time * self.speed
        if self.y > 760:
            self.y = 50
            self.x = random.randint(a=0, b=1280)
            self.speed = random.randint(a=20, b=70)


class Rain(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('images/rain.png')
        self.speed = random.randint(a=200, b=300)

    def act(self, delta_time: float):
        super().act(delta_time)

        self.y = self.y + delta_time * self.speed
        if self.y > 820:
            self.y = -100
            self.x = random.randint(a=0, b=1280)
            self.speed = random.randint(a=200, b=300)

class esoke(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/esos.png')

class napos(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/napos.png')

class havazas(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/havazas.png')

class havasesos(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/havaseso.png')


class menukep(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/alap.png')

class semmi(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/semmi.png')