import game
import random


class BgActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/snow.png')


class Visszagomb(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/back_to_menu_button.png')


class Joseph(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/my-caracter.png')


class Enemy(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/my-caracter.png')


class Car1(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/Car1.png')


class Car2(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/Car2.jpg')


class Car3(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/Car3.jpg')
