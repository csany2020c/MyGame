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
    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(0.2)
class ActorSnow(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("snow.png")
        self.x = random.randint(0, 1270)
        self.y = random.randint(0, 500)
        self.width = random.randint(40, 70)
        self.height = random.randint(40, 70)
    def act(self, delta_time: float):
        super().act(delta_time)
        self.y = self.y + 3
        if self.y == 720:
            self.y = 0
            self.x = random.randint(0, 1000)
class ActorRain(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("rain.png")
        self.x = random.randint(-100, 1270)
        self.y = random.randint(0, 500)
        self.width = random.randint(40, 70)
        self.height = random.randint(40, 70)
    def act(self, delta_time: float):
        super().act(delta_time)
        self.y = self.y + 3
        if self.y == 720:
            self.y = 0
            self.x = random.randint(0, 1000)
