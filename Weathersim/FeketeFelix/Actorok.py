import pygame
import game

class Sunny(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("resc/sunny.png")

class Sun(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("resc/sun.png")

class Rain(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("resc/rain.png")

class Land(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("resc/landscape.png")

class Snow(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("resc/snow.png")

class Cloudy(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("resc/cloudy.png")
