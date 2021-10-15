import game

class Cloudy (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/cloudy.png")

class Landscape(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/landscape.png")

class Rain (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/rain.png")
    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 200
        if self.y > 720:
            self.y = -50

class Snow (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/snow.png")
    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 200
        if self.y > 720:
            self.y = -50

class Sun(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/sun.png")

class Sunny(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/sunny.png")

class Havaseso(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/snow.png")
        super().__init__("images/rain.png")
    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 200
        if self.y > 720:
            self.y = -50