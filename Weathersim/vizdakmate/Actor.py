import game

class Sun(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("sun.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(delta_time * 20)
        if self.x + self.width < game.scene2d.MyGame.get_screen_width():
            self.x += delta_time * 120
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
        self.y += delta_time * 400

class Snow(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("snow.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 400
class Cloudy(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("cloudy.png")

class Sr(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("snow.png")
        super().__init__("rain.png")

class Menu(game.scene2d.MyActor):
    def __init__(self):
        super().__init__()

class MenuText(game.scene2d.MyLabel):

    def __init__(self, string: str = "Text") -> None:
            game.scene2d.MyLabel.__init__(self, string=string, font_name="arial")

class End(game.scene2d.MyActor):
    def __init__(self):
        super().__init__()

class EndText(game.scene2d.MyLabel):

    def __init__(self, string: str = "Text3") -> None:
            game.scene2d.MyLabel.__init__(self, string=string, font_name="arial")