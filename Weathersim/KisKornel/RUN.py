from Weathersim.KisKornel.Screen import *
import game
import pygame


class RUN(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen = MenuScreen()

        def key_down(sender, event):
            print(sender)
            print(event)
            if event.key == pygame.K_ESCAPE:
                self.exit()
            if event.key == pygame.K_3:
                self.screen = SnowyScreen()
            if event.key == pygame.K_2:
                self.screen = RainScreen()
            if event.key == pygame.K_1:
                self.screen = SunnyScreen()
            if event.key == pygame.K_BACKSPACE:
                self.screen = MenuScreen()
            if event.key == pygame.K_4:
                self.screen = MenuScreen()
        self.set_on_key_down_listener(key_down)



RUN().run()