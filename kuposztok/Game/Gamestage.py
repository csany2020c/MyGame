import game
import pygame
from kuposztok.Game.GameActor import *
from kuposztok.Game.GameActor import *
import kuposztok
import random
from kuposztok.Menu.MenuBgActor import *
from game.scene2d import MyPermanentTimer, MyOneTickTimer, MyBaseActor, MyTickTimer, MyIntervalTimer


class GameStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.bg = BgActor()
        self.bg.width = 2400
        self.bg.height = 1400
        self.add_actor(self.bg)
        self.button1 = Visszagomb()
        self.add_actor(self.button1)
        self.button1.width = 125
        self.button1.height = 75
        self.button1.y = 0
        self.button1.x = 0

        self.joseph = Joseph()
        self.add_actor(self.joseph)
        self.joseph.width = 100
        self.joseph.height = 200
        self.joseph.x = 200
        self.joseph.y = 500

        self.enemy = Enemy()
        self.add_actor(self.enemy)
        self.enemy.width = 100
        self.enemy.height = 100
        self.enemy.x = random.Random().randint(50, 1870)
        self.enemy.y = random.Random().randint(50, 1030)

        self.button1.set_on_mouse_down_listener(self.Klikk1)
        self.joseph.set_on_key_press_listener(self.iranyitas)

    def iranyitas(self, sender, event, a=10):
        if event.key == pygame.K_d:
            self.joseph.x += a
        if event.key == pygame.K_a:
            self.joseph.x -= a
        if event.key == pygame.K_ESCAPE:
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())

    def Klikk1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())

    def update(self):
        self.bg = MenuActor()
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        if self.bg.y == self.screen.height + self.screen.height:
            self.bg.set_y(self.bg.y - self.screen.height + 20)
        else:
            self.bg.y = self.bg.y + 20

        if self.bg.y == self.screen.height + self.screen.height:
            self.bg.set_y(self.bg.y - self.screen.height)
        else:
            self.bg.y = self.bg.y + 20

        if self.bg.y == self.screen.height + self.screen.height:
            self.bg.set_y(self.bg.y - self.screen.height)
        else:
            self.bg.y = self.bg.y + 20





