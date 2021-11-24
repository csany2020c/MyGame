from yetifc.yetiscreen import MenuScreen
from yetifc.yetigamescreen import GameScreen
from yetifc.yetigamescreen import GameStage

import game
import pygame


class Yeti(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = MenuScreen()
        pygame.mixer.music.load("Images/cowboymusic.wav")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(1)
        self.set_on_key_down_listener(self.key_down)

    def key_down(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()






Yeti().run()