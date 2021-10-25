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
        self.credit = super().__init__('image/back_to_menu_button.png')


class Joseph(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/my-caracter.png')


class Enemy(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/my-caracter.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 500
        if self.y > 1200:
            self.y = -200
            self.x = random.Random().randint(200, 1080)

class Car1(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/Car1.png')


class Car2(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/Car2.jpg')


class Car3(game.scene2d.MyActor):
    def __init__(self):
        self.credit = super().__init__('image/Car3.jpg')