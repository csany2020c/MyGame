import game
import random
import pygame

class menu(game.scene2d.MyActor):
    def __init__(self):
        super().__init__('images/hatter.jpg')

class button1(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('images/start.png')

class button2(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('images/exit.jpg')


class start(game.scene2d.MyActor):
    def __init__(self):
        super().__init__('images/start.png')

class exit(game.scene2d.MyActor):
    def __init__(self):
        super().__init__('images/exit.png')

class MenuStage(game.scene2d.MyStage):
    def __init__(self):
        super(MenuStage, self).__init__()
        self.menu = menu()
        self.add_actor(self.menu)
        self.start.z_index = 2
        self.start = start()
        self.start.x = 450
        self.start.y = 300
        self.add_actor(self.start)
        self.button1 = button1()
        self.add_actor(self.button1)
        self.button1.x = 450
        self.button1.y = 300
        self.button1.z_index = 2
        self.button1.set_on_mouse_down_listener(self.klikk1)

    def klikk1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(MenuScreen())


class MenuScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0)
        self.add_stage(MenuStage())


class Program(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = MenuScreen()

Program().run()