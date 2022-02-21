from Weathersim.nemethcsongor1.piano.PianoScreen import *
import pygame
import game


class PianoGame(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = PianoScreen()

        self.set_on_key_down_listener(self.katt)

    def katt(self, sender, event):
        print(sender)
        if event.key == pygame.K_ESCAPE:
            quit()


PianoGame().run()
