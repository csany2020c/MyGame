from pgzero import music

import kuposztok
from kuposztok.CaraValt.CaraValtAct import *
import kuposztok.Menu.MenuScreen
from kuposztok.Game.Car1Screen import Car1Screen
from kuposztok.Game.Car2Screen import Car2Screen
from kuposztok.Game.Car3Screen import Car3Screen
from kuposztok.Game.Car4Screen import Car4Screen
import pygame


class CaraValtStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        self.bg = BgActor()
        self.bg.width = self.width
        self.bg.height = self.height
        self.bg.y = 0
        self.add_actor(self.bg)

        self.button1 = Visszagomb()
        self.add_actor(self.button1)
        self.button1.width = 125
        self.button1.height = 75
        self.button1.y = 0
        self.button1.x = 0

        self.car1 = SnowBoard()
        self.car1.x = self.width / 2 - 100
        self.car1.y = self.height / 2

        self.car2 = Sledge()
        self.car2.x = self.width / 2 - 100
        self.car2.y = self.height / 2

        self.car3 = SnowMobile()
        self.car3.x = self.width / 2 - 100
        self.car3.y = self.height / 2

        self.car4 = Ski()
        self.car4.x = self.width / 2 - 100
        self.car4.y = self.height / 2

        self.car1valaszto = SnowMobile()
        self.car1valaszto.x = self.width / 5 - 100
        self.car1valaszto.y = self.height / 5
        self.add_actor(self.car1valaszto)

        self.car2valaszto = Sledge()
        self.car2valaszto.x = self.width / 2.5 - 100
        self.car2valaszto.y = self.height / 5
        self.add_actor(self.car2valaszto)

        self.car3valaszto= SnowBoard()
        self.car3valaszto.x = self.width / 1.66666666666 -100
        self.car3valaszto.y = self.height / 5 + 75
        self.add_actor(self.car3valaszto)

        self.car4valaszto = Ski()
        self.car4valaszto.x = self.width / 1.25 - 100
        self.car4valaszto.y = self.height / 5 + 75
        self.add_actor(self.car4valaszto)

        self.car1start = PlayButton()
        self.car1start.x = self.width / 2 -200
        self.car1start.y = self.height / 1.666666666666 + 100

        self.car2start = PlayButton()
        self.car2start.x = self.width / 2 - 200
        self.car2start.y = self.height / 1.666666666666 + 100

        self.car3start = PlayButton()
        self.car3start.x = self.width / 2 - 200
        self.car3start.y = self.height / 1.666666666666 + 100

        self.car4start = PlayButton()
        self.car4start.x = self.width / 2 - 200
        self.car4start.y = self.height / 1.666666666666 + 100
        self.add_actor(self.car4start)

        self.car1valaszto.set_on_mouse_down_listener(self.Actvalt1)
        self.car2valaszto.set_on_mouse_down_listener(self.Actvalt2)
        self.car3valaszto.set_on_mouse_down_listener(self.Actvalt3)
        self.car4valaszto.set_on_mouse_down_listener(self.Actvalt4)
        self.car1start.set_on_mouse_down_listener(self.Car1Start)
        self.car2start.set_on_mouse_down_listener(self.Car2Start)
        self.car3start.set_on_mouse_down_listener(self.Car3Start)
        self.car4start.set_on_mouse_down_listener(self.Car4Start)
        self.button1.set_on_mouse_down_listener(self.Klikk1)
        self.set_on_key_down_listener(self.iranyitas)

    def iranyitas(self, sender, event, ):
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        if event.key == pygame.K_ESCAPE:
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())

    def Klikk1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())

    def Car1Start(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Game.Car1Screen.Car1Screen())

    def Car2Start(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Game.Car2Screen.Car2Screen())

    def Car3Start(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Game.Car3Screen.Car3Screen())

    def Car4Start(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Game.Car4Screen.Car4Screen())

    #3
    def Actvalt1(self, sender, event):
        if event.button == 1:
            self.add_actor(self.car1)
            self.add_actor(self.car2)
            self.add_actor(self.car3)
            self.add_actor(self.car4)
            self.add_actor(self.car1start)
            self.add_actor(self.car2start)
            self.add_actor(self.car3start)
            self.add_actor(self.car4start)
            self.remove_actor(self.car1)
            self.remove_actor(self.car2)
            self.remove_actor(self.car4)
            self.remove_actor(self.car1start)
            self.remove_actor(self.car2start)
            self.remove_actor(self.car4start)
    #2
    def Actvalt2(self, sender, event):
        if event.button == 1:
            self.add_actor(self.car1)
            self.add_actor(self.car2)
            self.add_actor(self.car3)
            self.add_actor(self.car4)
            self.add_actor(self.car1start)
            self.add_actor(self.car2start)
            self.add_actor(self.car3start)
            self.add_actor(self.car4start)
            self.remove_actor(self.car1)
            self.remove_actor(self.car3)
            self.remove_actor(self.car4)
            self.remove_actor(self.car1start)
            self.remove_actor(self.car3start)
            self.remove_actor(self.car4start)

    #1
    def Actvalt3(self, sender, event):
        if event.button == 1:
            self.add_actor(self.car1)
            self.add_actor(self.car2)
            self.add_actor(self.car3)
            self.add_actor(self.car4)
            self.add_actor(self.car1start)
            self.add_actor(self.car2start)
            self.add_actor(self.car3start)
            self.add_actor(self.car4start)
            self.remove_actor(self.car3)
            self.remove_actor(self.car2)
            self.remove_actor(self.car4)
            self.remove_actor(self.car3start)
            self.remove_actor(self.car2start)
            self.remove_actor(self.car4start)

    #4
    def Actvalt4(self, sender, event):
        if event.button == 1:
            self.add_actor(self.car1)
            self.add_actor(self.car2)
            self.add_actor(self.car3)
            self.add_actor(self.car4)
            self.add_actor(self.car1start)
            self.add_actor(self.car2start)
            self.add_actor(self.car3start)
            self.add_actor(self.car4start)
            self.remove_actor(self.car3)
            self.remove_actor(self.car2)
            self.remove_actor(self.car1)
            self.remove_actor(self.car3start)
            self.remove_actor(self.car2start)
            self.remove_actor(self.car1start)


