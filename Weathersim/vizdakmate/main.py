from Weathersim.vizdakmate.Screen import *
import game
import pygame

class Main(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen = SunnyScreen()

    def key_down(sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_f:
            print('Quit')
            quit()



Main().run()