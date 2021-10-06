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

class ho(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('images/snow.png')
        self.speed = random.randint(a=20, b=70)

    def act(self, delta_time: float):
        super().act(delta_time)

        self.y = self.y + delta_time * self.speed
        if self.y > 820:
            self.y = -100
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




