import game
import random

class ActorA(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("landscape.png")

    def act(self, delta_time: float):
        super().act(delta_time)


class ActorB(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("sunny.png")

    def act(self, delta_time: float):
        super().act(delta_time)

class ActorC(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("cloudy.png")

    def act(self, delta_time: float):
        super().act(delta_time)

class ActorD(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("sun.png")
        self.x = 600
        self.y = 0

class ActorSnow(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("snow.png")
        self.speed = 0

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * self.speed

