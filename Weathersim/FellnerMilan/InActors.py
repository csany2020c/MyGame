import game
from Weathersim.FellnerMilan.Screen import *

class LandScape(game.scene2d.MyActor):
    def __init__(self, image_url: str = "../../!_resources/images/landscape.png"):
        super().__init__(image_url)

class Sunny(game.scene2d.MyActor):
    def __init__(self, image_url: str = "../../!_resources/images/sunny.png"):
        super().__init__(image_url)

class Sun(game.scene2d.MyActor):
    def __init__(self, image_url: str = "../../!_resources/images/sun.png"):
        super().__init__(image_url)

class Rain(game.scene2d.MyActor):

    def __init__(self, image_url: str = "../../!_resources/images/rain.png"):
        super().__init__(image_url)
        self.set_size(25,25)

class Rainy(game.scene2d.MyActor):

    def __init__(self, image_url: str = "../../!_resources/images/cloudy.png"):
        super().__init__(image_url)

class Snow(game.scene2d.MyActor):

    def __init__(self, image_url: str = "../../!_resources/images/snow.png"):
        super().__init__(image_url)


class MainMenu(game.scene2d.MyActor):
    def __init__(self, image_url: str = "mainmenu.png"):
        super().__init__(image_url)
        self.width = 300
        self.x = 640 - self.width / 2
        self.y = 600
        self.hitbox_scale_h = 0.4
        self.hitbox_scale_w = 0.6