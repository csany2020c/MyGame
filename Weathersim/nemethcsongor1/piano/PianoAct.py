import game
import pygame


class Feher(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("img/fehertile.png")


class Fekete(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("img/feketetile.png")


class Bg(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("img/blackboard.jpg")


class Gabriola(game.scene2d.MyLabel):
    def __init__(self, string: str = "MyText") -> None:
        game.scene2d.MyLabel.__init__(self, string=string, font_name="Gabriola")

    def act(self, delta_time: float):
        game.scene2d.MyLabel.act(self, delta_time)


class Klaviatura(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("img/klaviatura.png")
