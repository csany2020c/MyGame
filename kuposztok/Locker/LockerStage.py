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
            self.money = money
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        bg = ShopBgActor()
        self.add_actor(bg)
        self.snowmobilelabel = game.scene2d.MyLabel("SnowMobile:")
        self.snowmobilelabel.x = self.width / 5.5
        self.snowmobilelabel.y = self.height / 6.5
        self.snowmobilelabel.set_color(0, 0, 0)
        self.add_actor(self.snowmobilelabel)
        self.sledgelabel = game.scene2d.MyLabel("Sledge:")
        self.sledgelabel.x = self.width / 3
        self.sledgelabel.y = self.height / 6.5
        self.sledgelabel.set_color(0, 0, 0)
        self.add_actor(self.sledgelabel)
        self.snowboardlabel = game.scene2d.MyLabel("SnowBoard:")
        self.snowboardlabel.x = self.width / 1.75
        self.snowboardlabel.y = self.height / 6.5
        self.snowboardlabel.set_color(0, 0, 0)
        self.add_actor(self.snowboardlabel)
        self.ski = game.scene2d.MyLabel("Ski:")
        self.ski.x = self.width / 1.25
        self.ski.y = self.height / 6.5
        self.ski.set_color(0, 0, 0)
        self.add_actor(self.ski)
        self.moneylabel = game.scene2d.MyLabel("Your money:" + str(self.money))
        self.moneylabel.y = 0 + self.moneylabel.get_height() / 2
        self.moneylabel.x = self.width - self.moneylabel.get_width()
        self.moneylabel.set_color(0, 0, 0)
        self.add_actor(self.moneylabel)
        self.snowmobile = 0
        self.sledgevalt = 0
        self.snowboardvalt = 0
        self.skivalt = 0
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
        self.SilverSnowMobile = DefaultSnowMobile()
        self.SilverSnowMobile.set_size(200, 200)
        self.SilverSnowMobile.x = self.width / 5
        self.SilverSnowMobile.y = self.height / 2.5
        self.add_actor(self.SilverSnowMobile)
        self.SilverSledge = DefaultSledge()
        self.SilverSledge.set_size(200, 200)
        self.SilverSledge.x = self.width / 3
        self.SilverSledge.y = self.height / 2.5
        self.add_actor(self.SilverSledge)
        self.SilverSnowBoard = DefaultSnowBoard()
        self.SilverSnowBoard.set_size(200, 200)
        self.SilverSnowBoard.x = self.width / 1.7
        self.SilverSnowBoard.y = self.height / 2.5
        self.add_actor(self.SilverSnowBoard)
        self.SilverSki = DefaultSki()
        self.SilverSki.set_size(200, 200)
        self.SilverSki.x = self.width / 1.3
        self.SilverSki.y = self.height / 2.5
        self.add_actor(self.SilverSki)
        self.GoldSnowMobile = DefaultSnowMobile()
        self.GoldSnowMobile.set_size(200, 200)
        self.GoldSnowMobile.x = self.width / 5
        self.GoldSnowMobile.y = self.height / 1.5
        self.add_actor(self.GoldSnowMobile)
        self.GoldSledge = DefaultSnowMobile()
        self.GoldSledge.set_size(200, 200)
        self.GoldSledge.x = self.width / 5
        self.GoldSledge.y = self.height / 1.5
        self.add_actor(self.GoldSledge)
        self.GoldSnowBoard = DefaultSledge()
        self.GoldSnowBoard.set_size(200, 200)
        self.GoldSnowBoard.x = self.width / 3
        self.GoldSnowBoard.y = self.height / 1.5
        self.add_actor(self.GoldSnowBoard)
        self.add_actor(self.GoldSnowMobile)
        self.GoldSki = DefaultSki()
        self.GoldSki.set_size(200, 200)
        self.GoldSki.x = self.width / 1.3
        self.GoldSki.y = self.height / 1.5
        self.add_actor(self.GoldSki)


        self.set_on_key_down_listener(self.Back)
        self.back.set_on_mouse_down_listener(self.Back2)
        self.DefSnowMobile.set_on_mouse_down_listener(self.DefSnowMobile)
        self.DefSledge.set_on_mouse_down_listener(self.DefSledge)
        self.DefSnowBoard.set_on_mouse_down_listener(self.DefSnowBoard)
        self.DefSki.set_on_mouse_down_listener(self.DefSki)
        self.GoldSnowMobile.set_on_mouse_down_listener(self.GoldSnowMobile)
        self.GoldSledge.set_on_mouse_down_listener(self.GoldSledge)
        self.GoldSnowBoard.set_on_mouse_down_listener(self.GoldSnowBoard)
        self.GoldSki.set_on_mouse_down_listener(self.GoldSki)
        self.SilverSnowMobile.set_on_mouse_down_listener(self.SilverSnowMobile)
        self.SilverSledge.set_on_mouse_down_listener(self.SilverSledge)
        self.SilverSnowBoard.set_on_mouse_down_listener(self.SilverSnowBoard)
        self.SilverSki.set_on_mouse_down_listener(self.SilverSki)

    def Back(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())

    def Back2(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())

    def DefSnowMobile(self, sender, event):
        if event.button == 1:
            print("DefSnowMobile")
            skinvaltozo = 1

    def DefSledge(self, sender, event):
        if event.button == 1:
            print("DefSledge")
            skinvaltozo = 2

    def DefSnowBoard(self, sender, event):
        if event.button == 1:
            print("DefSnowBoard")
            skinvaltozo = 3

    def DefSki(self, sender, event):
        if event.button == 1:
            print("DefSki")
            skinvaltozo = 4

    def SilverSnowMobile(self, sender, event):
        if event.button == 1:
            print("SilverSnowMobile")
            goldvaltozo = 1

    def SilverSledge(self, sender, event):
        if event.button == 1:
            print("SilverSledge")
            goldvaltozo = 2

    def SilverSnowBoard(self, sender, event):
        if event.button == 1:
            print("SilverSnowBoard")
            goldvaltozo = 3

    def SilverSki(self, sender, event):
        if event.button == 1:
            print("SilverSki")
            skinvaltozo = 4

    def GoldSnowMobile(self, sender, event):
        if event.button == 1:
            print("GoldSnowMobile")
            skinvaltozo = 9

    def GoldSledge(self, sender, event):
        if event.button == 1:
            print("GoldSledge")
            skinvaltozo = 10

    def GoldSnowBoard(self, sender, event):
        if event.button == 1:
            print("GoldSnowBoard")
            skinvaltozo = 11

    def GoldSki(self, sender, event):
        if event.button == 1:
            print("GoldSki")
            skinvaltozo = 12

    # def Skinback(self):
    #     return self.skinvaltozo
    #
    # def act(self, delta_time: float):
    #     super().act(delta_time)
    #     print(skinvaltozo)


