import game
from game.scene2d.MyScreen import *


class taj(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('!_resources/images/landscape.png')


class szurkeeg(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('!_resources/images/cloudy.png')


class ho(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('!_resources/images/snow.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 200
        if self.y > 720:
            self.y = -50


class eso(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('!_resources/images/rain.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 200
        if self.y > 720:
            self.y = -50


class button3(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('!_resources/images/havaseso.png')

class button5(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('!_resources/images/Vissza.png')