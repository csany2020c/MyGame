import game
import pygame

class FatJordan(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/fatjordan.png")
        self.x += 500
        self.y += 250

class MenuText(game.scene2d.MyLabel):

    def __init__(self, string: str = "Text") -> None:
            game.scene2d.MyLabel.__init__(self, string=string, font_name="arial")