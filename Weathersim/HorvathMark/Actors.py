import game
import pygame

class Cloudysky(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/cloudy.png")

class Sunnysky(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/sunny.png")

class Sunactor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/sun.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.r += 20 * delta_time
        if self.x >= -400:
            self.x -= 2 * delta_time
        if self.x <= -400:
            self.x -= 0 * delta_time
        self.y -= 10 * delta_time
        if self.w >= 450:
            self.w -= 5 * delta_time
        if self.w <= 450:
            self.w += 0 * delta_time

class Background(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/landscape.png")

class Snowactor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/snow.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.r -= 80 * delta_time
        self.x -= 20 * delta_time
        self.y += 40 * delta_time

class Rainactor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Kepek/rain.png")





