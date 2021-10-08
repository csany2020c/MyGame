import game

class rain(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("rain.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 50
        if self.y > 720:
            self.y = -100

class snow(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("snow.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 50
        self.rotate_with(delta_time * 20)
        if self.y > 720:
            self.y = -100

class sun(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("sun.png")
        self.y = -100
    def act(self, delta_time: float):
        super().act(delta_time)
        if self.x + self.width < game.scene2d.MyGame.get_screen_width():
            self.x += delta_time * 40
        self.rotate_with(delta_time * 10)

class sunny(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("sunny.png")

class cloudy(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("cloudy.png")

class landscape(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("landscape.png")