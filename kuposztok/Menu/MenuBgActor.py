import game
import pygame


class MenuActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/menu.png')


class Button1(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/play_button.png')


class Button2(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/exit_button.png')


class Button3(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/credit_button.png')

class Button4(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/play_button.png')