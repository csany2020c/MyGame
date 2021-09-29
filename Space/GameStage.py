import random

import pygame

import game
from EnemyActor import *
from Arial32 import *
from game.scene2d import MyPermanentTimer, MyOneTickTimer, MyBaseActor


class GameStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.b = Enemy1Actor()
        self.add_actor(self.b)
        for j in range(0, 10):
            for i in range(0, 10):
                e = Enemy1Actor()
                e.set_on_mouse_move_listener(self.click)
                e.y = i * 40
                e.x = j * 40
                e.width = 20
                e.height = 20
                self.add_actor(e)
        self.b.z = 3000
        self.a = Arial32()
        #self.a.hitbox_shape = game.simpleworld.ShapeType.Circle
        self.add_actor(self.a)
        self.a.set_text("asd")
        self.a.set_bg_red(0)
        self.a.set_font_underline(True)
        self.a.set_alpha(128)
        self.atxt = game.scene2d.MyLabel("ASD")
        self.add_actor(self.atxt)
        self.asd = game.scene2d.MyActor("resources/images/enemy1.png")
        self.asd.x = 200
        self.asd.w = 200
        self.asd.hitbox_scale_w = 0.4
        self.asd.hitbox_scale_h = 0.4
        self.asd.hitbox_shape = game.simpleworld.ShapeType.Circle
        self.add_actor(self.asd)
        self.asd.debug = True
        # self.set_on_key_down_listener(self.key_down)
        self.asd.set_on_mouse_down_listener(self.click)
        self.asd.set_on_key_down_listener(self.key_down)

    def key_down(self, sender, event):
        # if isinstance(sender, MyBaseActor):
        #     sender.
        print(sender)
        print(event)
        if event.key == pygame.K_BACKSPACE:
            print("FFFFFFFFFFFFFFFFFFFFFFFFFFF")
            self.asd.x += 40

    def click(self, sender, event):
        print(event)
        #if event.button == 1:
        sender.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - sender.w)
        sender.y = random.Random().randint(0, game.scene2d.MyGame.get_screen_height() - sender.h)

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.a.overlaps(self.asd):
            print("OOOOO")
        #self.actors[20].width = 200
        #self.b.r -= 2
        # print(self.asd.overlaps(self.a))




