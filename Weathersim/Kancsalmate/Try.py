import random
from Weathersim.Kancsalmate.Actors import *
import game
import pygame


class Stage(game.scene2d.MyStage):

    def Keys(self, sender, event):
        if event.key == pygame.K_a:
            if self.isWPressed == False and self.isSPressed == False and self.isDPressed == False:
                self.isAPressed = True

        if event.key == pygame.K_s:
            self.isSPressed = True
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
        self.a = ActorA()
        self.b = ActorB()
        self.c = ActorC()
        self.d = ActorD()
        self.e = ActorSnow()
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


    def act(self, delta_time: float):
        super().act(delta_time)
        if self.isAPressed:
            self.add_actor(self.d)
            self.add_actor(self.b)



        if self.isSPressed:
            self.add_actor(self.c)
            self.x = self.x - 1



        if self.isEPressed:
            self.b.remove_from_stage(self.d)

        if self.isDPressed:
            self.add_actor(self.e)
            self.e.set_x(700)




class Screen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(Stage())


class Start(game.scene2d.MyGame):
    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False):
        super().__init__(width, height, autorun)
        self.screen = Screen()

Start().run()