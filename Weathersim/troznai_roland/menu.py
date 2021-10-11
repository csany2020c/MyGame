import Weathersim
import game
from Weathersim import troznai_roland
import Weathersim.troznai_roland.napos
import Weathersim.troznai_roland.eso
import Weathersim.troznai_roland.havas
import Weathersim.troznai_roland.havas_eso
from game.scene2d.MyScreen import *

class Screen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(GameStage())

class hatter(game.scene2d.MyActor):

    def __init__(self):
        self.hatter = super().__init__('menu_hatter.png')


class Gomb1(game.scene2d.MyActor):

    def __init__(self):
        self.button1 = super().__init__('napos_gomb.png')


class Gomb2(game.scene2d.MyActor):

    def __init__(self):
        self.button2 = super().__init__('havas_gomb.png')


class Gomb3(game.scene2d.MyActor):

    def __init__(self):
        self.button3 = super().__init__('esos_gomb.png')


class Gomb4(game.scene2d.MyActor):

    def __init__(self):
        self.button4 = super().__init__('esos_havas_gomb.png')


class Gomb5(game.scene2d.MyActor):

    def __init__(self):
        self.button5 = super().__init__('exit_gomb.png')


class GameStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.hatter = hatter()
        self.hatter.width = 1280
        self.hatter.height = 720
        self.add_actor(self.hatter)

        self.button1 = Gomb1()
        self.button1.width = 240
        self.button1.height = 120
        self.button1.x = 50
        self.button1.y = 170
        self.add_actor(self.button1)

        self.button2 = Gomb2()
        self.button2.width = 240
        self.button2.height = 120
        self.button2.x = 710
        self.button2.y = 170
        self.add_actor(self.button2)

        self.button3 = Gomb3()
        self.button3.width = 240
        self.button3.height = 120
        self.button3.x = 385
        self.button3.y = 170
        self.add_actor(self.button3)

        self.button4 = Gomb4()
        self.button4.width = 240
        self.button4.height = 120
        self.button4.x = 1010
        self.button4.y = 170
        self.add_actor(self.button4)

        self.button5 = Gomb5()
        self.button5.width = 240
        self.button5.height = 120
        self.button5.x = 520
        self.button5.y = 600
        self.add_actor(self.button5)

        self.button1.set_on_mouse_down_listener(self.Kattintas_napos)
        self.button2.set_on_mouse_down_listener(self.Kattintas_havas)
        self.button3.set_on_mouse_down_listener(self.Kattintas_esos)
        self.button4.set_on_mouse_down_listener(self.Kattintas_havas_eso)
        self.button5.set_on_mouse_down_listener(self.Kattintas_exit)

    def key_down(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()

    def Kattintas_napos(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.troznai_roland.napos.Screen())

    def Kattintas_havas(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.troznai_roland.havas.Screen())

    def Kattintas_esos(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.troznai_roland.eso.Screen())

    def Kattintas_havas_eso(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.troznai_roland.havas_eso.Screen())

    def Kattintas_exit(self, sender, event):
        if event.button == 1:
            quit()


class Menu(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = Screen()


Menu().run()