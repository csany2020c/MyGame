import random

import game


class taj(game.scene2d.MyActor):

    def __init__(self):
        self.taj = super().__init__('images/landscape.png')


class szurkeeg(game.scene2d.MyActor):

    def __init__(self):
        self.szeg = super().__init__('images/cloudy.png')


class eso(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/rain.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 100
        if self.y > 720:
            self.y = -50
            self.x = random.Random().randint(0, 1280)


class button1(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/eso2.png')


class windbag(game.scene2d.MyActor):

    def __init__(self):
        self.windbag = super().__init__('images/windbag.png')


class felho(game.scene2d.MyActor):

    def __init__(self):
        self.cloud = super().__init__('images/felho.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 200
        if self.x > 1300:
            self.x = 50


class button5(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/Vissza.png')
