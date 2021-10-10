import game
import random
import pygame
from Weathersim.faterlaszlo.Arial import *
from Weathersim.faterlaszlo.f_actors import *
#from Weathersim.faterlaszlo.f_menu_m.f_screen_m import *

class f_stage1(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.bg = bg_actor()
        self.sun = napocska()
        self.eg = eg_actor()
        self.add_actor(self.bg)
        self.add_actor(self.sun)
        self.add_actor(self.eg)
        #ezt nem szabad igy hagyni
        #self.set_on_key_down_listener(self.key_down)
        self.sun.x = 50
        self.sun.y = 80
        self.sun.w = 350
        self.eg.z_index = 0
        self.sun.z_index = 2

        self.t = Arial()
        self.add_actor(self.t)
        self.t.set_text("Vissza_n")
        self.t.x = 0
        self.t.y = 0

        for i in range(3):
            self.a = apple()
            self.add_actor(self.a)
            self.a.w = 35
            self.a.x = random.Random().randint(10, 300)
            self.a.y = random.Random().randint(0, 250)
