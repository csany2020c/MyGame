import random

import game
from game.scene2d.MyActor import *
from game.scene2d.MyLabel import *
from game.scene2d.MyTimer import *
from game.simpleworld.ShapeType import ShapeType





class Meghal(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.meghal = MyLabel("MEGHALTÁL","system", 128, [255,0,0])
        self.add_actor(self.meghal)
        self.gomb3_bg = Gomb3()
        self.add_actor(self.gomb3_bg)
        self.gomb3_bg.set_on_mouse_down_listener(self.Klikk3)

        self.gomb3_bg.width = 200
        self.gomb3_bg.height = 200
        self.gomb3_bg.x = 400
        self.gomb3_bg.y = 200

    def Klikk3(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(MenuScreen())
            print("Kiléptél")


class Kocka(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/images.jpg")
        self.set_height(64)
        self.set_width(64)
        self.hitbox_shape = ShapeType.Rectangle


class Golo(game.scene2d.MyActor):
    def __init__(self, image_url: str = "images/golo.png"):
        super().__init__(image_url)

        self.go = True
        self.set_height(14)
        self.set_width(14)
        self.hitbox_scale_h = 2
        self.hitbox_scale_w = 2
        self.y = 500
        self.hitbox_shape = ShapeType.Rectangle

class Actor(game.scene2d.MyActor):

    def __init__(self, image_url: str = "images/actorsus.png"):
        super().__init__(image_url)

        self.go = True
        self.set_width(64)
        self.hitbox_scale_h = 2
        self.hitbox_scale_w = 2
        self.y = 500
        self.hitbox_shape = ShapeType.Rectangle

class Gomb (game.scene2d.MyActor):

    def __init__(self, image_url: str = "images/start1.png"):
        super().__init__(image_url)

class Gomb2 (game.scene2d.MyActor):

    def __init__(self, image_url: str = "images/exit.png"):
        super().__init__(image_url)

class Gomb3 (game.scene2d.MyActor):

    def __init__(self, image_url: str = "images/back.png"):
        super().__init__(image_url)


class Hatter(game.scene2d.MyActor):

    def __init__(self, image_url: str = "images/city.jpg"):
        super().__init__(image_url)

class MenuHatter(game.scene2d.MyActor):

    def __init__(self, image_url: str = "images/spiderhatter.jpg"):
        super().__init__(image_url)

class venom(game.scene2d.MyActor):

    def __init__(self, x, y):
        super().__init__("images/venom.png")


        self.set_width(180)
        self.set_height(180)
        self.x = x
        self.y = y




class Stage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()

        f = open("images/palyaxd.txt", "r")



        self.hatter_bg = Hatter()
        self.repul = False
        self.counter = 0
        self.count = 0
        self.actor1_bg = Actor()
        self.add_actor(self.hatter_bg)
        self.add_actor(self.actor1_bg)
        self.timer = MyTickTimer(func=self.ido,interval=3,start_delay=0,repeat=True)
        self.add_timer(self.timer)



        self.actor1_bg.set_on_key_press_listener(self.press)
        self.set_on_key_press_listener(self.Golotuz)
        self.set_on_key_down_listener(self.key_down)

    def press(self, sender, event):
        if event.key == pygame.K_d:
            sender.x += 3
        if event.key == pygame.K_a:
            sender.x -= 3

    def ido(self, sender):
        self.randomszam = random.randint(0, 100)
        self.venom_bg = venom(1280 + self.randomszam, self.actor1_bg.get_y())
        self.add_actor(self.venom_bg)


    def interval(self, sender):
        self.actor1_bg.x += 100 * self.get_delta_time()
        # self.golo_bg.x += 100* self.get_delta_time()
        pass

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.repul == True:
            for a in self.actors:
                if isinstance(a,Golo):
                    a.x = a.get_x() + 3
                    self.ezegygolo = a

                    for b in self.actors:
                        if isinstance(b, venom):
                            if b.overlaps(self.ezegygolo):
                                b.remove_from_stage()
                                self.ezegygolo.remove_from_stage()
                                self.counter = 0
                                self.count += 1
                                if self.count + 1:
                                    print(self.count)






        for i in self.actors:
            if isinstance(i, venom):
                i.x = i.get_x() - 3
                if i.overlaps(self.actor1_bg):
                    i.remove_from_stage()
                    self.screen.game.set_screen(Meghal1())




    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("'QUIT'")
            quit()

    def Golotuz(self, sender, event):
        if event.key == pygame.K_SPACE:
            for a in self.actors:
                if isinstance(a, Golo):
                    self.counter += 1
            if self.counter == 0:
                self.add_actor(Golo())
                for a in self.actors:
                    if isinstance(a, Golo):
                        a.x = self.actor1_bg.get_x()
                        a.y = self.actor1_bg.get_y() + self.actor1_bg.get_height() / 2


                self.repul = True
                print(event)




class MenuStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.hatter_bg = MenuHatter()
        self.gomb_bg = Gomb()
        self.gomb2_bg = Gomb2()
        self.add_actor(self.gomb_bg)
        self.add_actor(self.hatter_bg)
        self.add_actor(self.gomb2_bg)

        self.gomb_bg.set_on_mouse_down_listener(self.Klikk)
        self.gomb2_bg.set_on_mouse_down_listener(self.Klikk2)
        self.set_on_key_down_listener(self.key_down)

        self.gomb_bg.width = 200
        self.gomb_bg.height = 200
        self.gomb_bg.x = 200
        self.gomb_bg.y = 200

        self.gomb2_bg.width = 200
        self.gomb2_bg.height = 200
        self.gomb2_bg.x = 400
        self.gomb2_bg.y = 200

    def Klikk(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Screen())

    def Klikk2(self, sender, event):
        if event.button == 1:
            quit()
            print("Kiléptél")



    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("Kiléptél")
            quit()


class Screen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(Stage())
class Meghal1(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(Meghal())

class MenuScreen(game.scene2d.MyScreen):
    def __init__(self):
        super(MenuScreen, self).__init__()
        self.add_stage(MenuStage())

class MenuKep(game.scene2d.MyGame):
    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False):
        super().__init__(width, height, autorun)
        self.screen = MenuScreen()

MenuKep().run()