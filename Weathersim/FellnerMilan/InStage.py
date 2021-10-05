from Weathersim.FellnerMilan.InActors import *
from Weathersim.FellnerMilan.RainyScreen import *
from Weathersim.FellnerMilan.Screen import *
import game
import pygame

class InStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.ls = LandScape()
        self.add_actor(self.ls)
        self.ls.z_index = 1

        self.sunny = Sunny()
        self.add_actor(self.sunny)
        self.sunny.z_index = 0

        self.sun = Sun()
        self.add_actor(self.sun)
        self.sun.z_index = 2
        self.sun.width = 400
        self.sun.x = 1280 - 250
        self.sun.y = 0 - 150

        self.backbutton = MainMenu()
        self.add_actor(self.backbutton)
        self.backbutton.set_on_mouse_down_listener(self.onClick)
        self.set_on_key_down_listener(self.keys)

    def act(self, delta_time: float):
        super().act(delta_time)
        self.sun.rotation = self.sun.rotation + 0.1

    def keys(self, sender,event):
        if event.key == pygame.K_LEFT:
            self.screen.game.set_screen(RainScreen())

    def onClick(self, sender,event):
        if event.button == 1:
            self.screen.game.set_screen(GameScreen())
            #quit()

