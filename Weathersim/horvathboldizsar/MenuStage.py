import pygame

import Weathersim.horvathboldizsar.GameScreen
from Weathersim.horvathboldizsar.MenuActors import *
from Weathersim.horvathboldizsar.GameActors import *


class MenuStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.menubackground = menubackground()
        self.menubackground.z_index = 2
        self.add_actor(self.menubackground)

        self.nap = nap()
        self.nap.z_index = 3
        self.add_actor(self.nap)

        self.esocsepp = esocsepp()
        self.esocsepp.z_index = 3
        for x in range(0, random.randint(25, 50)):
            e = esocsepp()
            e.width = 30
            e.y = random.randint(0, 300)
            e.x = random.randint(0, 420 - e.width)
            self.add_actor(e)

        self.hopehely = hopehely()
        self.hopehely.z_index = 3
        for j in range(0, random.randint(30, 70)):
            h = hopehely()
            h.width = 30
            h.height = 30
            h.y = 0
            h.x = random.randint(430, 845 - h.width)
            self.add_actor(h)

        self.naposbutton = naposbutton()
        self.naposbutton.width = 300
        self.naposbutton.y = 300
        self.naposbutton.x = 920
        self.add_actor(self.naposbutton)
        self.naposbutton.set_on_mouse_down_listener(self.NaposButtonClick)

        self.esosbutton = esosbutton()
        self.esosbutton.width = 300
        self.esosbutton.y = 300
        self.esosbutton.x = 60
        self.add_actor(self.esosbutton)
        self.esosbutton.set_on_mouse_down_listener(self.EsosButtonClick)

        self.havasbutton = havasbutton()
        self.havasbutton.width = 300
        self.havasbutton.y = 300
        self.havasbutton.x = 490
        self.add_actor(self.havasbutton)
        self.havasbutton.set_on_mouse_down_listener(self.HavasButtonClick)

        self.exitbutton = exitbutton()
        self.exitbutton.width = 150
        self.exitbutton.y = 650
        self.exitbutton.x = 1125
        self.add_actor(self.exitbutton)
        self.exitbutton.set_on_mouse_down_listener(self.ExitButtonClick)



    def NaposButtonClick(self, sender,event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.horvathboldizsar.GameScreen.NaposScreen())
            print("Napos Screen")

    def EsosButtonClick(self, sender,event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.horvathboldizsar.GameScreen.EsosScreen())
            print("Esős Screen")

    def HavasButtonClick(self, sender,event):
        if event.button == 1:
            self.screen.game.set_screen(Weathersim.horvathboldizsar.GameScreen.HavasScreen())
            print("Havas Screen")

    def ExitButtonClick(self, sender,event):
        if event.button == 1:
            print("Exit! Viszlát :(")
            quit()

