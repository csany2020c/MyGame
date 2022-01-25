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
        pygame.mixer.init()
        pygame.mixer.music.load("../kuposztok/music/shopmusica.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        self.bg = ShopBgActor()
        self.bg.width = self.width
        self.add_actor(self.bg)
        self.snowmobilelabel = game.scene2d.MyLabel("SnowMobile:")
        self.snowmobilelabel.x = self.width / 5.5 - self.snowmobilelabel.get_width() / 2
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
        self.DefSnowMobile.set_size(75, 150)
        self.DefSnowMobile.x = self.width / 5 - self.DefSnowMobile.get_width()
        self.DefSnowMobile.y = self.height / 5
        self.add_actor(self.DefSnowMobile)
        self.DefSledge = DefaultSledge()
        self.DefSledge.set_size(75, 150)
        self.DefSledge.x = self.width / 3
        self.DefSledge.y = self.height / 5
        self.add_actor(self.DefSledge)
        self.DefSnowBoard = DefaultSnowBoard()
        self.DefSnowBoard.set_size(50, 150)
        self.DefSnowBoard.x = self.width / 1.7 + self.DefSnowBoard.get_width() * 2
        self.DefSnowBoard.y = self.height / 5
        self.add_actor(self.DefSnowBoard)
        self.DefSki = DefaultSki()
        self.DefSki.set_size(50, 150)
        self.DefSki.x = self.width / 1.3 + self.DefSki.get_width() * 2
        self.DefSki.y = self.height / 5
        self.add_actor(self.DefSki)
        self.SilverSnowMobile = SilverSnowMobile()
        self.SilverSnowMobile.hide()
        self.SilverSnowMobile.set_size(75, 150)
        self.SilverSnowMobile.x = self.width / 5 - self.SilverSnowMobile.get_width()
        self.SilverSnowMobile.y = self.height / 2.5
        self.add_actor(self.SilverSnowMobile)
        self.SilverSledge = SilverSledge()
        self.SilverSledge.set_size(75, 150)
        self.SilverSledge.x = self.width / 3
        self.SilverSledge.y = self.height / 2.5
        self.add_actor(self.SilverSledge)
        self.SilverSnowBoard = SilverSnowBoard()
        self.SilverSnowBoard.set_size(50, 150)
        self.SilverSnowBoard.x = self.width / 1.7 + + self.SilverSnowBoard.get_width() * 2
        self.SilverSnowBoard.y = self.height / 2.5
        self.add_actor(self.SilverSnowBoard)
        self.SilverSki = SilverSki()
        self.SilverSki.set_size(50, 150)
        self.SilverSki.x = self.width / 1.3 + + self.SilverSki.get_width() * 2
        self.SilverSki.y = self.height / 2.5
        self.add_actor(self.SilverSki)
        self.GoldSnowMobile = GoldSnowMobile()
        self.GoldSnowMobile.set_size(75, 150)
        self.GoldSnowMobile.x = self.width / 5 - self.GoldSnowMobile.get_width()
        self.GoldSnowMobile.y = self.height / 1.5
        self.add_actor(self.GoldSnowMobile)
        self.GoldSledge = GoldSledge()
        self.GoldSledge.set_size(75, 150)
        self.GoldSledge.x = self.width / 3
        self.GoldSledge.y = self.height / 1.5
        self.add_actor(self.GoldSledge)
        self.GoldSnowBoard = GoldSnowBoard()
        self.GoldSnowBoard.set_size(50, 150)
        self.GoldSnowBoard.x = self.width / 1.7 + + self.GoldSnowBoard.get_width() * 2
        self.GoldSnowBoard.y = self.height / 1.5
        self.add_actor(self.GoldSnowBoard)
        self.add_actor(self.GoldSnowMobile)
        self.GoldSki = GoldSki()
        self.GoldSki.set_size(50, 150)
        self.GoldSki.x = self.width / 1.3 + + self.GoldSki.get_width() * 2
        self.GoldSki.y = self.height / 1.5
        self.add_actor(self.GoldSki)
        self.dollarlabel = game.scene2d.MyLabel("$")
        self.dollarlabel.y = 0 + self.dollarlabel.get_height() / 2
        self.dollarlabel.x = self.width - self.dollarlabel.get_width() - 20
        self.dollarlabel.set_color(0, 0, 0)
        self.add_actor(self.dollarlabel)
        self.moneylabel = game.scene2d.MyLabel("Your money:" + str(self.money))
        self.moneylabel.y = 0 + self.moneylabel.get_height() / 2
        self.moneylabel.x = self.width - self.moneylabel.get_width() - 50
        self.moneylabel.set_color(0, 0, 0)
        self.add_actor(self.moneylabel)

        self.silversnowmobilelock = SilverLock()
        self.silversnowmobilelock.x = self.SilverSnowMobile.get_x() - self.silversnowmobilelock.get_width() / 2.3
        self.silversnowmobilelock.y = self.SilverSnowMobile.get_y() - self.silversnowmobilelock.get_height() / 5
        self.silversnowmobilelock.set_size(250, 250)
        self.add_actor(self.silversnowmobilelock)
        self.silversledgelock = SilverLock()
        self.silversledgelock.x = self.SilverSledge.get_x() - self.silversledgelock.get_width() / 2.3
        self.silversledgelock.y = self.SilverSledge.get_y() - self.silversledgelock.get_height() / 5
        self.silversledgelock.set_size(250, 250)
        self.add_actor(self.silversledgelock)
        self.silversnowboardlock = SilverLock()
        self.silversnowboardlock.x = self.SilverSnowBoard.get_x() - self.silversnowboardlock.get_width() / 2.3
        self.silversnowboardlock.y = self.SilverSnowBoard.get_y() - self.silversnowboardlock.get_height() / 5
        self.silversnowboardlock.set_size(250, 250)
        self.add_actor(self.silversnowboardlock)
        self.silverskilock = SilverLock()
        self.silverskilock.x = self.SilverSki.get_x() - self.silverskilock.get_width() / 2.3
        self.silverskilock.y = self.SilverSki.get_y() - self.silverskilock.get_height() / 5
        self.silverskilock.set_size(250, 250)
        self.add_actor(self.silverskilock)
        self.goldsnowmobilelock = GoldLock()
        self.goldsnowmobilelock.x = self.GoldSnowMobile.get_x() - self.goldsnowmobilelock.get_width() / 2.3
        self.goldsnowmobilelock.y = self.GoldSnowMobile.get_y() - self.goldsnowmobilelock.get_height() / 5
        self.goldsnowmobilelock.set_size(250, 250)
        self.add_actor(self.goldsnowmobilelock)
        self.goldsledgelock = GoldLock()
        self.goldsledgelock.x = self.GoldSledge.get_x() - self.goldsledgelock.get_width() / 2.3
        self.goldsledgelock.y = self.GoldSledge.get_y() - self.goldsledgelock.get_height() / 5
        self.goldsledgelock.set_size(250, 250)
        self.add_actor(self.goldsledgelock)
        self.goldsnowboardlock = GoldLock()
        self.goldsnowboardlock.x = self.GoldSnowBoard.get_x() - self.goldsnowboardlock.get_width() / 2.3
        self.goldsnowboardlock.y = self.GoldSnowBoard.get_y() - self.goldsnowboardlock.get_height() / 5
        self.goldsnowboardlock.set_size(250, 250)
        self.add_actor(self.goldsnowboardlock)
        self.goldskilock = GoldLock()
        self.goldskilock.x = self.GoldSki.get_x() - self.goldskilock.get_width() / 2.3
        self.goldskilock.y = self.GoldSki.get_y() - self.goldskilock.get_height() / 5
        self.goldskilock.set_size(250, 250)
        self.add_actor(self.goldskilock)

        self.silverlabel = game.scene2d.MyLabel("5000000$")
        self.silverlabel.x = self.silversnowmobilelock.get_x() + self.silverlabel.get_width() / 3.5
        self.silverlabel.y = self.silversnowmobilelock.get_y() + self.silversnowmobilelock.get_height() / 1.6
        self.silverlabel.set_font_size(50)
        self.silverlabel.set_color(0, 0, 0)
        self.add_actor(self.silverlabel)
        self.silverlabel2 = game.scene2d.MyLabel("5000000$")
        self.silverlabel2.x = self.silversledgelock.get_x() + self.silverlabel.get_width() / 3.5
        self.silverlabel2.y = self.silversledgelock.get_y() + self.silversledgelock.get_height() / 1.6
        self.silverlabel2.set_color(0, 0, 0)
        self.silverlabel2.set_font_size(50)
        self.add_actor(self.silverlabel2)
        self.silverlabel3 = game.scene2d.MyLabel("5000000$")
        self.silverlabel3.x = self.silversnowboardlock.get_x() + self.silverlabel.get_width() / 3.5
        self.silverlabel3.y = self.silversnowboardlock.get_y() + self.silversnowboardlock.get_height() / 1.6
        self.silverlabel3.set_color(0, 0, 0)
        self.silverlabel3.set_font_size(50)
        self.add_actor(self.silverlabel3)
        self.silverlabel4 = game.scene2d.MyLabel("5000000$")
        self.silverlabel4.x = self.silverskilock.get_x() + self.silverlabel.get_width() / 3.5
        self.silverlabel4.y = self.silverskilock.get_y() + self.silverskilock.get_height() / 1.6
        self.silverlabel4.set_font_size(50)
        self.silverlabel4.set_color(0, 0, 0)
        self.add_actor(self.silverlabel4)
        self.goldlabel = game.scene2d.MyLabel("10000000$")
        self.goldlabel.x = self.goldsnowmobilelock.get_x() + self.goldlabel.get_width() / 5
        self.goldlabel.y = self.goldsnowmobilelock.get_y() + self.goldsnowmobilelock.get_height() / 1.6
        self.goldlabel.set_color(0, 0, 0)
        self.goldlabel.set_font_size(45)
        self.add_actor(self.goldlabel)
        self.goldlabel2 = game.scene2d.MyLabel("10000000$")
        self.goldlabel2.x = self.goldsledgelock.get_x() + self.goldlabel2.get_width() / 5
        self.goldlabel2.y = self.goldsledgelock.get_y() + self.goldsledgelock.get_height() / 1.6
        self.goldlabel2.set_color(0, 0, 0)
        self.goldlabel2.set_font_size(45)
        self.add_actor(self.goldlabel2)
        self.goldlabel3 = game.scene2d.MyLabel("10000000$")
        self.goldlabel3.x = self.goldsnowboardlock.get_x() + self.goldlabel3.get_width() / 5
        self.goldlabel3.y = self.goldsnowboardlock.get_y() + self.goldsnowboardlock.get_height() / 1.6
        self.goldlabel3.set_color(0, 0, 0)
        self.goldlabel3.set_font_size(45)
        self.add_actor(self.goldlabel3)
        self.goldlabel4 = game.scene2d.MyLabel("10000000$")
        self.goldlabel4.x = self.goldskilock.get_x() + self.goldlabel4.get_width() / 5
        self.goldlabel4.y = self.goldskilock.get_y() + self.goldskilock.get_height() / 1.6
        self.goldlabel4.set_color(0, 0, 0)
        self.goldlabel4.set_font_size(45)
        self.add_actor(self.goldlabel4)

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
        """self.skinbeolvas()"""

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
            if self.silversnowmobilelock.is_on_stage():
                if self.money >= 5000000:
                    self.remove_actor(self.silversnowmobilelock)
                    self.remove_actor(self.silverlabel)
                    self.skinvalt = 0
                    self.money = self.money - 5000000
                    self.moneylabel.set_text("Your money:" + str(self.money))


    def SilverSledgeB(self, sender, event):
        if event.button == 1:
            print("SilverSledge")
            self.sledgevalt = 2
            if self.silversledgelock.is_on_stage():
                if self.money >= 5000000:
                    self.remove_actor(self.silversledgelock)
                    self.remove_actor(self.silverlabel2)
                    self.skinvalt = 1
                    self.money = self.money - 5000000
                    self.moneylabel.set_text("Your money:" + str(self.money))


    def SilverSnowBoardB(self, sender, event):
        if event.button == 1:
            self.snowboardvalt = 2
            print("SilverSnowBoard")
            if self.silversnowboardlock.is_on_stage():
                if self.money >= 5000000:
                    self.remove_actor(self.silversnowboardlock)
                    self.remove_actor(self.silverlabel3)
                    self.skinvalt = 2
                    self.money = self.money - 5000000
                    self.moneylabel.set_text("Your money:" + str(self.money))


    def SilverSkiB(self, sender, event):
        if event.button == 1:
            print("SilverSki")
            self.skivalt = 2
            if self.silverskilock.is_on_stage():
                if self.money >= 5000000:
                    self.remove_actor(self.silverskilock)
                    self.remove_actor(self.silverlabel4)
                    self.skinvalt = 3
                    self.money = self.money - 5000000
                    self.moneylabel.set_text("Your money:" + str(self.money))


    def GoldSnowMobileB(self, sender, event):
        if event.button == 1:
            self.snowmobilevalt = 3
            print("GoldSnowMobile")
            if self.goldsnowmobilelock.is_on_stage():
                if self.money >= 10000000:
                    self.remove_actor(self.goldsnowmobilelock)
                    self.remove_actor(self.goldlabel)
                    self.skinvalt = 4
                    self.money = self.money - 10000000
                    self.moneylabel.set_text("Your money:" + str(self.money))


    def GoldSledgeB(self, sender, event):
        if event.button == 1:
            print("GoldSledge")
            self.sledgevalt = 3
            if self.goldsledgelock.is_on_stage():
                if self.money >= 10000000:
                    self.remove_actor(self.goldsledgelock)
                    self.remove_actor(self.goldlabel2)
                    self.skinvalt = 5
                    self.money = self.money - 10000000
                    self.moneylabel.set_text("Your money:" + str(self.money))

    def GoldSnowBoardB(self, sender, event):
        if event.button == 1:
            print("GoldSnowBoard")
            self.snowboardvalt = 3
            if self.goldsnowboardlock.is_on_stage():
                if self.money >= 10000000:
                    self.remove_actor(self.goldsnowboardlock)
                    self.remove_actor(self.goldlabel3)
                    self.skinvalt = 6
                    self.money = self.money - 10000000
                    self.moneylabel.set_text("Your money:" + str(self.money))

    def GoldSkiB(self, sender, event):
        if event.button == 1:
            print("GoldSki")
            self.skivalt = 3
            if self.goldskilock.is_on_stage():
                if self.money >= 10000000:
                    self.remove_actor(self.goldskilock)
                    self.remove_actor(self.goldlabel4)
                    self.skinvalt = 7
                    self.money = self.money - 10000000
                    self.moneylabel.set_text("Your money:" + str(self.money))

    def filebairas(self):
        with open('../kuposztok/Save/file.txt', 'w') as file:
            file.write(str(self.max_score))
            file.write("\n" + str(self.money))
            file.close()

    def skinbeolvas(self):
        with open('../kuposztok/Save/skininfile.txt', 'w') as beskinfile:
            self.valtozo = 1
            print(str(beskinfile.readline()))
            beskinfile.close()

            self.silverSnowMobile = int(beskinfile.readline())
            self.silverSledge = int('\n' + beskinfile.readline())
            self.silverSnowBoard = int('\n' + beskinfile.readline())
            self.silverSki = int('\n' + beskinfile.readline())
            self.goldSnowMobile = int('\n' + beskinfile.readline())
            self.goldSledge = int('\n' + beskinfile.readline())
            self.goldSnowBoard = int('\n' + beskinfile.readline())
            self.goldSki = int('\n' + beskinfile.readline())

            print(self.silverSnowMobile)




    def skinfilebairas(self):
        with open('../kuposztok/Save/skininfile.txt', 'w') as skinfile:
            if self.GoldSkiB == True:
                skinfile.write("\n alsadalma0")
            else:
                skinfile.write("alsadalma2")
            skinfile.close()

    def act(self, delta_time: float):
        super().act(delta_time)
        self.filebairas()
        self.skinfilebairas()







