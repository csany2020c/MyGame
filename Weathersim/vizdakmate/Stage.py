import game
from Weathersim.vizdakmate.Actor import *
#from game.scene2d import MyTickTimer
import random
import pygame


class SunnyStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.set_on_key_down_listener(self.key_down)
        self.add_actor(Sunny())
        self.Rain = Rain()
        self.add_actor(Background())
        self.Sun = Sun()
        self.add_actor(self.Sun)

    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("'QUIT'")
            quit()

class RainStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.add_actor(Cloudy())
        self.add_actor(Background())
        self.set_on_key_down_listener(self.key_down)
        for i in range(200):
            self.Rain = Rain()
            self.add_actor(self.Rain)
            self.Rain.width = 60
            self.Rain.height = 60
            self.Rain.x = random.Random().randint(-1000, 1270)
            self.Rain.y = random.Random().randint(-3000, 770)

    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("'QUIT'")
            quit()

class SnowStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.add_actor(Cloudy())
        self.add_actor(Background())
        self.set_on_key_down_listener(self.key_down)
        for i in range(200):
            self.Snow = Snow()
            self.add_actor(self.Snow)
            self.Snow.width = 60
            self.Snow.height = 60
            self.Snow.x = random.Random().randint(-1000, 1270)
            self.Snow.y = random.Random().randint(-5000, 770)

    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("'QUIT'")
            quit()

class BackgroundStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()

class CloudyStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.Cloudy = Cloudy

class SrStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.set_on_key_down_listener(self.key_down)
        self.add_actor(Cloudy())
        self.add_actor(Background())

        for i in range(200):
            self.Rain = Rain()
            self.add_actor(self.Rain)
            self.Rain.width = 60
            self.Rain.height = 60
            self.Rain.x = random.Random().randint(-1000, 1270)
            self.Rain.y = random.Random().randint(-3000, 770)
        for i in range(200):
            self.Snow = Snow()
            self.add_actor(self.Snow)
            self.Snow.width = 60
            self.Snow.height = 60
            self.Snow.x = random.Random().randint(-1000, 1270)
            self.Snow.y = random.Random().randint(-5000, 770)



    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("'QUIT'")
            quit()
