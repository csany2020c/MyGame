import Weathersim.horvathboldizsar.MenuScreen
from Weathersim.horvathboldizsar.GameActors import *
from Weathersim.horvathboldizsar.MenuScreen import *

class NaposStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.erdo = erdo()
        self.erdo.z_index = 2
        self.add_actor(self.erdo)

        self.naposeg = naposeg()
        self.naposeg.z_index = 1
        self.add_actor(self.naposeg)

        self.nap = nap()
        self.nap.z_index = 3
        self.add_actor(self.nap)

        self.menubutton = menubutton()
        self.menubutton.width = 150
        self.menubutton.y = 650
        self.menubutton.x = 1125
        self.add_actor(self.menubutton)
        self.menubutton.set_on_mouse_down_listener(self.MenuButtonClick)

    def MenuButtonClick(self, sender,event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.horvathboldizsar.MenuScreen.MenuScreen())
            print("Menü Screen")

class FelhosStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.erdo = erdo()
        self.erdo.z_index = 2
        self.add_actor(self.erdo)

        self.felhoseg = felhoseg()
        self.felhoseg.z_index = 1
        self.add_actor(self.felhoseg)

        self.menubutton = menubutton()
        self.menubutton.width = 150
        self.menubutton.y = 650
        self.menubutton.x = 1125
        self.add_actor(self.menubutton)
        self.menubutton.set_on_mouse_down_listener(self.MenuButtonClick)

    def MenuButtonClick(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.horvathboldizsar.MenuScreen.MenuScreen())
            print("Menü Screen")

class EsosStage(game.scene2d.MyStage, ):
    def __init__(self):
        super().__init__()
        self.erdo = erdo()
        self.erdo.z_index = 2
        self.add_actor(self.erdo)

        self.felhoseg = felhoseg()
        self.felhoseg.z_index = 1
        self.add_actor(self.felhoseg)

        self.esocsepp = esocsepp()
        self.esocsepp.z_index = 3
        for x in range(0, random.randint(25, 50)):
            e = esocsepp()
            e.width = 30
            e.y = random.randint(0, 300)
            e.x = random.randint(0, 1280 - e.width)
            self.add_actor(e)

        self.menubutton = menubutton()
        self.menubutton.width = 150
        self.menubutton.y = 650
        self.menubutton.x = 1125
        self.add_actor(self.menubutton)
        self.menubutton.set_on_mouse_down_listener(self.MenuButtonClick)

    def MenuButtonClick(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.horvathboldizsar.MenuScreen.MenuScreen())
            print("Menü Screen")


class HavasStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.erdo = erdo()
        self.erdo.z_index = 2
        self.add_actor(self.erdo)

        self.felhoseg = felhoseg()
        self.felhoseg.z_index = 1
        self.add_actor(self.felhoseg)

        self.hopehely = hopehely()
        self.hopehely.z_index = 3
        for j in range(0, random.randint(30, 70)):
            h = hopehely()
            h.width = 30
            h.height = 30
            h.y = 0
            h.x = random.randint(0, 1280 - h.width)
            self.add_actor(h)

        self.menubutton = menubutton()
        self.menubutton.width = 150
        self.menubutton.y = 650
        self.menubutton.x = 1125
        self.add_actor(self.menubutton)
        self.menubutton.set_on_mouse_down_listener(self.MenuButtonClick)

    def MenuButtonClick(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.horvathboldizsar.MenuScreen.MenuScreen())
            print("Menü Screen")






