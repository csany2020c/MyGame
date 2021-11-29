import pygame
import random
from bruhmomento.bruhScreen import *
from bruhmomento.bruhActor import *
from bruhmomento.menuscreen import *
from game.scene2d import MyPermanentTimer, MyOneTickTimer, MyBaseActor, MyTickTimer, MyIntervalTimer
import game


class bruhstage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.add_actor(lovedek())
        self.fohos = fohos()
        self.add_actor(self.fohos)
        self.kapu = kapu()
        self.add_actor(self.kapu)
        self.kapu.x = 70
        self.kapu.y = 200
        self.enemy1 = enemy1()
        self.add_actor(self.enemy1)
        self.enemy1.x = 1000
        self.enemy1.y = 300
        self.lovedek = lovedek()
        self.lovedek.x = 500
        self.lovedek.y = 200

        self.camera.tracking = self.fohos
        self.fohos.set_on_key_press_listener(self.press)

        f = open("map.txt", "r")

        y: int = 0
        while True:
            line = f.readline().strip()
            if line:
                x: int = 0
                for c in line:
                    a: MyBaseActor = None
                    if c == "w":
                        a = wall()
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
            self.camera.set_tracking_window(0.5, 0.6, 0.45, 0.5)
        if event.key == pygame.K_a:
            sender.x -= 10
            self.camera.set_tracking_window(0.5, 0.6, 0.45, 0.5)
        if event.key == pygame.K_w:
            sender.y -= 10
            self.camera.set_tracking_window(0.5, 0.6, 0.45, 0.5)
        if event.key == pygame.K_s:
            sender.y += 10
            self.camera.set_tracking_window(0.5, 0.6, 0.45, 0.5)

