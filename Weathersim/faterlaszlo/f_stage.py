import game
import pygame
from f_actors import *

class f_stage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.bg = hatter_actor()
        self.sun = napocska()
        self.eg = eg_actor()
        self.add_actor(self.bg)
        self.add_actor(self.sun)
        self.add_actor(self.eg)
        #ezt nem szabad igy hagyni
        self.sun.set_on_key_down_listener(self.key_down)
        self.sun.x = 50
        self.sun.y = 80
        self.sun.w = 350
        self.eg.z_index = 0
        self.sun.z_index = 3



    def key_down(self, event, sender):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("Sikeresen be lett zárva")
            pygame.quit()