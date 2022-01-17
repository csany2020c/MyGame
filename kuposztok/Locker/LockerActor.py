import game
import pygame


class ShopBgActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/snow.png')


class DefaultSnowMobile(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/SnowMobile.png')


class DefaultSledge(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/Sledge.png')


class DefaultSnowBoard(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/SnowBoard.png')


class DefaultSki(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/Ski.png')


class Back(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/back_to_menu_button.png')

class SilverLock(game.scene2d.MyActor):
    def __init__(self):
        super().__init__('image/SilverLock1.png')

class GoldLock(game.scene2d.MyActor):
    def __init__(self, image_url: str = ""):
        super().__init__('image/GoldLock.png')