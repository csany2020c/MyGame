from Weathersim.ZsuppanFlorian.mainscreen import *
import game
import pygame

class MainStage(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = Napsutes()
        self.set_on_key_down_listener(self.key_down)

    def key_down(self, sender, event):
        print(sender)
        if event.key == pygame.K_ESCAPE:
            print("Kileptunk")
            pygame.quit()

        if event.key == pygame.K_4:
            print("Havaseso")
            self.screen = Hoeso()

        if event.key == pygame.K_3:
            print("Havazik")
            self.screen = Havazik()

        if event.key == pygame.K_2:
            print("Esikeso")
            self.screen = Esik()

        if event.key == pygame.K_1:
            print("Sutanap")
            self.screen = Napsutes()

        if event.key == pygame.K_0:
            print("info")
            self.screen = Infok()

        if event.key == pygame.K_5:
            print("havazikesiksut")
            self.screen = Hoesonap()

        if event.key == pygame.K_F11:
            print("Teljes kepernyo")
            pygame.display.toggle_fullscreen()

MainStage().run()