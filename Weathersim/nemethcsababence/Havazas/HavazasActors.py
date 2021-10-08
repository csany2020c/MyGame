import game
from game.scene2d.MyScreen import *


class taj(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/landscape.png')


class szurkeeg(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/cloudy.png')


class ho(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/snow.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 50
        self.rotate_with(delta_time * 20)
        if self.y > 720:
            self.y = -100


class button2(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/havazas.png')


class button5(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/Vissza.png')