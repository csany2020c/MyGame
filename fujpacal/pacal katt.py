import game
import pygame
from game.scene2d.MyScreen import *
from game.scene2d.MyActor import *
from game.simpleworld.ShapeType import ShapeType

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


class Hatter(game.scene2d.MyActor):

    def __init__(self, image_url: str = "images/city.jpg"):
        super().__init__(image_url)

class MenuHatter(game.scene2d.MyActor):

    def __init__(self, image_url: str = "images/spiderhatter.jpg"):
        super().__init__(image_url)











class Stage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()

        f = open("images/palyaxd.txt", "r")



        self.hatter_bg = Hatter()
        self.actor1_bg = Actor()
        self.golo_bg = Golo()
        self.add_actor(self.hatter_bg)
        self.add_actor(self.actor1_bg)
        self.add_actor(self.golo_bg)


        self.actor1_bg.set_on_key_press_listener(self.press)
        self.golo_bg.set_on_key_press_listener(self.Golotuz)
        self.set_on_key_down_listener(self.key_down)

    def press(self, sender, event):
        if event.key == pygame.K_d:
            sender.x += 3
        if event.key == pygame.K_a:
            sender.x -= 3







    def interval(self, sender):
        self.actor1_bg.x += 100 * self.get_delta_time()
        self.golo_bg.x += 100* self.get_delta_time()
        pass

    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("'QUIT'")
            quit()

    def Golotuz(self, sender, event):
        if event.key == pygame.K_SPACE:
            sender.x += 30
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


class MenuScreen(game.scene2d.MyScreen):
    def __init__(self):
        super(MenuScreen, self).__init__()
        self.add_stage(MenuStage())

class MenuKep(game.scene2d.MyGame):
    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False):
        super().__init__(width, height, autorun)
        self.screen = MenuScreen()

MenuKep().run()

