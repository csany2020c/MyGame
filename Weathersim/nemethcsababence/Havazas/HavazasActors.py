import game
from game.scene2d.MyScreen import *


class havastaj(game.scene2d.MyActor):

    def __init__(self):
        self.hotaj = super().__init__('images/snowlandscape.png')


class szurkeeg(game.scene2d.MyActor):

    def __init__(self):
        self.szeg = super().__init__('images/cloudy.png')


class ho(game.scene2d.MyActor):

    def __init__(self):
        self.ho = super().__init__('images/snow.png')

    def act(self, delta_time: float):
        super().act(delta_time),
        self.y += delta_time * 50
        self.rotate_with(delta_time * 20)
        if self.y > 720:
            self.y = -100


class button2(game.scene2d.MyActor):

    def __init__(self):
        self.butt2 = super().__init__('images/havazas2.png')


class button5(game.scene2d.MyActor):

    def __init__(self):
        self.butt5 = super().__init__('images/Vissza.png')