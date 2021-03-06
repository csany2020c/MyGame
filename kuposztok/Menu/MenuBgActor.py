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
        super().__init__('image/shop_button.png')


class Button5(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/info_button.png')

class OptionsButton(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/options.png')
        self.width = 100
        self.height = 100