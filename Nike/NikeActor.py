import game
import pygame

class FatJordan(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/fatjordanact.png")
        self.x += 500
        self.y += 250


class MenuText(game.scene2d.MyLabel):

    def __init__(self, string: str = "Text") -> None:
            game.scene2d.MyLabel.__init__(self, string=string, font_name="arial")

class GameBg(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/bgpic.jpg")
        self.y = -450

class Sztrit(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/streett.png")
        self.y = 600

class FatJordanact(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/fatjordanact.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 100
        self.y += delta_time * 100