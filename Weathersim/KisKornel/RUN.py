from Weathersim.KisKornel.Screen import *
import game
import pygame


class RUN(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, heigt: int = 720):
        super().__init__(width, heigt)
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
                self.screen = havasesoScreen()
        self.set_on_key_down_listener(key_down)


RUN().run()