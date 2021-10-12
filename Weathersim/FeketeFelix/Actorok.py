import pygame
import game

class Sunny(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("resc/sunny.png")

class Sun(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("resc/sun.png")
        self.x += 800
        self.y += 5

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(1)

class Rain(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("resc/rain.png")

    def act(self, delta_time: float):
            super().act(delta_time)
            self.y += 20
            self.x += delta_time * 55

class Land(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("resc/landscape.png")

class Snow(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("resc/snow.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(5)
        self.y += delta_time * 55
        self.x += delta_time * 55


class Cloudy(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("resc/cloudy.png")

class Madar(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("resc/madar.png")

    def act(self, delta_time: float):
            super().act(delta_time)
            self.x += 10

class Sunbuttoninfo(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("resc/sunbuttoninfo.png")
        self.x += 300
        self.y += 550

class Rainbuttoninfo(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("resc/rainbuttoninfo.png")
        self.x += 1
        self.y += 600

class Snowbuttoninfo(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("resc/snowbuttoninfo.png")
        self.x += 100
        self.y += 600

class Snowrainbuttoninfo(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("resc/snowrainbuttoninfo.png")
        self.x += 225
        self.y += 600