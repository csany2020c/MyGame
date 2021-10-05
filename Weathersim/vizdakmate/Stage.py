import game
import pygame
from Weathersim.vizdakmate.actor import *
class Stage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.add_actor(Rain)
        self.rain = Rain()
        self.add_actor(self.rain)
    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("'QUIT'")
            quit()