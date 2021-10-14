import game
import random
from game.scene2d.MyScreen import *

class taj(game.scene2d.MyActor):
    def __init__(self, image_url: str = "resource/images/landscape.png"):
        super().__init__(image_url)

class felhos(game.scene2d.MyActor):
    def __init__(self, image_url: str = "resource/images/cloudy.png"):
        super().__init__(image_url)

class eg(game.scene2d.MyActor):
    def __init__(self, image_url: str = "resource/images/sunny.png"):
        super().__init__(image_url)

class eso(game.scene2d.MyActor):
    def __init__(self, image_url: str = "resource/images/rain.png"):
        super().__init__(image_url)
        self.width = 40

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * random.randint(200, 400)
        if self.y > 720:
            self.y = random.randint(-500, 0)

class ho(game.scene2d.MyActor):
    def __init__(self, image_url: str = "resource/images/snow.png"):
        super().__init__(image_url)
        self.width = 50

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * random.randint(200, 400)
        if self.y > 720:
            self.y = random.randint(-500, 0)

class nap(game.scene2d.MyActor):
    def __init__(self, image_url: str = "resource/images/sun.png"):
        super().__init__(image_url)

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 50
        if self.x > game.scene2d.MyGame.get_screen_width():
            self.x += delta_time * -100
        self.rotate_with(0.5)


class Gomb1(game.scene2d.MyLabel):
    def __init__(self):
        super().__init__("gomb1")

class Gomb2(game.scene2d.MyLabel):
    def __init__(self):
        super().__init__("gomb2")