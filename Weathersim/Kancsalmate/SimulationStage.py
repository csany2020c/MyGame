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

        if event.key == pygame.K_f:
            self.isFPressed = True
            if self.isFPressed == True:
                self.havaseso()

        if event.key == pygame.K_d:
            self.isDPressed = True
            if self.isDPressed == True:
                self.hav()
                self.esos()
        if event.key == pygame.K_ESCAPE:
            quit()

    def __init__(self):
        super().__init__()
        self.isWPressed: bool = False
        self.isAPressed: bool = False
        self.isSPressed: bool = False
        self.isDPressed: bool = False
        self.isMPressed: bool = False
        self.isFPressed: bool = False
        self.set_on_key_down_listener(self.Keys)
        self.timer = MyTickTimer(func=self.tik, interval=10)
        self.timer1 = MyTickTimer(func=self.tikk, interval=10)
        self.timer2 = MyTickTimer(func=self.tikkk, interval=10)
        self.a = ActorA()
        self.b = ActorB()
        self.c = ActorC()
        self.d = ActorD()
        self.e = ActorSnow()
        self.raindrops()
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
        self.snow()

    def tik(self, sender):
        print("TIKKK")
        self.b.remove_from_stage()
        self.d.remove_from_stage()

    def tikk(self, sender):
        print("TIKKK")
        self.c.remove_from_stage()
        self.f.remove_from_stage()
        self.f2.remove_from_stage()
        self.f3.remove_from_stage()
        self.f4.remove_from_stage()
        self.f5.remove_from_stage()
        self.f6.remove_from_stage()
        self.f7.remove_from_stage()
        self.f8.remove_from_stage()
        self.f9.remove_from_stage()
        self.f10.remove_from_stage()
        self.f11.remove_from_stage()
        self.f12.remove_from_stage()

    def tikkk(self, sender):
        print("TIKKK")
        self.c.remove_from_stage()
        self.s.remove_from_stage()
        self.s2.remove_from_stage()
        self.s3.remove_from_stage()
        self.s4.remove_from_stage()
        self.s5.remove_from_stage()
        self.s6.remove_from_stage()
        self.s7.remove_from_stage()
        self.s8.remove_from_stage()
        self.s9.remove_from_stage()
        self.s10.remove_from_stage()
        self.s11.remove_from_stage()
        self.s12.remove_from_stage()

    def cákk(self):
        self.c.remove_from_stage()
        self.s.remove_from_stage()
        self.s2.remove_from_stage()
        self.s3.remove_from_stage()
        self.s4.remove_from_stage()
        self.s5.remove_from_stage()
        self.s6.remove_from_stage()
        self.s7.remove_from_stage()
        self.s8.remove_from_stage()
        self.s9.remove_from_stage()
        self.s10.remove_from_stage()
        self.s11.remove_from_stage()
        self.s12.remove_from_stage()
        self.f.remove_from_stage()
        self.f2.remove_from_stage()
        self.f3.remove_from_stage()
        self.f4.remove_from_stage()
        self.f5.remove_from_stage()
        self.f6.remove_from_stage()
        self.f7.remove_from_stage()
        self.f8.remove_from_stage()
        self.f9.remove_from_stage()
        self.f10.remove_from_stage()
        self.f11.remove_from_stage()
        self.f12.remove_from_stage()

    def raindrops(self):
        self.f = ActorRain()
        self.f2 = ActorRain()
        self.f3 = ActorRain()
        self.f4 = ActorRain()
        self.f5 = ActorRain()
        self.f6 = ActorRain()
        self.f7 = ActorRain()
        self.f8 = ActorRain()
        self.f9 = ActorRain()
        self.f10 = ActorRain()
        self.f11 = ActorRain()
        self.f12 = ActorRain()

    def snow(self):
        self.s = ActorSnow()
        self.s1 = ActorSnow()
        self.s2 = ActorSnow()
        self.s3 = ActorSnow()
        self.s3 = ActorSnow()
        self.s4 = ActorSnow()
        self.s5 = ActorSnow()
        self.s6 = ActorSnow()
        self.s7 = ActorSnow()
        self.s8 = ActorSnow()
        self.s9 = ActorSnow()
        self.s10 = ActorSnow()
        self.s11 = ActorSnow()
        self.s12 = ActorSnow()

    def napos(self):
        if self.isAPressed:
            self.add_actor(self.d)
            self.add_actor(self.b)
            self.add_timer(self.timer)

    def esos(self):
        if self.isSPressed:
            self.add_actor(self.c)
            self.add_actor(self.f)
            self.add_actor(self.f2)
            self.add_actor(self.f3)
            self.add_actor(self.f4)
            self.add_actor(self.f5)
            self.add_actor(self.f6)
            self.add_actor(self.f7)
            self.add_actor(self.f8)
            self.add_actor(self.f9)
            self.add_actor(self.f10)
            self.add_actor(self.f11)
            self.add_actor(self.f12)
            self.add_timer(self.timer1)

    def hav(self):
        if self.isDPressed:
            self.add_actor(self.c)
            self.add_actor(self.s)
            self.add_actor(self.s2)
            self.add_actor(self.s3)
            self.add_actor(self.s4)
            self.add_actor(self.s5)
            self.add_actor(self.s6)
            self.add_actor(self.s7)
            self.add_actor(self.s8)
            self.add_actor(self.s9)
            self.add_actor(self.s10)
            self.add_actor(self.s11)
            self.add_actor(self.s12)
            self.add_timer(self.timer2)

    def havaseso(self):
        if self.isFPressed:
            self.add_actor(self.c)
            self.add_actor(self.s)
            self.add_actor(self.s2)
            self.add_actor(self.s3)
            self.add_actor(self.s4)
            self.add_actor(self.s5)
            self.add_actor(self.s6)
            self.add_actor(self.s7)
            self.add_actor(self.s8)
            self.add_actor(self.s9)
            self.add_actor(self.s10)
            self.add_actor(self.s11)
            self.add_actor(self.s12)

            self.add_actor(self.f)
            self.add_actor(self.f2)
            self.add_actor(self.f3)
            self.add_actor(self.f4)
            self.add_actor(self.f5)
            self.add_actor(self.f6)
            self.add_actor(self.f7)
            self.add_actor(self.f8)
            self.add_actor(self.f9)
            self.add_actor(self.f10)
            self.add_actor(self.f11)
            self.add_actor(self.f12)
            self.add_timer(self.timer1)
            self.add_timer(self.timer2)

class Screen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(Stage())

class Start(game.scene2d.MyGame):
    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False):
        super().__init__(width, height, autorun)
        self.screen = Screen()

Start().run()