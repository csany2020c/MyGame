import game

class Sun(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/sun.png")

class Landscape(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/landscape.png")

class Sunny(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/sunny.png")

class Snow (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/snow.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 200
        if self.y > 720:
            self.y = -50

class Cloudy (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/cloudy")

class Rain (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/rain")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 200
        if self.y > 720:
            self.y = -50