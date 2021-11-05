import game
from Weathersim.RigoDonat.actor import *
from Weathersim.RigoDonat.screen import *
import Weathersim.RigoDonat.screen
import random
import pygame

class MenuStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.MenuBg = MenuBg()
        self.add_actor(MenuBg())
        self.text = MenuText()
        self.add_actor(self.text)
        self.text.set_text("Weather Simulation")
        self.text.set_alpha(500)
        self.text.set_width(80)
        self.text.set_height(80)
        self.text.x += 360
        self.text.y += 50
        self.Sim = MenuText()
        self.add_actor(self.Sim)
        self.Sim.set_text("Start")
        self.Sim.set_alpha(500)
        self.Sim.set_width(150)
        self.Sim.set_height(150)
        self.Sim.x += 500
        self.Sim.y += 150
        self.Sim.set_on_mouse_down_listener(self.play)
        self.Exit = MenuText()
        self.add_actor(self.Exit)
        self.Exit.set_text("Exit")
        self.Exit.set_alpha(500)
        self.Exit.set_width(100)
        self.Exit.set_height(100)
        self.Exit.x += 550
        self.Exit.y += 300
        self.Exit.set_on_mouse_down_listener(self.click)

    def play(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.screen.game.set_screen(Weathersim.RigoDonat.screen.Sunny())
                print("'Start'")

    def click(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("'QUIT'")
                quit()


class SunnyStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.SunnySky = SunnySky()
        self.add_actor(SunnySky())
        self.Sun = Sun()
        self.add_actor(self.Sun)
        self.Forest = Forest()
        self.add_actor(Forest())

class RainStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.CloudySky = CloudySky()
        self.add_actor(CloudySky())
        self.add_actor(Forest())
        for a in range(1000):
            self.RainDrop = RainDrop()
            self.add_actor(self.RainDrop)
            self.RainDrop.width = 30
            self.RainDrop.height = 30
            self.RainDrop.x = random.Random().randint(-1500, 1500)
            self.RainDrop.y = random.Random().randint(-1000, 1000)

        self.t = game.scene2d.MyTickTimer(interval=0.15, func=self.tikk)
        self.add_timer(self.t)

    def tikk(self, sender):
        for i in range(5):
            self.RainDrop = RainDrop()
            self.add_actor(self.RainDrop)
            self.RainDrop.w = random.Random().randint(30, 30)
            self.RainDrop.y = random.Random().randint(-100, 50)
            self.RainDrop.x = random.Random().randint(0, 1400)


class SnowStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.CloudySky = CloudySky()
        self.add_actor(CloudySky())
        self.add_actor(Forest())
        for a in range(1000):
            self.SnowDrop = SnowDrop()
            self.add_actor(self.SnowDrop)
            self.SnowDrop.width = 30
            self.SnowDrop.height = 30
            self.SnowDrop.x = random.Random().randint(-1500, 1500)
            self.SnowDrop.y = random.Random().randint(-1000, 1000)

        self.t = game.scene2d.MyTickTimer(interval=1.5, func=self.tikk)
        self.add_timer(self.t)

    def tikk(self, sender):
        for i in range(50):
            self.SnowDrop = SnowDrop()
            self.add_actor(self.SnowDrop)
            self.SnowDrop.w = random.Random().randint(30, 30)
            self.SnowDrop.y = random.Random().randint(-100, 50)
            self.SnowDrop.x = random.Random().randint(0, 1400)

class RainSnowStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.CloudySky = CloudySky()
        self.add_actor(CloudySky())
        self.add_actor(Forest())
        for a in range(700):
            self.RainDrop = RainDrop()
            self.add_actor(self.RainDrop)
            self.RainDrop.width = 30
            self.RainDrop.height = 30
            self.RainDrop.x = random.Random().randint(-1500, 1500)
            self.RainDrop.y = random.Random().randint(-1000, 1000)
        for a in range(700):
            self.SnowDrop = SnowDrop()
            self.add_actor(self.SnowDrop)
            self.SnowDrop.width = 30
            self.SnowDrop.height = 30
            self.SnowDrop.x = random.Random().randint(-1500, 1500)
            self.SnowDrop.y = random.Random().randint(-1000, 1000)

        self.t = game.scene2d.MyTickTimer(interval=1.5, func=self.tikk)
        self.add_timer(self.t)

    def tikk(self, sender):
        for i in range(50):
            self.SnowDrop = SnowDrop()
            self.add_actor(self.SnowDrop)
            self.SnowDrop.w = random.Random().randint(30, 30)
            self.SnowDrop.y = random.Random().randint(-100, 50)
            self.SnowDrop.x = random.Random().randint(0, 1400)
        for i in range(50):
            self.RainDrop = RainDrop()
            self.add_actor(self.RainDrop)
            self.RainDrop.w = random.Random().randint(30, 30)
            self.RainDrop.y = random.Random().randint(-100, 50)
            self.RainDrop.x = random.Random().randint(0, 1400)

class EndStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.MenuBg = MenuBg()
        self.add_actor(MenuBg())
        self.endtext = MenuText()
        self.add_actor(self.endtext)
        self.endtext.set_text("The simulation is over")
        self.endtext.set_alpha(500)
        self.endtext.set_width(80)
        self.endtext.set_height(80)
        self.endtext.x += 425
        self.endtext.y += 300



