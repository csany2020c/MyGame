import game
import pygame

class SunnyActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("sun.png")




class backgroundActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("landscape.png")



class skyActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("sunny.png")


class CloudActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("cloudy.png")


class SnowActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("snow.png")
    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 50
        self.rotate_with(delta_time * 20)
        if self.y > 740:
            self.y = -250

class RainActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("rain.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 50
        if self.y > 740:
            self.y = -50

class egyesgomb(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("1es gomb.PNG")

class kettesgomb(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("2es gomb.PNG")

class harmasgomb(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("3as gomb.PNG")

class vissza(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("asd.PNG")

class negyesgomb(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("4esgomb.PNG")
