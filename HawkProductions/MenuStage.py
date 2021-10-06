import game
import pygame
from HawkProductions.Actors import *
from HawkProductions.Anything import *


class MenuStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.h1 = Enemy1Actor()
        self.h2 = Enemy2Actor()
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
        self.h2.set_on_key_down_listener(self.key_down)

    def key_down(self, sender, event):
        # if isinstance(sender, MyBaseActor):
        print(sender)
        print(event)
        if event.key == pygame.K_SPACE:
            print("kilépés")
            pygame.quit()


        #majd meg kell csinálni következő órán
        #if event.key == pygame.K_c:
            #print("Start")
            #pygame.display()
