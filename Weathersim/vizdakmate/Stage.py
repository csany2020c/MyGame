import Weathersim.vizdakmate.Screen
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
        self.Sun = Sun()
        self.add_actor(Background())

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
            self.Rain.width = 50
            self.Rain.height = 50
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
        for i in range(400):
            self.Snow = Snow()
            self.add_actor(self.Snow)
            self.Snow.width = 50
            self.Snow.height = 50
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
            self.Rain.width = 50
            self.Rain.height = 50
            self.Rain.x = random.Random().randint(-1000, 1270)
            self.Rain.y = random.Random().randint(-5000, 770)
        for i in range(200):
            self.Snow = Snow()
            self.add_actor(self.Snow)
            self.Snow.width = 50
            self.Snow.height = 50
            self.Snow.x = random.Random().randint(-1000, 1270)
            self.Snow.y = random.Random().randint(-5000, 770)



    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("'QUIT'")
            quit()

class MenuStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()

        self.text = MenuText()
        self.add_actor(self.text)
        self.text.set_text("Időjárás szimuláció")
        self.text.set_width(80)
        self.text.set_height(80)
        self.text.x += 370
        self.text.y += 100
        self.text2 = MenuText()
        self.add_actor(self.text2)
        self.text2.set_text("Az F gomb lenyomásával elkezdődik az időjárás szimulálás")
        self.text2.set_width(50)
        self.text2.set_height(50)
        self.text2.x += 170
        self.text2.y += 300
        self.text3 = MenuText()
        self.add_actor(self.text3)
        self.text3.set_text("Az ESC gomb lenyomásával ki lehet lépni ")
        self.text3.set_width(50)
        self.text3.set_height(50)
        self.text3.x += 170
        self.text3.y += 360

        self.set_on_key_down_listener(self.gomb)
    def gomb(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()
        if event.key == pygame.K_f:
            self.screen.game.set_screen(Weathersim.vizdakmate.Screen.RainScreen())

class EndStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.text = EndText()
        self.add_actor(self.text)
        self.text.set_text("Vége:(")
        self.text.set_width(80)
        self.text.set_height(80)
        self.text.x += 500
        self.text.y += 300


        self.set_on_key_down_listener(self.gomb)
    def gomb(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()
        if event.key == pygame.K_f:
            self.screen.game.set_screen(Weathersim.vizdakmate.Screen.RainScreen())