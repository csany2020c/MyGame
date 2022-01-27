import pygame

import game
import kuposztok
from kuposztok.CaraValt.CaraValtScreen import CaraValtScreen
from kuposztok.Credit.CreditScreen import CreditScreen
import kuposztok.Locker.LockerScreen
from kuposztok.Menu.MenuBgActor import *
from kuposztok.Info.InfoScreen import InfoScreen


class MenuStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        pygame.mixer.init()
        pygame.mixer.music.load("../kuposztok/music/menumusica.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
        bg = MenuActor()
        self.money = 0
        self.max_score = 0
        self.add_actor(bg)
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        bg.height = self.height
        bg.width = self.width
        self.early = game.scene2d.MyLabel("Early Access, Alpha Test")
        self.early.set_color(0, 0, 0)
        self.add_actor(self.early)
        self.early.set_font_size(20)
        self.early.x = self.width - self.early.get_width()
        self.early.y = self.height - self.early.get_height()
        self.Ver = game.scene2d.MyLabel("Version: 0.9.8")
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
        self.set_on_key_down_listener(self.Admin1)


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

    def act(self, delta_time: float,):
        super().act(delta_time)
        self.filebaolvasas()


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
