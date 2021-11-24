import game
from game.scene2d.MyScreen import *
from game.scene2d.MyActor import *
from game.simpleworld.ShapeType import ShapeType

class Kocka(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/images.jpg")
        self.set_height(64)
        self.set_width(64)
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

    def __init__(self, image_url: str = "images/gomb1.png"):
        super().__init__(image_url)


class Hatter(game.scene2d.MyActor):

    def __init__(self, image_url: str = "images/hatter.jpg"):
        super().__init__(image_url)

class MenuHatter(game.scene2d.MyActor):

    def __init__(self, image_url: str = "images/spiderhatter.jpg"):
        super().__init__(image_url)


class Stage(game.scene2d.MyStage):


    def __init__(self):
        super().__init__()

        f = open("images/palyaxd.txt", "r")

        y: int = 0
        while True:
            line = f.readline().strip()
            if line:
                x: int = 0
                for c in line:
                    a: MyBaseActor = None
                    if c == "o":
                        a = Kocka()
                    if a is not None:
                        a.x = x * 64
                        a.y = y * 64
                        self.add_actor(a)
                        print(c)
                    x += 1
            else:
                break
            y += 1

        f.close()

        self.hatter_bg = Hatter()
        self.actor1_bg = Actor()
        self.add_actor(self.hatter_bg)
        self.add_actor(self.actor1_bg)


        self.actor1_bg.set_on_key_press_listener(self.press)
        self.set_on_key_down_listener(self.key_down)

    def press(self, sender, event):
        if event.key == pygame.K_d:
            sender.x += 10
        if event.key == pygame.K_a:
            sender.x -= 10
        if event.key == pygame.K_w:
            sender.y -= 10
        if event.key == pygame.K_s:
            sender.y += 10

    def interval(self, sender):
        self.actor1_bg.x += 100 * self.get_delta_time()
        pass

    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("'QUIT'")
            quit()

class MenuStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.hatter_bg = MenuHatter()
        self.gomb_bg = Gomb()
        self.add_actor(self.gomb_bg)
        self.add_actor(self.hatter_bg)
        self.gomb_bg.set_on_mouse_down_listener(self.Klikk)
        self.set_on_key_down_listener(self.key_down)

        self.gomb_bg.width = 100
        self.gomb_bg.height = 100
        self.gomb_bg.x = 300
        self.gomb_bg.y = 200

    def Klikk(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Screen())

    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("'QUIT'")
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

