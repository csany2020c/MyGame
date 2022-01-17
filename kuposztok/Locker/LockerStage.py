import game
import pygame

import kuposztok.Menu.MenuStage
from kuposztok.Locker.LockerActor import *
import kuposztok.Menu.MenuScreen
from game.scene2d import MyPermanentTimer, MyOneTickTimer, MyBaseActor, MyTickTimer, MyIntervalTimer


class LockerStage(game.scene2d.MyStage):
    def __init__(self, money: int, max_score:int):
        super().__init__()
        for i in range(5):
            print(money)
            self.money = money
            self.max_score = max_score
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
        self.snowmobilevalt = 0
        self.sledgevalt = 0
        self.snowboardvalt = 0
        self.skivalt = 0
        self.skinvalt = 0

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
        self.GoldSledge = DefaultSledge()
        self.GoldSledge.set_size(200, 200)
        self.GoldSledge.x = self.width / 3
        self.GoldSledge.y = self.height / 1.5
        self.add_actor(self.GoldSledge)
        self.GoldSnowBoard = DefaultSnowBoard()
        self.GoldSnowBoard.set_size(200, 200)
        self.GoldSnowBoard.x = self.width / 1.7
        self.GoldSnowBoard.y = self.height / 1.5
        self.add_actor(self.GoldSnowBoard)
        self.add_actor(self.GoldSnowMobile)
        self.GoldSki = DefaultSki()
        self.GoldSki.set_size(200, 200)
        self.GoldSki.x = self.width / 1.3
        self.GoldSki.y = self.height / 1.5
        self.add_actor(self.GoldSki)
        self.moneylabel = game.scene2d.MyLabel("Your money:" + str(self.money))
        self.moneylabel.y = 0 + self.moneylabel.get_height() / 2
        self.moneylabel.x = self.width - self.moneylabel.get_width()
        self.moneylabel.set_color(0, 0, 0)
        self.add_actor(self.moneylabel)


        self.silversnowmobilelock = SilverLock()
        self.silversnowmobilelock.x = self.SilverSnowMobile.get_x()
        self.silversnowmobilelock.y = self.SilverSnowMobile.get_y()
        self.silversnowmobilelock.set_size(250, 250)
        self.add_actor(self.silversnowmobilelock)
        self.silversledgelock = SilverLock()
        self.silversledgelock.x = self.SilverSledge.get_x()
        self.silversledgelock.y = self.SilverSledge.get_y()
        self.silversledgelock.set_size(250, 250)
        self.add_actor(self.silversledgelock)
        self.silversnowboardlock = SilverLock()
        self.silversnowboardlock.x = self.SilverSnowBoard.get_x()
        self.silversnowboardlock.y = self.SilverSnowBoard.get_y()
        self.silversnowboardlock.set_size(250, 250)
        self.add_actor(self.silversnowboardlock)
        self.silverskilock = SilverLock()
        self.silverskilock.x = self.SilverSki.get_x()
        self.silverskilock.y = self.SilverSki.get_y()
        self.silverskilock.set_size(250, 250)
        self.add_actor(self.silverskilock)
        self.goldsnowmobilelock = GoldLock()
        self.goldsnowmobilelock.x = self.GoldSnowMobile.get_x()
        self.goldsnowmobilelock.y = self.GoldSnowMobile.get_y()
        self.goldsnowmobilelock.set_size(250, 250)
        self.add_actor(self.goldsnowmobilelock)
        self.goldsledgelock = GoldLock()
        self.goldsledgelock.x = self.GoldSledge.get_x()
        self.goldsledgelock.y = self.GoldSledge.get_y()
        self.goldsledgelock.set_size(250, 250)
        self.add_actor(self.goldsledgelock)
        self.goldsnowboardlock = GoldLock()
        self.goldsnowboardlock.x = self.GoldSnowBoard.get_x()
        self.goldsnowboardlock.y = self.GoldSnowBoard.get_y()
        self.goldsnowboardlock.set_size(250, 250)
        self.add_actor(self.goldsnowboardlock)
        self.goldskilock = GoldLock()
        self.goldskilock.x = self.GoldSki.get_x()
        self.goldskilock.y = self.GoldSki.get_y()
        self.goldskilock.set_size(250, 250)
        self.add_actor(self.goldskilock)

        self.set_on_key_down_listener(self.Back)
        self.back.set_on_mouse_down_listener(self.Back2)
        self.DefSnowMobile.set_on_mouse_down_listener(self.DefSnowMobileB)
        self.DefSledge.set_on_mouse_down_listener(self.DefSledgeB)
        self.DefSnowBoard.set_on_mouse_down_listener(self.DefSnowBoardB)
        self.DefSki.set_on_mouse_down_listener(self.DefSkiB)
        self.GoldSnowMobile.set_on_mouse_down_listener(self.GoldSnowMobileB)
        self.GoldSledge.set_on_mouse_down_listener(self.GoldSledgeB)
        self.GoldSnowBoard.set_on_mouse_down_listener(self.GoldSnowBoardB)
        self.GoldSki.set_on_mouse_down_listener(self.GoldSkiB)
        self.SilverSnowMobile.set_on_mouse_down_listener(self.SilverSnowMobileB)
        self.SilverSledge.set_on_mouse_down_listener(self.SilverSledgeB)
        self.SilverSnowBoard.set_on_mouse_down_listener(self.SilverSnowBoardB)
        self.SilverSki.set_on_mouse_down_listener(self.SilverSkiB)

    def Back(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())

    def Back2(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())

    def DefSnowMobileB(self, sender, event):
        if event.button == 1:
            print("DefSnowMobile")
            self.snowmobilevalt = 1

    def DefSledgeB(self, sender, event):
        if event.button == 1:
            print("DefSledge")
            self.sledgevalt = 1

    def DefSnowBoardB(self, sender, event):
        if event.button == 1:
            print("DefSnowBoard")
            self.snowboardvalt = 1

    def DefSkiB(self, sender, event):
        if event.button == 1:
            print("DefSki")
            self.skivalt = 1

    def SilverSnowMobileB(self, sender, event):
        if event.button == 1:
            print("SilverSnowMobile")
            self.snowmobilevalt = 2
            if self.money >= 20000:
                self.remove_actor(self.silversnowmobilelock)
                self.skinvalt = 0
                self.money = self.money - 20000


    def SilverSledgeB(self, sender, event):
        if event.button == 1:
            print("SilverSledge")
            self.sledgevalt = 2
            if self.money >= 20000:
                self.remove_actor(self.silversledgelock)
                self.skinvalt = 1
                self.money = self.money - 20000


    def SilverSnowBoardB(self, sender, event):
        if event.button == 1:
            self.snowboardvalt = 2
            print("SilverSnowBoard")
            if self.money >= 20000:
                self.remove_actor(self.silversnowboardlock)
                self.skinvalt = 2
                self.money = self.money - 20000


    def SilverSkiB(self, sender, event):
        if event.button == 1:
            print("SilverSki")
            self.skivalt = 2
            if self.money >= 20000:
                self.remove_actor(self.silverskilock)
                self.skinvalt = 3
                self.money = self.money - 20000


    def GoldSnowMobileB(self, sender, event):
        if event.button == 1:
            self.snowmobilevalt = 3
            print("GoldSnowMobile")
            if self.money >= 100000:
                self.remove_actor(self.goldsnowmobilelock)
                self.skinvalt = 4
                self.money = self.money - 100000


    def GoldSledgeB(self, sender, event):
        if event.button == 1:
            print("GoldSledge")
            self.sledgevalt = 3
            if self.money >= 100000:
                self.remove_actor(self.goldsledgelock)
                self.skinvalt = 5
                self.money = self.money - 100000

    def GoldSnowBoardB(self, sender, event):
        if event.button == 1:
            print("GoldSnowBoard")
            self.snowboardvalt = 3
            if self.money >= 100000:
                self.remove_actor(self.goldsnowboardlock)
                self.skinvalt = 6
                self.money = self.money - 100000

    def GoldSkiB(self, sender, event):
        if event.button == 1:
            print("GoldSki")
            self.skivalt = 3
            if self.money >= 100000:
                self.remove_actor(self.goldskilock)
                self.skinvalt = 7
                self.money = self.money - 100000

    def filebairas(self):
        with open('../kuposztok/Save/file.txt', 'w') as file:
            file.write(str(self.max_score))
            file.write("\n" + str(self.money))
            file.close()

    def skinbeolvas(self):
        with open('../kuposztok/Save/skininfile.txt', 'w') as beskinfile:
            self.silversnom = beskinfile.readline()
            self.silversnob = beskinfile.readline()
            self.silversled = beskinfile.readline()
            self.silverski = beskinfile.readline()
            self.goldsnom = beskinfile.readline()
            self.goldsnob = beskinfile.readline()
            self.goldsled = beskinfile.readline()
            self.goldski = beskinfile.readline()

            beskinfile.close()

    def skinfilebairas(self):
        with open('../kuposztok/Save/skininfile.txt', 'w') as skinfile:
            skinfile.write(str(self.skinvalt) + "\n")
            skinfile.close()

    def act(self, delta_time: float):
        super().act(delta_time)
        self.filebairas()
        self.skinfilebairas()
        self.moneylabel.set_text("Your money:" + str(self.money))






