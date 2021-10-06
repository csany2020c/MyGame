import game
import random

class snow(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("snow.png")

class sun(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("sun.png")
        self.x += 850
        self.y -= 80

class sunny(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("sunny.png")

class cloudy(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("cloudy.png")

class landscape(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("landscape.png")