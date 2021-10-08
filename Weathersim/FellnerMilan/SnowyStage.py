import  game
from random import Random
import pygame
from Weathersim.FellnerMilan.InActors import *
import Weathersim.FellnerMilan.InScreen
import Weathersim.FellnerMilan.SnowyRainScreen
from game.scene2d import MyTickTimer, MyOneTickTimer, MyIntervalTimer
from random import Random
class SnowStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.l = SnowyLandScape()
        self.add_actor(self.l)
        self.l.z_index = 2


        self.sunny = Sunny()
        self.add_actor(self.sunny)
        self.sunny.z_index = 0

        self.snow = Snow()
        self.add_actor(self.snow)
        self.snow.z_index = 3

        self.cloudreal = Cloud()
        self.add_actor(self.cloudreal)
        self.cloudreal.z_index = 1

        self.r = Random()

        self.backbutton = MainMenu()
        self.add_actor(self.backbutton)
        self.backbutton.x = 800
        self.backbutton.z_index = 15

        self.arrowleft = ArrowLeft()
        self.add_actor(self.arrowleft)
        self.arrowleft.set_on_mouse_down_listener(self.leftarrowListener)

        self.arrowright = ArrowRight()
        self.add_actor(self.arrowright)
        self.arrowright.set_on_mouse_down_listener(self.rightArrowListener)

        self.set_on_key_down_listener(self.keylistener)

    def act(self, delta_time: float):
        super().act(delta_time)
        self.t = MyTickTimer(interval=1,func=self.timerhandler)
        self.add_timer(self.t)


    def timerhandler(self,sender):
            self.snow2 = Snow()
            self.add_actor(self.snow2)
            self.remove_timer(self.t)
    def keylistener(self,sender,event):
        if event.key == pygame.K_LEFT:
            self.screen.game.set_screen(Weathersim.FellnerMilan.InScreen.InScreen())
        if event.key == pygame.K_RIGHT:
            self.screen.game.set_screen(Weathersim.FellnerMilan.SnowyRainScreen.SnowyRainScreen())

    def leftarrowListener(self,sender,event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.FellnerMilan.InScreen.InScreen())

    def rightArrowListener(self,sender,event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.FellnerMilan.SnowyRainScreen.SnowyRainScreen())