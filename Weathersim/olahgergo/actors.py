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

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(0.5)

class ho(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('images/snow.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y = self.y + delta_time * 90
        if self.y > 720:
            self.y = 20


class Eso(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('images/rain.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y = self.y + delta_time * 250
        if self.y > 720:
            self.y = 20



class menukep(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/alap2.png')

class imenukep(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/idojarasok2.png')


class esoskatt(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/esoskatt.png')

class naposkatt(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/naposkatt.png')

class havasesoskatt(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/havasesoskatt.png')

class havazaskatt(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/havazaskatt.png')

class vissza(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/vissza.png')

class kilep(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/kilepes.png')

class idojarasok(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/idojarasok.png')