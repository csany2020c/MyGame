import game
import pygame
from HawkProductions.Actors import *
from HawkProductions.Font import *
from HawkProductions.GameScreen import *
from HawkProductions.InfoScreen import *


class MenuStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.h1 = Startb()
        self.h2 = Exit()
        self.b = Anything()
        self.add_actor(self.h1)
        self.add_actor(self.h2)
        self.add_actor(self.b)
        self.h1.x = 525
        self.h1.y = 250
        self.h1.w = 200

        self.h2.x = 525
        self.h2.y = 550
        self.h2.w = 200

        self.b.set_text("Flappy D")
        self.b.x = 500
        self.b.y = 100

        self.i = Info()
        self.add_actor(self.i)
        self.i.width = 250
        self.i.y = 400
        self.i.x = 500

        self.set_on_key_down_listener(self.key_down)
        self.h1.set_on_mouse_down_listener(self.click1)
        self.h2.set_on_mouse_down_listener(self.click)
        self.i.set_on_mouse_down_listener(self.click2)

    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("kilépés")
            quit()
        if event.key == pygame.K_SPACE:
            print("Elindul a játék")
            self.screen.game.set_screen(GameScreen())
        if event.key == pygame.K_i:
            self.screen.game.set_screen(IScreen())

    def click(self, sender, event):
        if event.button == 1:
            quit()

    def click1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(GameScreen())

    def click2(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(IScreen())
