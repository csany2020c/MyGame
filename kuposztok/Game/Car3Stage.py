import game
import pygame
from kuposztok.Game.GameActor import *
from kuposztok.Game.GameActor import *
import kuposztok
import random
from kuposztok.Menu.MenuBgActor import *
from game.scene2d import MyPermanentTimer, MyOneTickTimer, MyBaseActor, MyTickTimer, MyIntervalTimer


class Car3Stage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
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

        self.joseph = SnowMobile()
        self.add_actor(self.joseph)
        self.joseph.width = 100
        self.joseph.height = 200
        self.joseph.x = 200
        self.joseph.y = 500
        self.t = MyIntervalTimer(func=self.Timer, start_time=0, stop_time=9223372036854775807)
        self.add_timer(self.t)

        self.score = 0
        self.scorelabel = game.scene2d.MyLabel("Score:" + str(self.score))
        self.add_actor(self.scorelabel)
        self.scorelabel.x = self.width - 250
        self.scorelabel.y = self.height - 50
        self.scorelabel.set_color(0, 0, 0)
        self.scorelabel.width = 100
        self.scorelabel.height = 50

        for i in range(5):
            self.enemy = Enemy()
            self.add_actor(self.enemy)
            self.enemy.width = 100
            self.enemy.height = 100
            self.enemy.x = random.Random().randint(0, 1080)
            self.enemy.y = random.Random().randint(-1080, 0)

        self.button1.set_on_mouse_down_listener(self.Klikk1)
        self.joseph.set_on_key_press_listener(self.iranyitas)

    def Timer(self, sender):
        self.score = self.score + 1
        self.scorelabel.set_text("Score:" + str(self.score))

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.joseph.overlaps(self.enemy):
            self.score = self.score - self.score
            print("Utkoztem")

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






