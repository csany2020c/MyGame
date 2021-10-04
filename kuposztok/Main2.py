import pygame

import game
from game import *


class BgActor(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('image/map.jpg')


class Caracter(game.scene2d.MyActor):

    def __init__(self):
        super().__init__('image/my-caracter.png')


class GameStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.a = Caracter()
        bg = BgActor()
        bg.width = 1920
        bg.height = 1300
        self.a.y = 300
        self.a.x = 600
        self.add_actor(bg)
        self.add_actor(self.a)
        print(self.a)
        self.a.set_on_key_down_listener(self.key_down)

    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("W")
            self.a.y += 40
        if event.key == pygame.K_a:
            print("A")
            self.a.x -= 40
        if event.key == pygame.K_s:
            print("S")
            self.a.y -= 40
        if event.key == pygame.K_d:
            print("D")
            self.a.x += 40



class GameScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(r=0,g=0, b=255)
        self.add_stage(GameStage())



class Game(game.scene2d.MyGame):

    def __init__(self, width: int = 1920, height: int = 1080, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = GameScreen()


Game().run()
