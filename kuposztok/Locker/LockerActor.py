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

class SilverSnowMobile(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/SnowMobile_silver.png')


class SilverSledge(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/Sledge_silver.png')


class SilverSnowBoard(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/SnowBoard_silver.png')


class SilverSki(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/Ski_silver.png')

class GoldSnowMobile(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/SnowMobile_gold.png')


class GoldSledge(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/Sledge_gold.png')


class GoldSnowBoard(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/SnowBoard_gold.png')


class GoldSki(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/Ski_gold.png')


class Back(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/back_to_menu_button.png')

class SilverLock(game.scene2d.MyActor):
    def __init__(self):
        super().__init__('image/silver_lock.png')

class GoldLock(game.scene2d.MyActor):
    def __init__(self, image_url: str = ""):
        super().__init__('image/golden_lock.png')