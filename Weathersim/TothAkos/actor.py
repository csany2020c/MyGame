import game
import pygame
from game.scene2d import MyTickTimer, MyIntervalTimer


class Sun(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/sun.png")
        self.asd = None
        self.life = 5
        self.set_on_key_down_listener()


    def Act(self, delta_time: float):
        super().act(delta_time)
        if self.x + self.width < game.scene2d.MyGame.get_screen_width():
            self.x += delta_time * 60
            self.rotate_with(delta_time * 20)


class Landscape(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/landscape.png")

class Sunny(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/sunny.png")
