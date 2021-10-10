import game
import Weathersim.FellnerMilan.SnowyScreen
import Weathersim.FellnerMilan.RainyScreen
from Weathersim.FellnerMilan.InActors import *
from game.scene2d import MyOneTickTimer, MyTickTimer
import pygame

class SnowyRainStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()

        self.ls = SnowyLandScape()
        self.add_actor(self.ls)
        self.ls.z_index = 1

        self.sky = Sunny()
        self.add_actor(self.sky)
        self.sky.z_index = -1

        self.snowyrain = SnowyRain()
        self.add_actor(self.snowyrain)
        self.snowyrain.z_index = 2

        self.cloud = Cloud()
        self.add_actor(self.cloud)
        self.cloud.z_index = 0

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
            self.snowyrain2 = SnowyRain()
            self.add_actor(self.snowyrain2)
            self.remove_timer(self.t)

    def keylistener(self,sender,event):
        if event.key == pygame.K_LEFT:
            self.screen.game.set_screen(Weathersim.FellnerMilan.SnowyScreen.SnowScreen())
        if event.key == pygame.K_RIGHT:
            self.screen.game.set_screen(Weathersim.FellnerMilan.RainyScreen.RainScreen())

    def leftarrowListener(self,sender,event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.FellnerMilan.SnowyScreen.SnowScreen())

    def rightArrowListener(self,sender,event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.FellnerMilan.RainyScreen.RainScreen())
