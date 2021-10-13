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

class RainSnowStage(game.scene2d.MyStage):
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
        for a in range(1000):
            self.SnowDrop = SnowDrop()
            self.add_actor(self.SnowDrop)
            self.SnowDrop.width = 30
            self.SnowDrop.height = 30
            self.SnowDrop.x = random.Random().randint(-1500, 1500)
            self.SnowDrop.y = random.Random().randint(-1000, 1000)



