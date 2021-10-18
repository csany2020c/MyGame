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
        super().act(delta_time)
        self.y += delta_time * 50
        if self.y > 720:
            self.y = -50


class eso(game.scene2d.MyActor):

    def __init__(self):
        self.eso = super().__init__('images/rain.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 100
        if self.y > 720:
            self.y = -50


class button3(game.scene2d.MyActor):

    def __init__(self):
        self.butt3 = super().__init__('images/havaseso2.png')


class button5(game.scene2d.MyActor):

    def __init__(self):
        self.butt5 = super().__init__('images/Vissza.png')