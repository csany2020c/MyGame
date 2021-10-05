from Weathersim.KisKornel.Screen import *
import game
import pygame


class RUN(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen = SunnyScreen()


        def key_down(sender, event):
            print(sender)
            print(event)
            if event.key == pygame.K_ESCAPE:
                self.exit()

        self.set_on_key_down_listener(key_down)



RUN().run()