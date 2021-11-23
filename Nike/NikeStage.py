import game
from Nike.NikeScreen import *
from Nike.NikeActor import *
import Nike.NikeScreen
import random
import pygame

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
        self.exit.set_on_mouse_down_listener(self.exitbut)


    def play(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.screen.game.set_screen(Nike.NikeScreen.Game())
                print("'Start'")

    def exitbut(self, sender, event):
        print(sender)
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("'QUIT'")
                quit()

class GameStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.GameBg =GameBg()
        self.add_actor(GameBg())
        self.Sztrit = Sztrit()
        self.add_actor(Sztrit())
        self.FatJordanact = FatJordanact()
        self.add_actor(FatJordanact())






