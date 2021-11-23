import kuposztok
import pygame
from kuposztok.CaraValt.CaraValtAct import *
import kuposztok.Menu.MenuScreen
from kuposztok.Game.Car1Screen import Car1Screen
from kuposztok.Game.Car2Screen import Car2Screen
from kuposztok.Game.Car3Screen import Car3Screen
from kuposztok.Game.Car4Screen import Car4Screen
from kuposztok.Game.Car1Multi.Car1ScreenMultiP import Car1ScreenMultiP
from kuposztok.Game.Car2Multi.Car2ScreenMultiP import Car2ScreenMultiP
from kuposztok.Game.Car3Multi.Car3ScreenMultiP import Car3ScreenMultiP
from kuposztok.Game.Car4Multi.Car4ScreenMultiP import Car4ScreenMultiP
from kuposztok.Game.CarOsszesScreen import CarOsszesScreen


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

        self.car1 = Single()
        self.car1.x = self.width / 2 - 200
        self.car1.y = self.height / 2

        self.car2 = Single()
        self.car2.x = self.width / 2 - 200
        self.car2.y = self.height / 2

        self.car3 = Single()
        self.car3.x = self.width / 2 - 200
        self.car3.y = self.height / 2

        self.car4 = Single()
        self.car4.x = self.width / 2 - 200
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
        self.car3valaszto.x = self.width / 1.66666666666 - 100
        self.car3valaszto.y = self.height / 5 + 75
        self.add_actor(self.car3valaszto)

        self.car4valaszto = Ski()
        self.car4valaszto.x = self.width / 1.25 - 100
        self.car4valaszto.y = self.height / 5 + 75
        self.add_actor(self.car4valaszto)

        self.car5 = Randomplayer()
        self.car5.x = self.width / 2.5 - 100
        self.car5.y = self.height / 3
        self.add_actor(self.car5)

        self.car1multvalaszto = Multi()
        self.car1multvalaszto.x = self.width / 2 + 100
        self.car1multvalaszto.y = self.height / 2

        self.car2multvalaszto = Multi()
        self.car2multvalaszto.x = self.width / 2 + 100
        self.car2multvalaszto.y = self.height / 2

        self.car3multvalaszto = Multi()
        self.car3multvalaszto.x = self.width / 2 + 100
        self.car3multvalaszto.y = self.height / 2

        self.car4multvalaszto = Multi()
        self.car4multvalaszto.x = self.width / 2 + 100
        self.car4multvalaszto.y = self.height / 2

        self.car1valaszto.set_on_mouse_down_listener(self.Actvalt1)
        self.car2valaszto.set_on_mouse_down_listener(self.Actvalt2)
        self.car3valaszto.set_on_mouse_down_listener(self.Actvalt3)
        self.car4valaszto.set_on_mouse_down_listener(self.Actvalt4)
        self.car1.set_on_mouse_down_listener(self.Car1Start)
        self.car2.set_on_mouse_down_listener(self.Car2Start)
        self.car3.set_on_mouse_down_listener(self.Car3Start)
        self.car4.set_on_mouse_down_listener(self.Car4Start)
        self.car4.set_on_mouse_down_listener(self.Car5MultStart)
        self.car1multvalaszto.set_on_mouse_down_listener(self.Car1MultStart)
        self.car2multvalaszto.set_on_mouse_down_listener(self.Car2MultStart)
        self.car3multvalaszto.set_on_mouse_down_listener(self.Car3MultStart)
        self.car4multvalaszto.set_on_mouse_down_listener(self.Car4MultStart)
        self.button1.set_on_mouse_down_listener(self.Klikk1)
        self.set_on_key_down_listener(self.iranyitas)

        self.randomvaltozo = None


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
            self.randomvaltozo = 11

    def Car2Start(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Game.Car2Screen.Car2Screen())
            self.randomvaltozo = 21

    def Car3Start(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Game.Car3Screen.Car3Screen())
            self.randomvaltozo = 31

    def Car4Start(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Game.Car4Screen.Car4Screen())
            self.randomvaltozo = 41

    def Car5Start(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Game.CarOsszesScreen.CarOsszesScreen())
            self.randomvaltozo = 51

    def Car1MultStart(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Game.Car1Multi.Car1ScreenMultiP.Car1ScreenMultiP())
            self.randomvaltozo = 12

    def Car2MultStart(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Game.Car2Multi.Car2ScreenMultiP.Car2ScreenMultiP())
            self.randomvaltozo = 22

    def Car3MultStart(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Game.Car3Multi.Car3ScreenMultiP.Car3ScreenMultiP())
            self.randomvaltozo = 32

    def Car4MultStart(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Game.Car4Multi.Car4ScreenMultiP.Car4ScreenMultiP())
            self.randomvaltozo = 42

    def Car5MultStart(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Game.CarOsszesScreen.CarOsszesScreen())
            self.randomvaltozo = 1


    #3
    def Actvalt1(self, sender, event):
        if event.button == 1:
            self.add_actor(self.car1)
            self.add_actor(self.car2)
            self.add_actor(self.car3)
            self.add_actor(self.car4)
            self.remove_actor(self.car1)
            self.remove_actor(self.car2)
            self.remove_actor(self.car4)
            self.add_actor(self.car1multvalaszto)
            self.add_actor(self.car2multvalaszto)
            self.remove_actor(self.car2multvalaszto)
            self.add_actor(self.car3multvalaszto)
            self.remove_actor(self.car3multvalaszto)
            self.add_actor(self.car4multvalaszto)
            self.remove_actor(self.car4multvalaszto)

    #2
    def Actvalt2(self, sender, event):
        if event.button == 1:
            self.add_actor(self.car1)
            self.add_actor(self.car2)
            self.add_actor(self.car3)
            self.add_actor(self.car4)
            self.remove_actor(self.car1)
            self.remove_actor(self.car3)
            self.remove_actor(self.car4)
            self.add_actor(self.car1multvalaszto)
            self.remove_actor(self.car1multvalaszto)
            self.add_actor(self.car2multvalaszto)
            self.add_actor(self.car3multvalaszto)
            self.remove_actor(self.car3multvalaszto)
            self.add_actor(self.car4multvalaszto)
            self.remove_actor(self.car4multvalaszto)

    #1
    def Actvalt3(self, sender, event):
        if event.button == 1:
            self.add_actor(self.car1)
            self.add_actor(self.car2)
            self.add_actor(self.car3)
            self.add_actor(self.car4)
            self.remove_actor(self.car3)
            self.remove_actor(self.car2)
            self.remove_actor(self.car4)
            self.add_actor(self.car1multvalaszto)
            self.remove_actor(self.car1multvalaszto)
            self.add_actor(self.car2multvalaszto)
            self.remove_actor(self.car2multvalaszto)
            self.add_actor(self.car3multvalaszto)
            self.add_actor(self.car4multvalaszto)
            self.remove_actor(self.car4multvalaszto)

    #4
    def Actvalt4(self, sender, event):
        if event.button == 1:
            self.add_actor(self.car1)
            self.add_actor(self.car2)
            self.add_actor(self.car3)
            self.add_actor(self.car4)
            self.remove_actor(self.car3)
            self.remove_actor(self.car2)
            self.remove_actor(self.car1)
            self.add_actor(self.car1multvalaszto)
            self.remove_actor(self.car1multvalaszto)
            self.add_actor(self.car2multvalaszto)
            self.remove_actor(self.car2multvalaszto)
            self.add_actor(self.car3multvalaszto)
            self.remove_actor(self.car3multvalaszto)
            self.add_actor(self.car4multvalaszto)

    def RandomVariable(self):
        return self.randomvaltozo
