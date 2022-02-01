import retardszisza.menu_halal.MenuStage
from game.scene2d import MyLabel, ShapeType
from retardszisza.menu_halal.MenuScreen import *
import retardszisza.menu_halal.HalalActor
import retardszisza.menu_halal.HalalStage
import retardszisza.menu_halal.HalalScreen
from retardszisza.menu_halal.HalalScreen import *
import game
from retardszisza.Actor import *
import random
import pygame
import random

class GameStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.ut = UtActor()
        self.macska = szisza()
        self.kocsi1 = kocsi1()
        self.kocsi2 = kocsi2()
        self.kocsi3 = kocsi3()
        self.kocsi4 = kocsi4()
        self.fal = FalActor()
        self.fal2 = FalActor2()
        self.palyaszele1 = Palyaszele1()
        self.palyaszele2 = Palyaszele2()
        self.score: int = 170

        self.asdddsa = MyLabel("Score:")
        self.points = MyLabel("")
        self.add_actor(self.asdddsa)
        self.add_actor(self.points)
        self.add_actor(self.ut)
        self.add_actor(self.macska)
        self.add_actor(self.kocsi1)
        self.add_actor(self.kocsi2)
        self.add_actor(self.kocsi3)
        self.add_actor(self.kocsi4)
        self.add_actor(self.fal)
        self.add_actor(self.fal2)
        self.add_actor(self.palyaszele1)
        self.add_actor(self.palyaszele2)
        # pos
        self.ut.x = 0
        self.ut.y = -45

        self.macska.x = 100
        self.macska.y = 600

        self.kocsi1.x = 1000
        self.kocsi1.y = 550

        self.kocsi2.x = 1300
        self.kocsi2.y = 380

        self.kocsi3.x = 1000
        self.kocsi3.y = 190

        self.kocsi4.x = 1200
        self.kocsi4.y = 50

        self.fal.x = -300
        self.fal2.x = -140
        self.palyaszele1.y = 790
        self.palyaszele2.y = -100

        self.points.x = 150
        # hitbox
        self.macska.hitbox_scale_h = 0.5
        self.macska.hitbox_scale_w = 0.5
        self.macska.hitbox_shape = ShapeType.Circle

        self.kocsi1.hitbox_scale_h = 0.9
        self.kocsi1.hitbox_scale_w = 0.9

        self.kocsi2.hitbox_scale_h = 0.9
        self.kocsi2.hitbox_scale_w = 0.9

        self.kocsi3.hitbox_scale_h = 0.9
        self.kocsi3.hitbox_scale_w = 0.9

        self.kocsi4.hitbox_scale_h = 0.9
        self.kocsi4.hitbox_scale_w = 0.9

        self.macska.set_on_key_down_listener(self.button_down)

    def button_down(self, sender, event):
        if event.key == pygame.K_w:
            self.macska.y -= 190
        if event.key == pygame.K_s:
            self.macska.y += 190
        if event.key == pygame.K_d:
            self.macska.x += 120
        if event.key == pygame.K_a:
            self.macska.x -= 120

    def act(self, delta_time: float):
        super().act(delta_time)
        Overlaps: bool = False
        kocsirespawn1: bool = False
        kocsirespawn2: bool = False
        kocsirespawn3: bool = False
        kocsirespawn4: bool = False
        Palyaszel1: bool = False
        Palyaszel2: bool = False
        Fal2: bool = False

        for l in self.actors:
            if self.kocsi1.overlaps(self.macska):
                Overlaps = True
                break

            if self.kocsi2.overlaps(self.macska):
                Overlaps = True
                break

            if self.kocsi3.overlaps(self.macska):
                Overlaps = True
                break

            if self.kocsi4.overlaps(self.macska):
                Overlaps = True
                break

            if self.kocsi1.overlaps(self.fal):
                kocsirespawn1 = True

            if self.kocsi2.overlaps(self.fal):
                kocsirespawn2 = True

            if self.kocsi3.overlaps(self.fal):
                kocsirespawn3 = True

            if self.kocsi4.overlaps(self.fal):
                kocsirespawn4 = True

            if self.macska.overlaps(self.palyaszele1):
                Palyaszel1 = True

            if self.macska.overlaps(self.palyaszele2):
                Palyaszel2 = True

            if self.macska.overlaps(self.fal2):
                Fal2 = True

        if Overlaps:
            self.screen.game.set_screen(retardszisza.menu_halal.HalalScreen.halalscreen())  # HALAL

        if kocsirespawn1:
            self.kocsi1.x = random.randint(1300, 1500)
            self.score = self.score + 2
            print("Pontszám:")
            print(self.score)
            self.points.set_text(str(self.score))

        if kocsirespawn2:
            self.kocsi2.x = 1300
            self.score = self.score + 1
            print("Pontszám:")
            print(self.score)
            self.points.set_text(str(self.score))

        if kocsirespawn3:
            self.kocsi3.x = random.randint(1300, 1550)
            self.score = self.score + 3
            print("Pontszám:")
            print(self.score)
            self.points.set_text(str(self.score))

        if kocsirespawn4:
            self.kocsi4.x = random.randint(1300, 1550)
            self.score = self.score + 3
            print("Pontszám:")
            print(self.score)
            self.points.set_text(str(self.score))

        if Palyaszel1:
            self.macska.y = 600

        if Palyaszel2:
            self.macska.y = 30

        if Fal2:
            self.macska.x = -20

        if self.score > 20:
            self.kocsi4.act(delta_time / 3)
            self.kocsi3.act(delta_time / 3.5)
            self.kocsi2.act(delta_time / 2.5)
            self.kocsi1.act(delta_time / 1.5)

        if self.score > 50:
            self.kocsi4.act(delta_time / 6)
            self.kocsi3.act(delta_time / 4.5)
            self.kocsi2.act(delta_time / 3.5)
            self.kocsi1.act(delta_time / 2.5)

        if self.score > 100:
            self.kocsi4.act(delta_time / 9.5)
            self.kocsi3.act(delta_time / 8.8)
            self.kocsi2.act(delta_time / 6.9)
            self.kocsi1.act(delta_time / 5.4)

        if self.score > 180:
            self.kocsi4.act(delta_time * 1.8)
            self.kocsi3.act(delta_time * 1.5)
            self.kocsi2.act(delta_time * 1.4)
            self.kocsi1.act(delta_time * 1.2)

        if self.score > 250:
            quit()