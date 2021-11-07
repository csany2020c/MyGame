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


class PlayButton(game.scene2d.MyActor):
    def __init__(self):
        super().__init__('image/play_button.png')


class Enemy(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/tree.png')


class Ski(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/Ski.png')
        self.width = 100
        self.height = 100


class Multi(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/multi.png')


class Single(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/single.png')


class SnowBoard(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/SnowBoard.png')
        self.width = 100
        self.height = 100


class SnowMobile(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/SnowMobile.png')
        self.width = 200
        self.height = 200


class Sledge(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/Sledge.png')
        self.width = 200
        self.height = 200

