import pygame
import game

class SunnyImg(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("images/sunny.png")

class SunImg(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("images/sun.png")

class LandscapeImg(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("images/landscape.png")

class RainImg(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("images/rain.png")
        self.set_width(45)
        self.set_height(45)

class CloudyImg(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("images/cloudy.png")

class SnowImg(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("images/snow.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 0:
            self.y += delta_time * 50
            self.rotate_with(delta_time * 25)

class FelhoImg(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/felhok.png")
