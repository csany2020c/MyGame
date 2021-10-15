import Weathersim.bobicsbarnabas.menu.menuscreen
import game
import pygame
import random
from Weathersim.bobicsbarnabas.actors import *

class napsutesstage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.nap = sunActor()
        self.hatter = sunnyActor()
        self.hatter2 = landscapeActor()
        self.add_actor(self.hatter)
        self.add_actor(self.nap)
        self.add_actor(self.hatter2)
        self.nap.z_index = 1
        self.hatter.z_index = 0
        self.hatter2.z_index = 2
        self.nap.y = -100
        self.nap.x = 100

        self.hatter2.set_on_key_down_listener(self.key_down)
        self.hatter.set_on_key_down_listener(self.key_down2)

    def key_down(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()

    def key_down2(self, sender, event):
        if event.key == pygame.K_BACKSPACE:
            self.screen.game.set_screen(Weathersim.bobicsbarnabas.menu.menuscreen.menuscreen())

class havazasstage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.ho = snowActor()
        self.hatter = landscapeActor()
        self.hatter2 = cloudyActor()
        for i in range(150):
            self.ho = snowActor()
            self.add_actor(self.ho)
            self.ho.x = random.randint(20, 1230)
            self.ho.y = random.randint(-300, 590)
            self.ho.w = random.randint(40, 60)
            self.ho.h = random.randint(40, 60)
        self.add_actor(self.hatter)
        self.add_actor(self.hatter2)
        self.ho.z_index = 2
        self.hatter.z_index = 1
        self.hatter2.z_index = 0

        self.hatter2.set_on_key_down_listener(self.key_down)
        self.hatter.set_on_key_down_listener(self.key_down2)

    def key_down(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()

    def key_down2(self, sender, event):
        if event.key == pygame.K_BACKSPACE:
            self.screen.game.set_screen(Weathersim.bobicsbarnabas.menu.menuscreen.menuscreen())

class havasesostage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.ho = snowActor()
        self.eso = rainActor()
        self.hatter = cloudyActor()
        self.hatter2 = landscapeActor()
        for i in range(30):
            self.ho = snowActor()
            self.eso = rainActor()
            self.add_actor(self.ho)
            self.add_actor(self.eso)
            self.ho.x = random.randint(20, 1230)
            self.ho.y = random.randint(-300, 590)
            self.ho.w = random.randint(40, 60)
            self.ho.h = random.randint(40, 60)

            self.eso.x = random.randint(20, 1230)
            self.eso.y = random.randint(-300, 590)
            self.eso.w = random.randint(40, 60)
            self.eso.h = random.randint(40, 60)
        self.add_actor(self.hatter)
        self.add_actor(self.hatter2)
        self.eso.z_index = 3
        self.ho.z_index = 2
        self.hatter.z_index = 0
        self.hatter2.z_index = 1

        self.hatter2.set_on_key_down_listener(self.key_down)
        self.hatter.set_on_key_down_listener(self.key_down2)

    def key_down(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()

    def key_down2(self, sender, event):
        if event.key == pygame.K_BACKSPACE:
            self.screen.game.set_screen(Weathersim.bobicsbarnabas.menu.menuscreen.menuscreen())

class esostage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.eso = rainActor()
        self.hatter = landscapeActor()
        self.hatter2 = cloudyActor()
        for i in range(100):
            self.eso = rainActor()
            self.add_actor(self.eso)
            self.eso.x = random.randint(20, 1230)
            self.eso.y = random.randint(-300, 590)
            self.eso.w = random.randint(40, 60)
            self.eso.h = random.randint(40, 60)
        self.add_actor(self.hatter)
        self.add_actor(self.hatter2)
        self.eso.z_index = 2
        self.hatter.z_index = 1
        self.hatter2.z_index = 0

        self.hatter2.set_on_key_down_listener(self.key_down)
        self.hatter.set_on_key_down_listener(self.key_down2)

    def key_down(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()

    def key_down2(self, sender, event):
        if event.key == pygame.K_BACKSPACE:
            self.screen.game.set_screen(Weathersim.bobicsbarnabas.menu.menuscreen.menuscreen())