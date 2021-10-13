import pygame
import Weathersim.horvathboldizsar.GameScreen
from Weathersim.horvathboldizsar.MenuActors import *
from Weathersim.horvathboldizsar.GameActors import *


class MenuStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()

        self.menubackground = MenuBackground()
        self.add_actor(self.menubackground)

        self.menunap = MenuNap()
        self.add_actor(self.menunap)

        for x in range(0, random.randint(75, 120)):
            e = Esocsepp()
            e.y = random.randint(-500, 300)
            e.x = random.randint(30, 420) - e.width
            self.add_actor(e)

        for j in range(0, random.randint(100, 170)):
            h = Hopehely()
            h.y = random.randint(-500, 500)
            h.x = random.randint(460, 845) - h.width
            self.add_actor(h)

        for x in range(0, random.randint(20, 30)):
            he = HavasesoCseppMenube()
            he.y = random.randint(360, 500)
            he.x = random.randint(460, 845) - he.width
            self.add_actor(he)

        self.naposbutton = NaposButton()
        self.naposbutton.width = 300
        self.naposbutton.y = 300
        self.naposbutton.x = 920
        self.add_actor(self.naposbutton)
        self.naposbutton.set_on_mouse_down_listener(self.napos_button_click)

        self.esosbutton = EsosButton()
        self.esosbutton.width = 300
        self.esosbutton.y = 300
        self.esosbutton.x = 60
        self.add_actor(self.esosbutton)
        self.esosbutton.set_on_mouse_down_listener(self.esos_button_click)

        self.havasbutton = HavasButton()
        self.havasbutton.width = 300
        self.havasbutton.y = 100
        self.havasbutton.x = 490
        self.add_actor(self.havasbutton)
        self.havasbutton.set_on_mouse_down_listener(self.havas_button_click)

        self.havasesobutton = HavasesosButton()
        self.havasesobutton.width = 300
        self.havasesobutton.y = 500
        self.havasesobutton.x = 490
        self.add_actor(self.havasesobutton)
        self.havasesobutton.set_on_mouse_down_listener(self.havaseso_button_click)

        self.exitbutton = ExitButton()
        self.exitbutton.width = 150
        self.exitbutton.y = 650
        self.exitbutton.x = 1125
        self.add_actor(self.exitbutton)
        self.exitbutton.set_on_mouse_down_listener(self.exit_button_click)

    def napos_button_click(self, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.horvathboldizsar.GameScreen.NaposScreen())
            print("Napos Screen")

    def esos_button_click(self, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.horvathboldizsar.GameScreen.EsosScreen())
            print("Esős Screen")

    def havas_button_click(self, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.horvathboldizsar.GameScreen.HavasScreen())
            print("Havas Screen")

    def havaseso_button_click(self, event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.horvathboldizsar.GameScreen.HavasesoScreen())
            print("Havaseső Screen")

    def exit_button_click(self, event):
        if event.button == 1:
            print("Exit! Viszlát :(")
            quit()
