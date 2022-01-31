

import game
import random
import pygame


class BgActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/snow.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 500
        if self.y > 1080:
            self.y = -1080


class BgActor2(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/snow.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 500
        if self.y > 1080:
            self.y = -1080


class Visszagomb(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/back.png')


class Enemy(game.scene2d.MyActor):

    def __init__(self):
        self.credit = super().__init__('image/tree.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 500
        if self.y > 1180:
            self.y = random.Random().randint(-500, 0)
            self.x = random.Random().randint(0, 2000)


class Ski(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/Ski.png')
        self.width = 100
        self.height = 100


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


class Newgame(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/new_game.png')
        self.height = 75
        self.width = 125

class SportDrink(game.scene2d.MyActor):
    def __init__(self):
        self.SportDrink = super().__init__('image/SportDrink.png')

        self.width = 200
        self.height = 200

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 500
        if self.y > 1180:
            self.y = random.Random().randint(-500, 0)
            self.x = random.Random().randint(0, 2000)

class Trap(game.scene2d.MyActor):
    def __init__(self):
        self.SportDrink = super().__init__('image/Trap.png')

        self.width = 200
        self.height = 200

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 500
        if self.y > 1180:
            self.y = random.Random().randint(-500, 0)
            self.x = random.Random().randint(0, 2000)

class silverski(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/Ski_silver.png')
        self.width = 100
        self.height = 100


class silversnowboard(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/SnowBoard_silver.png')
        self.width = 100
        self.height = 100


class silversnowmobile(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/SnowMobile_silver.png')
        self.width = 200
        self.height = 200


class silversledge(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/Sledge_silver.png')
        self.width = 200
        self.height = 200

class goldski(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/Ski_gold.png')
        self.width = 100
        self.height = 100


class goldsnowboard(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/SnowBoard_gold.png')
        self.width = 100
        self.height = 100


class goldsnowmobile(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/SnowMobile_gold.png')
        self.width = 200
        self.height = 200


class goldsledge(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/Sledge_gold.png')
        self.width = 200
        self.height = 200


