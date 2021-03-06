import pygame
import socket

import game
import kuposztok
from kuposztok.CaraValt.CaraValtScreen import CaraValtScreen
from kuposztok.Credit.CreditScreen import CreditScreen
import kuposztok.Locker.LockerScreen
from kuposztok.Menu.MenuBgActor import *
from kuposztok.Info.InfoScreen import InfoScreen
import datetime
import kuposztok.options.OptionsScreen
import webbrowser


class MenuStage(game.scene2d.MyStage):

    def act(self, delta_time: float,):
        super().act(delta_time)
        self.filebaolvasas()
        self.ma = datetime.datetime.now()
        self.devicelabel.set_text("A gép neve:" + str(self.devicename))
        self.ido.set_text("Jelenlegi idő: " + str(self.ma.hour) + " : " + str(self.ma.minute))

    def soundvaltread(self):
        with open('../kuposztok/Save/options.txt', 'r') as beskinfile1:
            self.soundvaltbe = int(beskinfile1.readline())
            self.musica = int(beskinfile1.readline())
            self.allstagebe = int(beskinfile1.readline())
            beskinfile1.close()

    def __init__(self):
        super().__init__()
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        self.devicename = socket.gethostname()
        self.devicewrite()
        self.deviceread()
        self.deviceben = self.alldevice
        self.soundvaltread()
        self.allstageben = self.allstagebe
        self.soundvalt = self.soundvaltbe
        self.musicaselect = self.musica
        pygame.mixer.init()
        self.allstage = False
        if self.allstageben == 0 or self.allstageben == 1:
            self.allstage = True
        if self.allstageben == 2:
            self.allstage = False
        if self.allstage == False:
            pygame.mixer.music.load("../kuposztok/music/menumusica.wav")
        else:
            if self.musicaselect == 0 or self.musicaselect == 1:
                pygame.mixer.music.load("../kuposztok/music/gamemusica1.wav")
            if self.musicaselect == 2:
                pygame.mixer.music.load("../kuposztok/music/gamemusica2.wav")
            if self.musicaselect == 3:
                pygame.mixer.music.load("../kuposztok/music/gamemusica3.wav")
            if self.musicaselect == 4:
                pygame.mixer.music.load("../kuposztok/music/gamemusica4.wav")
            if self.musicaselect == 5:
                pygame.mixer.music.load("../kuposztok/music/gamemusica5.wav")
        pygame.mixer.music.play(-1)
        if self.soundvalt == 0 or self.soundvalt == 1:
            pygame.mixer.music.set_volume(0.5)
        if self.soundvalt == 2:
            pygame.mixer.music.set_volume(0.20)
        if self.soundvalt == 3:
            pygame.mixer.music.set_volume(0.07)
        if self.soundvalt == 4:
            pygame.mixer.music.stop()
        bg = MenuActor()
        self.add_actor(bg)
        bg.height = self.height
        bg.width = self.width
        self.options = OptionsButton()
        self.options.set_position(0, self.height - self.options.get_height() * 2)
        self.add_actor(self.options)
        self.ma = datetime.datetime.now()
        self.ido = game.scene2d.MyLabel("Jelenlegi idő: " + str(self.ma.hour) + " : " + str(self.ma.minute))
        self.ido.set_color(0, 0, 0)
        self.add_actor(self.ido)
        self.ido.set_font_size(40)
        self.ido.x = 0
        self.ido.y = 0 + self.ido.get_height() - 20
        self.money = 0
        self.max_score = 0
        self.early = game.scene2d.MyLabel("Early Access, Closed Beta Test")
        self.early.set_color(0, 0, 0)
        self.add_actor(self.early)
        self.early.set_font_size(20)
        self.early.x = self.width - self.early.get_width()
        self.early.y = self.height - self.early.get_height()
        self.Ver = game.scene2d.MyLabel("Version: 1.0")
        self.Ver.set_color(0, 0, 0)
        self.add_actor(self.Ver)
        self.Ver.x = self.width - self.Ver.get_width()
        self.Ver.y = self.height - self.Ver.get_height() - self.early.get_height()
        self.button1 = Button1()
        self.button2 = Button2()
        self.button3 = Button3()
        self.button4 = Button4()
        self.button5 = Button5()
        self.button2.x = self.width / 2 - 230
        self.button2.y = self.height / 2.5 + 130
        self.button4.y = self.height - self.button4.get_height()
        self.button4.x = 0
        self.button4.width = 300
        self.button4.height = 100
        self.button3.y = self.height / 2.5 - 60
        self.button3.x = self.width / 2 - 150
        self.button1.y = self.height / 2 - 320
        self.button1.x = self.width / 2 - 190
        self.button5.x = self.width - self.button5.get_width() * 2 + 15
        self.button5.y = 10
        self.button5.width = 75
        self.button5.height = 75
        self.add_actor(bg)
        self.add_actor(self.button3)
        self.add_actor(self.button1)
        self.add_actor(self.button4)
        self.add_actor(self.button2)
        self.add_actor(self.button5)
        self.devicelabel = game.scene2d.MyLabel("A gép neve:" + str(self.devicename))
        self.devicelabel.set_position(self.width / 2 - self.devicelabel.get_width() / 4, 0)
        self.devicelabel.set_font_size(40)
        self.devicelabel.set_color(0, 0, 0)
        self.add_actor(self.devicelabel)
        self.a = False
        self.d = False
        self.m = False
        self.i = False
        self.n = False

        self.set_on_key_down_listener(self.katt)
        self.button1.set_on_mouse_down_listener(self.Klikk1)
        self.button2.set_on_mouse_down_listener(self.Klikk2)
        self.button3.set_on_mouse_down_listener(self.Klikk3)
        self.button4.set_on_mouse_down_listener(self.Klikk4)
        self.button5.set_on_mouse_down_listener(self.Klikk5)
        self.options.set_on_mouse_down_listener(self.OptionsButton)
        self.set_on_key_down_listener(self.Admin1)

    def deviceread(self):
        with open('../kuposztok/Save/devices.txt', 'r') as device:
            self.alldevice = str(device.readline())
            device.close()

    def devicewrite(self):
        with open('../kuposztok/Save/devices.txt', 'r+') as device:
            self.alldevice = str(device.readline())
            self.deviceben = self.alldevice
            if self.deviceben == self.devicename:
                device.write("")
                
            if self.deviceben != self.devicename:
                device.write('\n' + str(self.devicename))
            device.close()

    def filebaolvasas(self):
        with open('../kuposztok/Save/file.txt', 'r') as file:
            self.max_score = int(file.readline())
            self.money = int(file.readline())
            file.close()

    def filebairas(self):
        with open('../kuposztok/Save/file.txt', 'w') as file:
            file.write(str(self.max_score))
            self.money = 0
            file.write("\n" + str(self.money + 60000000))
            file.close()

    def OptionsButton(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.options.OptionsScreen.OptionsScreen())

    def Klikk1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.CaraValt.CaraValtScreen.CaraValtScreen(money=self.money, maxScore=self.max_score))

    def Klikk2(self, sender, event):
        if event.button == 1:
            quit()

    def Klikk3(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Credit.CreditScreen.CreditScreen())


    def Klikk4(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Locker.LockerScreen.LockerScreen(money=self.money, max_score=self.max_score))

    def Klikk5(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Info.InfoScreen.InfoScreen())

    def katt(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()

    def Admin1(self, sender, event):
        if event.key == pygame.K_a:
            print("a")
            self.a = True
        if event.key == pygame.K_d:
            if self.a == True:
                print("d")
                self.d = True
        if event.key == pygame.K_m:
            if self.a == True and self.d == True:
                print("m")
                self.m = True
        if event.key == pygame.K_i:
            if self.a == True and self.d == True and self.m == True:
                print("i")
                self.i = True
        if event.key == pygame.K_n:
            if self.a == True and self.d == True and self.m == True and self.i == True:
                print("n")
                self.n = True
                self.filebairas()
