import game
import pygame

class SunnySky(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("pictures/sunny.png")

class Sun(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("pictures/sun.png")

    def act(self, delta_time: float):
            super().act(delta_time)
            if self.x + self.width < game.scene2d.MyGame.get_screen_width():
                self.x += delta_time * 60
                self.rotate_with(delta_time * 20)

class Forest(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("pictures/landscape.png")

class CloudySky(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("pictures/cloudy.png")

class RainDrop(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("pictures/rain.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y +=delta_time * 100

class SnowDrop(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("pictures/snow.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y +=delta_time * 100

class MenuBg(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("pictures/menu.png")

class MenuText(game.scene2d.MyLabel):

    def __init__(self, string: str = "Text") -> None:
            game.scene2d.MyLabel.__init__(self, string=string, font_name="arial")