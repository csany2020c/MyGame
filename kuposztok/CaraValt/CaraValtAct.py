import game
import random


class BgActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/menu.png')


class BgActor2(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/menu.png')





class Visszagomb(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/back_to_menu_button.png')


class Joseph(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/my-caracter.png')


class Enemy(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/my-caracter.png')
