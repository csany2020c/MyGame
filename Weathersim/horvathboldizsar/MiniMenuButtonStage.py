import Weathersim.horvathboldizsar.GameScreen
from Weathersim.horvathboldizsar.MiniMenuActors import *


class MiniStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()

        self.menubutton = MenuButton()
        self.menubutton.width = 150
        self.menubutton.y = 650
        self.menubutton.x = 1125
        self.add_actor(self.menubutton)
        self.menubutton.set_on_mouse_down_listener(self.menu_button_click)

        self.minimenubutton = MiniMenuButton()
        self.minimenubutton.height = 50
        self.add_actor(self.minimenubutton)
        self.minimenubutton.set_on_mouse_down_listener(self.menu_button_click)

        self.mininapbutton = MiniNapButton()
        self.mininapbutton.height = 50
        self.mininapbutton.x = 50
        self.add_actor(self.mininapbutton)
        self.mininapbutton.set_on_mouse_down_listener(self.mini_nap_button_click)

        self.miniesobutton = MiniEsoButton()
        self.miniesobutton.height = 50
        self.miniesobutton.x = 100
        self.add_actor(self.miniesobutton)
        self.miniesobutton.set_on_mouse_down_listener(self.mini_eso_button_click)

        self.minihavasesobutton = MiniHavasesoButton()
        self.minihavasesobutton.height = 50
        self.minihavasesobutton.x = 150
        self.add_actor(self.minihavasesobutton)
        self.minihavasesobutton.set_on_mouse_down_listener(self.mini_havaseso_button_click)

        self.minihobutton = MiniHoButton()
        self.minihobutton.height = 50
        self.minihobutton.x = 200
        self.add_actor(self.minihobutton)
        self.minihobutton.set_on_mouse_down_listener(self.mini_ho_button_click)

    def menu_button_click(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.horvathboldizsar.MenuScreen.MenuScreen())

    def mini_nap_button_click(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.horvathboldizsar.GameScreen.NaposScreen())

    def mini_eso_button_click(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.horvathboldizsar.GameScreen.EsosScreen())

    def mini_havaseso_button_click(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.horvathboldizsar.GameScreen.HavasesoScreen())

    def mini_ho_button_click(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.horvathboldizsar.GameScreen.HavasScreen())
