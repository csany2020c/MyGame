import pygame
from SzBKScreen import *
import random


class IdoSim(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = Sutanap()
        self.set_on_key_down_listener(self.key_down)

    def key_down(self, sender, event):
        print(sender)
        if event.key == pygame.K_ESCAPE:
            print("veged")
            pygame.quit()

        if event.key == pygame.K_2:
            print("222222222222222222222222222222")
            self.screen = Esikaho()

        if event.key == pygame.K_3:
            print("333333333333333333333333333333")
            self.screen = Esikaeso()

        if event.key == pygame.K_1:
            print("111111111111111111111111111111")
            self.screen = Sutanap()

        if event.key == pygame.K_4:
            print("444444444444444444444444444444")
            self.screen = Esikmindketo()

        if event.key == pygame.K_F11:
            print("555555555555555555555555555555")
            pygame.display.toggle_fullscreen()



IdoSim().run()