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
        self.y += delta_time * random.randint(100, 500)
        if self.y > 720:
            self.y = random.randint(-200, 0)

class ho(game.scene2d.MyActor):
    def __init__(self, image_url: str = "resource/images/snow.png"):
        super().__init__(image_url)
        self.width = 55

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * random.randint(100, 500)
        if self.y > 720:
            self.y = random.randint(-200, 0)

class nap(game.scene2d.MyActor):
    def __init__(self, image_url: str = "resource/images/sun.png"):
        super().__init__(image_url)
    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 30
        self.rotate_with(0.2)

class InfoHatter(game.scene2d.MyActor):
    def __init__(self, image_url: str = "resource/images/infobg.jpg"):
        super().__init__(image_url)

class Info1(game.scene2d.MyLabel):
    def __init__(self):
        super().__init__("Az időjárások között az 1-es, 2-es, 3-as, 4-es gombokkal tudsz váltogatni.", font_size=52)

class Info2(game.scene2d.MyLabel):
    def __init__(self):
        super().__init__("1- Napsütés, 2- Eső, 3- Hó, 4- Havaseső.", font_size=90)

class Info3(game.scene2d.MyLabel):
    def __init__(self):
        super().__init__("Ha lenyomod az ESCAPE  billentyűt, kilép.", font_size=60)

class Info4(game.scene2d.MyLabel):
    def __init__(self):
        super().__init__("Az F11 megnyomásával teljes képernyőre vált a program.")