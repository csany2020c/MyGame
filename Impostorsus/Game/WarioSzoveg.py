import game
import pygame


class MenuSzoveg(game.scene2d.MyLabel):

    def __init__(self, string: str = "MyText") -> None:
            game.scene2d.MyLabel.__init__(self, string=string, font_name="arial")
