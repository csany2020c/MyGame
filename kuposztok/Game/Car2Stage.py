import game
import pygame
from kuposztok.Game.GameActor import *
from kuposztok.Game.GameActor import *
import kuposztok
import random
from kuposztok.Menu.MenuBgActor import *
from game.scene2d import MyPermanentTimer, MyOneTickTimer, MyBaseActor, MyTickTimer, MyIntervalTimer


class Car1Stage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.bg = BgActor()
        self.bg.width = 2400
        self.bg.height = 1400
        self.bg.y = 0
        self.add_actor(self.bg)
        self.bg2 = BgActor2()
        self.bg2.y = -1080
        self.bg2.width = 2400
        self.bg2.height = 1400
        self.add_actor(self.bg2)
        self.button1 = Visszagomb()
        self.add_actor(self.button1)
        self.button1.width = 125
        self.button1.height = 75
        self.button1.y = 0
        self.button1.x = 0

        self.joseph = Car2()
        self.add_actor(self.joseph)
        self.joseph.width = 100
        self.joseph.height = 200
        self.joseph.x = 200
        self.joseph.y = 500

        for i in range(5):
            self.enemy = Enemy()
            self.add_actor(self.enemy)
            self.enemy.width = 100
            self.enemy.height = 100
            self.enemy.x = random.Random().randint(50, 1270)
            self.enemy.y = random.Random().randint(-500, 0)

        self.button1.set_on_mouse_down_listener(self.Klikk1)
        self.joseph.set_on_key_press_listener(self.iranyitas)

    def iranyitas(self, sender, event, a=10):
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        if event.key == pygame.K_d:
            if self.joseph.x < self.width - 200:
                self.joseph.x += a
        if event.key == pygame.K_a:
            if self.joseph.x > 200:
                self.joseph.x -= a
        if event.key == pygame.K_ESCAPE:
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())


    def Klikk1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())






