import game
import pygame
from Weathersim.faterlaszlo.f_actors import *
import random
from Weathersim.faterlaszlo.Anything import *


class f_stage_m(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.set_on_key_down_listener(self.key_down)

        self.t = Anything()
        self.add_actor(self.t)
        self.t.set_text("Napsütés")
        self.t.x = 500
        self.t.y = 50
        self.t.set_on_mouse_down_listener(self.click)

        self.t1 = Anything()
        self.add_actor(self.t1)
        self.t1.set_text("Eső")
        self.t1.x = 550
        self.t1.y = 100
        self.t1.set_on_mouse_down_listener(self.click1)

        self.t2 = Anything()
        self.add_actor(self.t2)
        self.t2.set_text("Eső")
        self.t2.x = 550
        self.t2.y = 200
        self.t2.set_on_mouse_down_listener(self.click2)

        self.t3 = Anything()
        self.add_actor(self.t3)
        self.t3.set_text("Havazás")
        self.t3.x = 550
        self.t3.y = 250
        self.t3.set_on_mouse_down_listener(self.click3)

        self.t4 = Anything()
        self.add_actor(self.t4)
        self.t4.set_text("Kilépés")
        self.t4.x = 550
        self.t4.y = 400
        self.t4.set_on_mouse_down_listener(self.click4)

    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("Sikeresen be lett zárva")
            quit()
        if event.key == pygame.K_1:
            print("Nspsütés")
            self.screen.add_stage(f_stage1())
        if event.key == pygame.K_2:
            print("felhős az ég")
            self.screen.add_stage(f_stage2())
        if event.key == pygame.K_3:
            print("Havas eső")
            self.screen.add_stage(f_stage3())
        if event.key == pygame.K_4:
            print("Eső")
            self.screen.add_stage(f_stage4())
        if event.key == pygame.K_SPACE:
            print("Vissza a főképernyőre(menu)")
            self.screen.add_stage(f_stage_m())

    def click(self, sender, event):
        if event.button == 1:
            self.screen.add_stage(f_stage1())

    def click1(self, sender, event):
        if event.button == 1:
            self.screen.add_stage(f_stage2())

    def click2(self, sender, event):
        if event.button == 1:
            self.screen.add_stage(f_stage3())

    def click3(self, sender, event):
        if event.button == 1:
            self.screen.add_stage(f_stage4())

    def click4(self, sender, event):
        if event.button == 1:
            quit()

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



    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("Sikeresen be lett zárva")
            quit()

class f_stage2(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.bg = bg_actor()
        self.felho = felhos_actor()
        self.add_actor(self.bg)
        self.add_actor(self.felho)
        self.felho.z_index = 0

class f_stage3(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.bg = bg_actor()
        self.felho = felhos_actor()
        self.add_actor(self.bg)
        self.add_actor(self.felho)
        self.felho.z_index = 0
        for i in range(12):
            self.eso = eso()
            self.add_actor(self.eso)
            self.eso.h = 25
            self.eso.w = 50
            self.eso.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.eso.w)
            self.eso.y = random.Random().randint(0, game.scene2d.MyGame.get_screen_height() - self.eso.h)

class f_stage3(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.bg = bg_actor()
        self.felho = felhos_actor()
        self.add_actor(self.bg)
        self.add_actor(self.felho)
        self.felho.z_index = 0
        for i in range(12):
            self.eso = eso()
            self.add_actor(self.eso)
            self.eso.h = 25
            self.eso.w = 50
            self.eso.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.eso.w)
            self.eso.y = random.Random().randint(0, game.scene2d.MyGame.get_screen_height() - self.eso.h)

        for i in range(12):
            self.havazik = havazas()
            self.add_actor(self.havazik)
            self.havazik.h = 20
            self.havazik.w = 45
            self.havazik.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.havazik.w)
            self.havazik.y = random.Random().randint(0, game.scene2d.MyGame.get_screen_height() - self.havazik.h)

class f_stage4(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.bg = bg_actor()
        self.felho = felhos_actor()
        self.add_actor(self.bg)
        self.add_actor(self.felho)
        self.felho.z_index = 0
        for i in range(12):
            self.havazik = havazas()
            self.add_actor(self.havazik)
            self.havazik.h = 20
            self.havazik.w = 45
            self.havazik.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.havazik.w)
            self.havazik.y = random.Random().randint(0, game.scene2d.MyGame.get_screen_height() - self.havazik.h)


