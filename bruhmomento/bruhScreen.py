import game
from bruhmomento.bruhActor import *


import pygame
import random
from bruhmomento.bruhScreen import *
from bruhmomento.bruhActor import *
from game.scene2d import MyPermanentTimer, MyOneTickTimer, MyBaseActor, MyTickTimer, MyIntervalTimer
import game

class menuscreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.r = 0
        self.g = 100
        self.b = 0
        self.add_stage(menustage())

class menustage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.add_actor(startgomb())
        self.startgomb = startgomb()
        self.startgomb.set_on_mouse_down_listener(self.inditas)

    #def Click(self, sender,event):
    #    if event.button == 1:
    #        self.screen = bruhScreen()

    def inditas(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.screen.game.set_screen(bruhScreen(map.txt))

class bruhstage(game.scene2d.MyStage):

    def __init__(self, map: str):
        super().__init__()
        self.lovedek = lovedek()
        self.add_actor(self.lovedek)
        self.fohos = fohos()
        self.add_actor(self.fohos)
        self.kapu = kapu()
        self.add_actor(self.kapu)
        self.kapu.x = 3400
        self.kapu.y = 820
        self.kapu.rotate_with(270)
        self.lovedek.x = 500
        self.lovedek.y = 200
        self.enemy1 = enemy1()
        self.add_actor(self.enemy1)
        self.enemy1.x = 452
        self.enemy1.y = 384
        self.enemy2 = enemy1()
        self.add_actor(self.enemy2)
        self.enemy2.x = 70
        self.enemy2.y = 762
        self.enemy3 = enemy2()
        self.add_actor(self.enemy3)
        self.enemy3.x = 2510
        self.enemy3.y = 750
        self.kulcs = kulcs()
        self.add_actor(self.kulcs)
        self.kulcs.x = 150
        self.kulcs.y = 350
        self.fal = wall()
        self.zartajto = zartajto()
        self.add_actor(self.zartajto)
        self.zartajto.x = 3000
        self.zartajto.y = 750


        self.camera.tracking = self.fohos
        self.fohos.set_on_key_press_listener(self.press)

        f = open(map, "r")

        y: int = 0
        while True:
            line = f.readline().strip()
            if line:
                x: int = 0
                for c in line:
                    a: MyBaseActor = None
                    if c == "w":
                        a = wall()
                    if c == "r":
                        a = wall2()
                    if c == "g":
                        a = eastereggtabla()
                    if c == "h":
                        a = easteregg()
                    if c == "k":
                        self.fohos = fohos()
                        a = self.fohos
                    if a is not None:
                        a.x = x * 64
                        a.y = y * 64
                        self.add_actor(a)
                        print(c)
                    x += 1
            else:
                break
            y += 1

        f.close()

    def press(self, sender, event):
        # print(event.key)
        if event.key == pygame.K_d:
            sender.x += 10
            self.camera.set_tracking_window(0.2, 0.4, 0.6, 0.4)
        if event.key == pygame.K_a:
            sender.x -= 10
            self.camera.set_tracking_window(0.6, 0.4, 0.2, 0.4)
        if event.key == pygame.K_w:
            sender.y -= 10
            self.camera.set_tracking_window(0.4, 0.6, 0.4, 0.2)
        if event.key == pygame.K_s:
            sender.y += 10
            self.camera.set_tracking_window(0.4, 0.2, 0.4, 0.6)

    def act(self, delta_time: float):
        super().act(delta_time)
        # print(self.lovedek)
        if self.kapu.overlaps(other=self.fohos):
            self.screen.game.set_screen(bruhScreen("map2.txt"))
        if self.enemy1.overlaps(self.lovedek):
            self.enemy1.remove_from_stage()
        if self.fohos.overlaps(self.kulcs):
            self.zartajto.remove_from_stage()
            self.kulcs.remove_from_stage()


class bruhScreen(game.scene2d.MyScreen):
    def __init__(self, map: str):
        super().__init__()
        self.r = 0
        self.g = 100
        self.b = 0
        self.add_stage(bruhstage(map))

class brruhScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.r = 50
        self.g = 41
        self.b = 40
        self.add_stage(bruhstage())

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.elapsed_time > 1:
            self.game.screen = bruhScreen()