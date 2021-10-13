import random
from Weathersim.Kancsalmate.Actors import *
import game
import pygame
from game.scene2d import MyTickTimer

class Stage(game.scene2d.MyStage):

    def Keys(self, sender, event):
        if event.key == pygame.K_a:
            self.isAPressed = True
            if self.isAPressed == True:
                self.napos()

        if event.key == pygame.K_s:
            self.isSPressed = True
            if self.isSPressed == True:
                self.esos()
        if event.key == pygame.K_m:
            self.isMPressed = True
        if event.key == pygame.K_e:
            self.isEPressed = True
        if event.key == pygame.K_d:
            self.isDPressed = True



    def __init__(self):
        super().__init__()
        self.isWPressed: bool = False
        self.isAPressed: bool = False
        self.isSPressed: bool = False
        self.isDPressed: bool = False
        self.isMPressed: bool = False
        self.isEPressed: bool = False
        self.set_on_key_down_listener(self.Keys)
        self.timer = MyTickTimer(func=self.tik, interval=3)
        self.timer1 = MyTickTimer(func=self.tikk, interval=3)
        self.a = ActorA()
        self.b = ActorB()
        self.c = ActorC()
        self.d = ActorD()
        self.e = ActorSnow()
        self.f = ActorRain()
        self.e.speed = 100
        self.x = 1
        self.e.set_z_index(6)
        self.c.set_z_index(1)
        self.b.set_z_index(1)
        self.d.set_z_index(3)
        self.a.set_z_index(5)
        self.b.set_x = 0
        self.a.set_x = 0
        self.add_actor(self.a)
        self.napos()

    def tik(self, sender):
        print("TIKKK")
        self.b.remove_from_stage()
        self.d.remove_from_stage()

    def tikk(self, sender):
        print("TIKKK")
        self.c.remove_from_stage()
        self.f.remove_from_stage()


    def napos(self):
        if self.isAPressed:
            self.add_actor(self.d)
            self.add_actor(self.b)
            self.add_timer(self.timer)

    def esos(self):
        if self.isSPressed:
            self.add_actor(self.c)

            self.add_timer(self.timer1)



    def act(self, delta_time: float):
        super().act(delta_time)





class Screen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(Stage())


class Start(game.scene2d.MyGame):
    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False):
        super().__init__(width, height, autorun)
        self.screen = Screen()

Start().run()