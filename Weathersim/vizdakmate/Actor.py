import game

class Sun(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("sun.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(delta_time * 20)


class Background(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("landscape.png")

class Sunny(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("sunny.png")

class Rain(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("rain.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 300

class Snow(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("snow.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 300
class Cloudy(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("cloudy.png")