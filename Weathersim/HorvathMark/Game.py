from Weathersim.HorvathMark.Screen import *
import pygame

class Game(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720):
        super().__init__(width, height)
        self.screen = Sunnyscreen()

        def key_down(sender, event):
            print(sender)
            print(event)
            if event.key == pygame.K_ESCAPE:
                exit()

            if event.key == pygame.K_1:
                self.screen = Sunnyscreen()

            if event.key == pygame.K_2:
                self.screen = Snowyscreen()

            if event.key == pygame.K_3:
                self.screen = Rainyscreen()

            if event.key == pygame.K_4:
                self.screen = SnowyRainscreen()

        self.set_on_key_press_listener(key_down)


Game().run()