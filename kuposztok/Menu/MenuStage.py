import pygame

import game
import kuposztok
from kuposztok.CaraValt.CaraValtScreen import CaraValtScreen
from kuposztok.Credit.CreditScreen import CreditScreen
import kuposztok.Locker.LockerScreen
#from kuposztok.Menu.Read import Read
from kuposztok.Menu.MenuBgActor import *



class MenuStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        #self.money = Read.Read.getMoney()
        pygame.mixer.init()
        pygame.mixer.music.load("../kuposztok/CaraValt/music/kuposztokmusica.wav")
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
        print(self.width)
        print(self.height)
        self.Ver = game.scene2d.MyLabel("Ver.:0.6.1")
        self.Ver.set_color(0, 0, 0)
        self.add_actor(self.Ver)
        self.Ver.x = self.width - 250
        self.Ver.y = self.height - 50
        self.Ver.width = 100
        self.Ver.height = 50
        self.Ver.get_hitbox()
        self.Ver.hitbox_scale_w = 0.4
        self.Ver.hitbox_scale_h = 0.4
        self.Ver.hitbox_shape = game.simpleworld.ShapeType.Circle
        self.Ver.debug = True
        button1 = Button1()
        button2 = Button2()
        button3 = Button3()
        button4 = Button4()
        button2.x = self.width / 2 - 230
        button2.y = self.height / 2.5 + 130
        button4.y = self.height / 2.5 - 60
        button4.x = self.width / 2
        button3.y = self.height / 2.5 - 60
        button3.x = self.width / 2 - 150
        button1.y = self.height / 2 - 320
        button1.x = self.width / 2 - 190
        self.add_actor(bg)
        self.add_actor(button3)
        self.add_actor(button1)
        self.add_actor(button4)
        self.add_actor(button2)

        self.set_on_key_down_listener(self.katt)
        button1.set_on_mouse_down_listener(self.Klikk1)
        button2.set_on_mouse_down_listener(self.Klikk2)
        button3.set_on_mouse_down_listener(self.Klikk3)
        button4.set_on_mouse_down_listener(self.Klikk4)
        self.filebaolvasas()

    def filebaolvasas(self):
        with open('../kuposztok/Save/file.txt', 'r') as file:
            self.max_score = int(file.readline())
            self.money = int(file.readline())
            file.close()

    def act(self, delta_time: float,):
        super().act(delta_time)

    def Klikk1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.CaraValt.CaraValtScreen.CaraValtScreen(money=self.money, maxScore=self.max_score))


    def Klikk2(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(quit())

    def Klikk3(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Credit.CreditScreen.CreditScreen())


    def Klikk4(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Locker.LockerScreen.LockerScreen(money=self.money))
            pygame.mixer.init()
            pygame.mixer.music.load("../kuposztok/CaraValt/music/buttonmusica.wav")
            pygame.mixer.music.play(1)
            pygame.mixer.music.set_volume(0.2)

    def katt(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()

    #def getMenuMoney(self):
    #   return self.money