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

class FelhoImg(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/felhok.png")
