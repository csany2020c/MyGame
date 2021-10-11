import game
import random
from game.scene2d.MyScreen import *

class Gomb1 (game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/gomb.png')

class Gomb2 (game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/gomb.png')

class Gomb3 (game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/gomb.png')

class Gomb4 (game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/gomb.png')

class Eso (game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__ ('!_resources/images/rain.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 300
        if self.y > game.scene2d.MyGame.get_screen_height():
            self.y = -128


class Nap(game.scene2d.MyActor):
    def __init__(self):
        self.map = super ().__init__('!_resources/images/sun.png')

class Szurke(game.scene2d.MyActor):
    def __init__(self):
        self.map = super ().__init__('!_resources/images/cloudy.png')

class Hav(game.scene2d.MyActor):
    def __init__(self):
        self.map = super ().__init__('!_resources/images/snow.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 300
        if self.y > game.scene2d.MyGame.get_screen_height():
            self.y = -128

class Hatter(game.scene2d.MyActor):
    def __init__(self):
        self.map = super ().__init__('!_resources/images/landscape.png')

class Napos(game.scene2d.MyActor):
    def __init__(self):
        self.map = super ().__init__('!_resources/images/sunny.png')



class NaposStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.napos_bg = Napos()
        self.hatter_bg = Hatter()
        self.add_actor(self.napos_bg)
        self.add_actor(self.hatter_bg)

class EsoStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.szurke_bg = Szurke()
        self.hatter_bg = Hatter()
        self.add_actor(self.szurke_bg)
        self.add_actor(self.hatter_bg)

        for i in range(50):
            self.eso_bg = Eso()
            self.add_actor(self.eso_bg)
            self.eso_bg.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.eso_bg.w)
            self.eso_bg.y = random.Random().randint(0, 720)



class HavStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.szurke_bg = Szurke()
        self.hatter_bg = Hatter()
        self.hav_bg = Hav()
        self.add_actor(self.hav_bg)
        self.add_actor(self.szurke_bg)
        self.add_actor(self.hatter_bg)

        for i in range(50):
            self.hav_bg = Hav()
            self.add_actor(self.hav_bg)
            self.hav_bg.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.hav_bg.w)
            self.hav_bg.y = random.Random().randint(0, 720)

class HavEsoStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.eso_bg = Eso()
        self.hav_bg = Hav()
        self.szurke_bg = Szurke()
        self.hatter_bg = Hatter()
        self.add_actor(self.eso_bg)
        self.add_actor(self.hav_bg)
        self.add_actor(self.szurke_bg)
        self.add_actor(self.hatter_bg)


        for s in range(50):
            self.eso_bg = Eso()
            self.add_actor(self.eso_bg)
            self.eso_bg.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.eso_bg.w)
            self.eso_bg.y = random.Random().randint(0, 720)

        for i in range(50):
            self.hav_bg = Hav()
            self.add_actor(self.hav_bg)
            self.hav_bg.x = random.Random().randint(0, game.scene2d.MyGame.get_screen_width() - self.hav_bg.w)
            self.hav_bg.y = random.Random().randint(0, 720)

class NaposScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(NaposStage())

class EsosScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(EsoStage())

class HavScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(HavStage())

class HavEsoScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(HavEsoStage())



class MenuStage(game.scene2d.MyStage):
    def __init__(self):
        super(MenuStage, self).__init__()
        self.hatter_bg = Hatter()
        self.gomb_bg = Gomb1()
        self.gomb2_bg = Gomb2()
        self.gomb3_bg = Gomb3()
        self.gomb4_bg = Gomb4()

        self.add_actor(self.hatter_bg)
        self.add_actor(self.gomb_bg)
        self.add_actor(self.gomb2_bg)
        self.add_actor(self.gomb3_bg)
        self.add_actor(self.gomb4_bg)

        self.gomb_bg.set_on_mouse_down_listener(self.Klikk1)
        self.gomb2_bg.set_on_mouse_down_listener(self.Klikk2)
        self.gomb3_bg.set_on_mouse_down_listener(self.Klikk3)
        self.gomb4_bg.set_on_mouse_down_listener(self.Klikk4)

        self.gomb_bg.width = 100
        self.gomb_bg.height = 50
        self.gomb_bg.x = 700
        self.gomb_bg.y = 600

        self.gomb2_bg.width = 100
        self.gomb2_bg.height = 50
        self.gomb2_bg.x = 800
        self.gomb2_bg.y = 600

        self.gomb3_bg.width = 100
        self.gomb3_bg.height = 50
        self.gomb3_bg.x = 900
        self.gomb3_bg.y = 600

        self.gomb4_bg.width = 100
        self.gomb4_bg.height = 50
        self.gomb4_bg.x = 1000
        self.gomb4_bg.y = 600

    def Klikk1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(NaposScreen())

    def Klikk2(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(EsosScreen())

    def Klikk3(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(HavScreen())

    def Klikk4(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(HavEsoScreen())


class MenuScreen(game.scene2d.MyScreen):
    def __init__(self):
        super(MenuScreen, self).__init__()
        self.add_stage(MenuStage())

class MenuKep(game.scene2d.MyGame):
    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False):
        super().__init__(width, height, autorun)
        self.screen = MenuScreen()


MenuKep().run()








