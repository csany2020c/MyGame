import game
import pygame

import kuposztok.Menu.MenuStage
from kuposztok.Locker.LockerActor import *
import kuposztok.Menu.MenuScreen


class LockerStage(game.scene2d.MyStage):
    def __init__(self, money: int):
        super().__init__()
        for i in range(5):
            print(money)
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        bg = ShopBgActor()
        self.add_actor(bg)
        self.skinvaltozo = 0
        from kuposztok.Menu.MenuStage import MenuStage
        # self.money = MenuStage.getMoneyMenu()
        # self.moneyLabel = game.scene2d.MyLabel("Your money: " + self.money)
        # self.add_actor(self.moneyLabel)
        self.back = Back()
        self.add_actor(self.back)
        self.DefSnowMobile = DefaultSnowMobile()
        self.DefSnowMobile.set_size(200, 200)
        self.DefSnowMobile.x = self.width / 5
        self.DefSnowMobile.y = self.height / 5
        self.add_actor(self.DefSnowMobile)
        self.DefSledge = DefaultSledge()
        self.DefSledge.set_size(200, 200)
        self.DefSledge.x = self.width / 3
        self.DefSledge.y = self.height / 5
        self.add_actor(self.DefSledge)
        self.DefSnowBoard = DefaultSnowBoard()
        self.DefSnowBoard.set_size(200, 200)
        self.DefSnowBoard.x = self.width / 1.7
        self.DefSnowBoard.y = self.height / 5
        self.add_actor(self.DefSnowBoard)
        self.DefSki = DefaultSki()
        self.DefSki.set_size(200, 200)
        self.DefSki.x = self.width / 1.3
        self.DefSki.y = self.height / 5
        self.add_actor(self.DefSki)
        self.BlueSnowMobile = DefaultSnowMobile()
        self.BlueSnowMobile.set_size(200, 200)
        self.BlueSnowMobile.x = self.width / 5
        self.BlueSnowMobile.y = self.height / 2.5
        self.add_actor(self.BlueSnowMobile)
        self.BlueSledge = DefaultSledge()
        self.BlueSledge.set_size(200, 200)
        self.BlueSledge.x = self.width / 3
        self.BlueSledge.y = self.height / 2.5
        self.add_actor(self.BlueSledge)
        self.BlueSnowBoard = DefaultSnowBoard()
        self.BlueSnowBoard.set_size(200, 200)
        self.BlueSnowBoard.x = self.width / 1.7
        self.BlueSnowBoard.y = self.height / 2.5
        self.add_actor(self.BlueSnowBoard)
        self.BlueSki = DefaultSki()
        self.BlueSki.set_size(200, 200)
        self.BlueSki.x = self.width / 1.3
        self.BlueSki.y = self.height / 2.5
        self.add_actor(self.BlueSki)
        self.RedSnowMobile = DefaultSnowMobile()
        self.RedSnowMobile.set_size(200, 200)
        self.RedSnowMobile.x = self.width / 5
        self.RedSnowMobile.y = self.height / 1.5
        self.add_actor(self.RedSnowMobile)
        self.RedSledge = DefaultSledge()
        self.RedSledge.set_size(200, 200)
        self.RedSledge.x = self.width / 3
        self.RedSledge.y = self.height / 1.5
        self.add_actor(self.RedSledge)
        self.RedSnowBoard = DefaultSnowBoard()
        self.RedSnowBoard.set_size(200, 200)
        self.RedSnowBoard.x = self.width / 1.7
        self.RedSnowBoard.y = self.height / 1.5
        self.add_actor(self.RedSnowBoard)
        self.RedSki = DefaultSki()
        self.RedSki.set_size(200, 200)
        self.RedSki.x = self.width / 1.3
        self.RedSki.y = self.height / 1.5
        self.add_actor(self.RedSki)


        self.set_on_key_down_listener(self.Back)
        self.back.set_on_mouse_down_listener(self.Back2)
        self.DefSnowMobile.set_on_mouse_down_listener(self.Def1)
        self.DefSledge.set_on_mouse_down_listener(self.Def2)
        self.DefSnowBoard.set_on_mouse_down_listener(self.Def3)
        self.DefSki.set_on_mouse_down_listener(self.Def4)
        self.BlueSnowMobile.set_on_mouse_down_listener(self.Blue1)
        self.BlueSledge.set_on_mouse_down_listener(self.Blue2)
        self.DefSnowMobile.set_on_mouse_down_listener(self.Blue3)
        self.DefSledge.set_on_mouse_down_listener(self.Blue4)
        self.DefSnowBoard.set_on_mouse_down_listener(self.Red1)
        self.DefSki.set_on_mouse_down_listener(self.Red2)
        self.BlueSnowMobile.set_on_mouse_down_listener(self.Red3)
        self.BlueSledge.set_on_mouse_down_listener(self.Red4)

    def Back(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())

    def Back2(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())

    def Def1(self, sender, event):
        if event.button == 1:
            print("def1")
            skinvaltozo = 1

    def Def2(self, sender, event):
        if event.button == 1:
            print("def2")
            skinvaltozo = 2

    def Def3(self, sender, event):
        if event.button == 1:
            print("def3")
            skinvaltozo = 3

    def Def4(self, sender, event):
        if event.button == 1:
            print("def4")
            skinvaltozo = 4

    def Blue1(self, sender, event):
        if event.button == 1:
            print("blue1")
            skinvaltozo = 5

    def Blue2(self, sender, event):
        if event.button == 1:
            print("blue2")
            skinvaltozo = 6

    def Blue3(self, sender, event):
        if event.button == 1:
            print("blue3")
            skinvaltozo = 7

    def Blue4(self, sender, event):
        if event.button == 1:
            print("blue4")
            skinvaltozo = 8

    def Red1(self, sender, event):
        if event.button == 1:
            print("red1")
            skinvaltozo = 9

    def Red2(self, sender, event):
        if event.button == 1:
            print("red2")
            skinvaltozo = 10

    def Red3(self, sender, event):
        if event.button == 1:
            print("red3")
            skinvaltozo = 11

    def Red4(self, sender, event):
        if event.button == 1:
            print("red4")
            skinvaltozo = 12

    # def Skinback(self):
    #     return self.skinvaltozo
    #
    # def act(self, delta_time: float):
    #     super().act(delta_time)
    #     print(skinvaltozo)


