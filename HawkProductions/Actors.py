from random import Random

import game
import HawkProductions.over.OverScreen
import pygame
import random


class Sellect(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/select.jpg")


class Title(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/title.png")


class Startb(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/startb.png")

    def act(self, delta_time: float):
        super().act(delta_time)


class Exit(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/quitb.png")

    def act(self, delta_time: float):
        super().act(delta_time)


class Pile(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/oszlop.png")

    def act(self, delta_time: float):
        self.x -= 150 * delta_time
        if self.x < 0:
            self.x = 1280


class Pile_a(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/oszlop-a.png")

    def act(self, delta_time: float):
        self.x -= 150 * delta_time
        if self.x < 0:
            self.x = 1280


class Pile_f(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/oszlop-f.png")

    def act(self, delta_time: float):
        self.x -= 150 * delta_time
        if self.x < 0:
            self.x = 1280


class Bg(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/bg.png")


class Arrow(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/nyil_main.png")


class Arrow_w(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/arrow.png")


class Arrow2(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/nyil_main_f.png")


class Info(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/info.png")


class Coin(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/coin.png")

    def act(self, delta_time: float):
        self.x -= 150 * delta_time
        if self.x < 0:
            self.x = 1280


class Selectimage(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/original.png")


class Gun(game.scene2d.MyActor):
    def act(self, delta_time: float):
        self.y += 75 * delta_time
        if self.r < 0:
            self.r += 7.5 * delta_time * (-self.r)
        else:
            self.r -= 7.5 * delta_time * self.r

        if self.y < 0:
            self.stage.screen.game.set_screen(HawkProductions.over.OverScreen.OverScreen2())
        if self.y > 720:
            self.stage.screen.game.set_screen(HawkProductions.over.OverScreen.OverScreen3())


class Deagle(Gun):
    def __init__(self):
        super().__init__("image/bid.png")

class Deagle_2(Gun):
    def __init__(self):
        super().__init__("image/original.png")

class Deagle_3(Gun):
    def __init__(self):
        super().__init__("image/luckyspade1.png")


class Deagle_4(Gun):
    def __init__(self):
        super().__init__("image/goldengun1.png")


class Deagle_5(Gun):
    def __init__(self):
        super().__init__("image/observator88.png")


class Sarga(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/sarga.png")


class Piros(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/piros.png")


class Win(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/win.png")


# class Gaymover(game.scene2d.MyActor):
#     def __init__(self):
#         gaym = ["image/Gameover.png", "image/Gameover2.png", "image/Gamover3.png", "image/Gameover4.png", "image/Gamover5.png", "image/Gameover6.png"]
#         super().__init__(random.choice(gaym))


class Logo(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/Logo.png")
