import game
from Nike.NikeScreen import *
from Nike.NikeActor import *
import Nike.NikeScreen
import random
import pygame
from game.simpleworld.ShapeType import ShapeType

class MenuStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.FatJordan = FatJordan()
        self.add_actor(FatJordan())
        self.text = MenuText()
        self.add_actor(self.text)
        self.text.set_text("Fat Jordan")
        self.text.set_alpha(500)
        self.text.set_width(80)
        self.text.set_height(80)
        self.text.x += 500
        self.text.y += 150
        self.start = MenuText()
        self.add_actor(self.start)
        self.start.set_text("Start")
        self.start.set_alpha(500)
        self.start.set_width(80)
        self.start.set_height(80)
        self.start.x += 300
        self.start.y += 250
        self.start.set_on_mouse_down_listener(self.play)
        self.exit = MenuText()
        self.add_actor(self.exit)
        self.exit.set_text("Exit")
        self.exit.set_alpha(500)
        self.exit.set_width(80)
        self.exit.set_height(80)
        self.exit.x += 850
        self.exit.y += 250
        #self.exit.set_on_mouse_down_listener(self.exitbut)


    def play(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.screen.game.set_screen(Nike.NikeScreen.Game)
                quit()

class GameStage(game.scene2d.MyStage):
    def __init__(self, map: str):
        super().__init__()
        self.set_on_key_down_listener(self.backtomenu)
        self.GameBg =GameBg()
        #self.add_actor(GameBg())
        #self.add_actor(GameBg2())
        #self.Sztrit = Sztrit()
        self.add_actor(Sztrit())
        self.FatJordanact = FatJordanact()
        self.add_actor(FatJordanact())
        self.LeBron = LeBron()
        self.add_actor(LeBron())

        self.camera.tracking = self.FatJordanact
        self.FatJordanact.set_on_key_press_listener(self.press)

        f = open(map, "r")

        y: int = 0
        while True:
            line = f.readline().strip()
            if line:
                x: int = 0
                for c in line:
                    a: MyBaseActor = None
                    if c == "s":
                        a = stone()
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
        if event.key == pygame.K_d:
            sender.x += 10
            self.camera.set_tracking_window(0.5, 0.6, 0.5, 0.5)
        if event.key == pygame.K_a:
            sender.x -= 10
            self.camera.set_tracking_window(0.5, 0.6, 0.5, 0.5)
        if event.key == pygame.K_w:
            sender.y -= 10
            self.camera.set_tracking_window(0.4, 0.6, 0.4, 0.2)
        if event.key == pygame.K_s:
            sender.y += 10
            self.camera.set_tracking_window(0.4, 0.2, 0.4, 0.6)

    def backtomenu(self,sender,event):
        if event.key == pygame.K_ESCAPE:
            self.screen.game.set_screen(Nike.NikeScreen.Menu())