from Weathersim.TothAkos.actor import *
import random
import pygame
import Weathersim.TothAkos.screen

class Sunnystage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.b = Sun()
        self.add_actor(Sunny())
        self.add_actor(Landscape())
        self.Sun = Sun()
        self.add_actor(self.Sun)
        self.Sun.x = 800
        self.set_on_key_down_listener(self.gombok)
    def gombok(self,sender,event):
        if event.key == pygame.K_ESCAPE:
            quit()
        if event.key == pygame.K_1:
            self.screen.game.set_screen(Weathersim.TothAkos.screen.Sunnyscr())
        if event.key == pygame.K_2:
            self.screen.game.set_screen(Weathersim.TothAkos.screen.Snowyscr())
        if event.key == pygame.K_3:
            self.screen.game.set_screen(Weathersim.TothAkos.screen.Rainyscr())
        if event.key == pygame.K_4:
            self.screen.game.set_screen(Weathersim.TothAkos.screen.Havasesoscr())

class Snowystage (game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.b = Cloudy()
        self.add_actor(self.b)
        self.landscape = Landscape()
        self.add_actor(self.landscape)
        for i in range(40):
            self.Snow = Snow()
            self.add_actor(self.Snow)
            self.Snow.x = random.Random().randint(-100, 1280)
            self.Snow.y = random.Random().randint(-100, 720)
        self.set_on_key_down_listener(self.gombok)
    def gombok(self,sender,event):
        if event.key == pygame.K_ESCAPE:
            quit()
        if event.key == pygame.K_1:
            self.screen.game.set_screen(Weathersim.TothAkos.screen.Sunnyscr())
        if event.key == pygame.K_2:
            self.screen.game.set_screen(Weathersim.TothAkos.screen.Snowyscr())
        if event.key == pygame.K_3:
            self.screen.game.set_screen(Weathersim.TothAkos.screen.Rainyscr())
        if event.key == pygame.K_4:
            self.screen.game.set_screen(Weathersim.TothAkos.screen.Havasesoscr())

class Rainystage (game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.b = Cloudy()
        self.add_actor(self.b)
        self.landscape = Landscape()
        self.add_actor(self.landscape)
        for i in range(40):
            self.Rain = Rain()
            self.add_actor(self.Rain)
            self.Rain.x = random.Random().randint(-100, 1280)
            self.Rain.y = random.Random().randint(-100, 720)
        self.set_on_key_down_listener(self.gombok)
    def gombok(self,sender,event):
        if event.key == pygame.K_ESCAPE:
            quit()
        if event.key == pygame.K_1:
            self.screen.game.set_screen(Weathersim.TothAkos.screen.Sunnyscr())
        if event.key == pygame.K_2:
            self.screen.game.set_screen(Weathersim.TothAkos.screen.Snowyscr())
        if event.key == pygame.K_3:
            self.screen.game.set_screen(Weathersim.TothAkos.screen.Rainyscr())
        if event.key == pygame.K_4:
            self.screen.game.set_screen(Weathersim.TothAkos.screen.Havasesoscr())

class Havasesostage (game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.cloudy = Cloudy()
        self.add_actor(self.cloudy)
        self.landscape = Landscape()
        self.add_actor(self.landscape)
        self.snow = Snow()
        self.add_actor(self.snow)
        for i in range(40):
            self.Snow = Snow()
            self.add_actor(self.Snow)
            self.Snow.x = random.Random().randint(-100, 1280)
            self.Snow.y = random.Random().randint(-100, 720)
        self.rain = Rain()
        self.add_actor(self.rain)
        for i in range(100):
            self.Rain = Rain()
            self.add_actor(self.Rain)
            self.Rain.x = random.Random().randint(-100, 1280)
            self.Rain.y = random.Random().randint(-100, 720)
        self.set_on_key_down_listener(self.gombok)
    def gombok(self,sender,event):
        if event.key == pygame.K_ESCAPE:
            quit()
        if event.key == pygame.K_1:
            self.screen.game.set_screen(Weathersim.TothAkos.screen.Sunnyscr())
        if event.key == pygame.K_2:
            self.screen.game.set_screen(Weathersim.TothAkos.screen.Snowyscr())
        if event.key == pygame.K_3:
            self.screen.game.set_screen(Weathersim.TothAkos.screen.Rainyscr())
        if event.key == pygame.K_4:
            self.screen.game.set_screen(Weathersim.TothAkos.screen.Havasesoscr())