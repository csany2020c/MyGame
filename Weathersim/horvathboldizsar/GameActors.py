import game
from random import Random

class erdo(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/landscape.png')

class naposeg(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/sunny.png')

class felhoseg(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/cloudy.png')

class esocsepp(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/rain.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 120


class hopehely(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/snow.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(2)
        self.y += delta_time * 60

class nap(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/sun.png')
        self.x += 1000
        self.y += -200

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(0.2)

