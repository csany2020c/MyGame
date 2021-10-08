import game
import pygame
from HawkProductions.Actors import *
from HawkProductions.Anything import *
from HawkProductions.GameScreen import *


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
        self.h2.y = 400
        self.h2.w = 200
        self.b.set_text("Flappy D")
        self.b.set_x(500)
        self.b.set_y(100)
        self.set_on_key_down_listener(self.key_down)
        self.h1.set_on_mouse_down_listener(self.klikk1)
        self.h2.set_on_mouse_down_listener(self.klikk)

    def key_down(self, sender, event):
        # if isinstance(sender, MyBaseActor):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("kilépés")
            quit()
        if event.key == pygame.K_SPACE:
            print("ASd")
            self.screen.game.set_screen(GameScreen())


    def klikk(self, sender, event):
        if event.button == 1:
            quit()

    def klikk1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(GameScreen())




        #if event.key == pygame.K_1:
         #   print("Végre jó")
          #  self.screen.game.set_screen(HawkProductions.GameScreen())


        #majd meg kell csinálni következő órán
        #if event.key == pygame.K_c:
            #print("Start")
            #pygame.display()
