import game
import pygame
from game.scene2d import MyPermanentTimer, MyOneTickTimer, MyBaseActor, MyTickTimer, MyIntervalTimer
from pygame import mixer
from Weathersim.FellnerMilan.Actors import *
from Weathersim.FellnerMilan.InScreen import *
class GameStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        mixer.init()
        mixer.music.load("music.mp3")
        mixer.music.set_volume(0.1)
        mixer.music.play()


        self.actor1 = testActor()

        self.actor2 = startActor()

        self.actor3 = exitActor()

        self.add_actor(self.actor1)
        self.add_actor(self.actor2)
        self.add_actor(self.actor3)

        self.actor2.hitbox_scale_h = 0.4
        self.actor2.set_on_mouse_down_listener(self.startListener)

        self.actor3.hitbox_scale_h = 0.4
        self.actor3.hitbox_scale_w = 0.6
        self.actor3.set_on_mouse_down_listener(self.exitListener)

    def startListener(self,sender,event):
        if event.button == 1:
            print("lefut")
            self.actor2.image_url = "startOnClick.png"
            self.t = MyOneTickTimer(interval=0.2, func=self.changeActors)
            self.add_timer(self.t)

    def exitListener(self,sender,event):
        if event.button == 1:
            self.actor3.image_url = "exitOnClick.png"
            self.t2 = MyTickTimer(interval=0.2, func=self.changeActors2)
            self.add_timer(self.t2)

    def changeActors2(self,sender):
        self.actor3.image_url = "exit.png"
        pygame.quit()

    def changeActors(self,sender):
        self.actor2.image_url = "start.png"
        mixer.music.stop()
        self.screen.game.set_screen(InScreen())
        self.actor2.remove_on_mouse_down_listener()