import kuposztok
import pygame
from kuposztok.CaraValt.CaraValtAct import *
import kuposztok.Menu.MenuScreen
from kuposztok.Game.CarOsszesScreen import CarOsszesScreen


randomvaltozo = 0

class CaraValtStage(game.scene2d.MyStage):
    def __init__(self, money: int, maxScore: int):
        super().__init__()
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        self.bg = BgActor()
        self.bg.width = self.width
        self.bg.height = self.height
        self.bg.y = 0
        self.add_actor(self.bg)

        self.money = money
        self.maxScore = maxScore

        self.scoreshow = game.scene2d.MyLabel("Az eddigi legjobb pontszámod:" + str(self.maxScore))
        self.scoreshow.x = self.width / 2 - self.scoreshow.get_width() / 2
        self.scoreshow.y = self.height / 1.5
        self.scoreshow.set_color(0, 0, 0)
        self.add_actor(self.scoreshow)

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

        """self.car5 = Randomplayer()
        self.car5.x = self.width / 2.5 - 100
        self.car5.y = self.height / 3
        self.add_actor(self.car5)"""

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
        self.car1multvalaszto.set_on_mouse_down_listener(self.Car1MultStart)
        self.car2multvalaszto.set_on_mouse_down_listener(self.Car2MultStart)
        self.car3multvalaszto.set_on_mouse_down_listener(self.Car3MultStart)
        self.car4multvalaszto.set_on_mouse_down_listener(self.Car4MultStart)
        self.button1.set_on_mouse_down_listener(self.Klikk1)
        self.set_on_key_down_listener(self.iranyitas)



    def iranyitas(self, sender, event, ):
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        if event.key == pygame.K_ESCAPE:
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())
        if event.key == pygame.K_F11:
            pygame.display.toggle_fullscreen()

    def Klikk1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())

    def Car1Start(self, sender, event):
        if event.button == 1:
            self.randomvaltozo = 11
            self.screen.game.set_screen(CarOsszesScreen(carvalt=self.randomvaltozo, money=self.money, maxScore=self.maxScore))


    def Car2Start(self, sender, event):
        if event.button == 1:
            self.randomvaltozo = 21
            self.screen.game.set_screen(CarOsszesScreen(carvalt=self.randomvaltozo, money=self.money, maxScore=self.maxScore))


    def Car3Start(self, sender, event):
        if event.button == 1:
            self.randomvaltozo = 31
            self.screen.game.set_screen(CarOsszesScreen(carvalt=self.randomvaltozo, money=self.money, maxScore=self.maxScore))


    def Car4Start(self, sender, event):
        if event.button == 1:
            self.randomvaltozo = 41
            self.screen.game.set_screen(CarOsszesScreen(carvalt=self.randomvaltozo, money=self.money, maxScore=self.maxScore))


    def Car1MultStart(self, sender, event):
        if event.button == 1:
            self.randomvaltozo = 12
            self.screen.game.set_screen(CarOsszesScreen(carvalt=self.randomvaltozo, money=self.money, maxScore=self.maxScore))

    def Car2MultStart(self, sender, event):
        if event.button == 1:
            self.randomvaltozo = 22
            self.screen.game.set_screen(CarOsszesScreen(carvalt=self.randomvaltozo, money=self.money, maxScore=self.maxScore))

    def Car3MultStart(self, sender, event):
        if event.button == 1:
            self.randomvaltozo = 32
            self.screen.game.set_screen(CarOsszesScreen(carvalt=self.randomvaltozo, money=self.money, maxScore=self.maxScore))

    def Car4MultStart(self, sender, event):
        if event.button == 1:
            self.randomvaltozo = 42
            self.screen.game.set_screen(CarOsszesScreen(carvalt=self.randomvaltozo, money=self.money, maxScore=self.maxScore))

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

