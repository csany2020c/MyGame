import game
from random import Random

class Alap(game.scene2d.MyActor):
    def __init__(self, image_url: str = "landscape.png"):
        super().__init__(image_url)

class Felhos(game.scene2d.MyActor):
    def __init__(self, image_url: str = "cloudy.png"):
        super().__init__(image_url)

class Eso(game.scene2d.MyActor):
    def __init__(self, image_url: str = "rain.png"):
        super().__init__(image_url)
        self.set_size(50,50)
        self.randomObj = Random()
        self.randomSpeed : int = self.randomObj.randint(4,8)
        self.x = self.randomObj.randint(0,1280)
        self.y = 0

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y = self.y + self.randomSpeed
        if self.y >= 720:
            self.y = 0


