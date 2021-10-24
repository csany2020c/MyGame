import kuposztok
from kuposztok.CaraValt.CaraValtAct import *
from kuposztok.Menu.MenuScreen import MenuScreen
import pygame


class CaraValtStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        self.bg = BgActor()
        self.bg.width = 2400
        self.bg.height = 1400
        self.bg.y = 0
        self.add_actor(self.bg)

        self.button1 = Visszagomb()
        self.add_actor(self.button1)
        self.button1.width = 125
        self.button1.height = 75
        self.button1.y = 0
        self.button1.x = 0

        self.car1 = Car1()
        self.car1.x = self.width / 2.4
        self.car1.y = self.height / 2.5

        self.car2 = Car2()
        self.car2.x = self.width / 2.4
        self.car2.y = self.height / 2.5

        self.car3 = Car3()
        self.car3.x = self.width / 2.4
        self.car3.y = self.height / 2.5

        self.car1elo = Car1()
        self.car1elo.x = self.width / 2
        self.car1elo.y = self.height / 7
        self.add_actor(self.car1elo)

        self.car2elo = Car2()
        self.car2elo.x = self.width / 3
        self.car2elo.y = self.height / 7
        self.add_actor(self.car2elo)

        self.car3elo = Car3()
        self.car3elo.x = self.width / 7
        self.car3elo.y = self.height / 7
        self.add_actor(self.car3elo)

        self.car1start = Car1()
        self.car1start.x = self.width / 2
        self.car1start.y = self.height / 3

        self.car2start = Car2()
        self.car2start.x = self.width / 3
        self.car2start.y = self.height / 3

        self.car3start = Car3()
        self.car3start.x = self.width / 7
        self.car3start.y = self.height / 3
        #self.car4elo = Car3()
        #self.car4elo.x = self.width / 3.2
        #self.car4elo.y = self.height / 2.5
        #self.add_actor(self.car4elo)

        self.car1elo.set_on_mouse_down_listener(self.Actvalt1)
        self.car2elo.set_on_mouse_down_listener(self.Actvalt2)
        self.car3elo.set_on_mouse_down_listener(self.Actvalt3)
        #self.car4elo.set_on_mouse_down_listener(self.Actvalt4)
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

    #3
    def Actvalt1(self, sender, event):
        if event.button == 1:
            self.add_actor(self.car1)
            self.add_actor(self.car2)
            self.add_actor(self.car3)
            self.add_actor(self.car1start)
            self.add_actor(self.car2start)
            self.add_actor(self.car3start)
            self.remove_actor(self.car1)
            self.remove_actor(self.car2)
            self.remove_actor(self.car1start)
            self.remove_actor(self.car2start)
    #2
    def Actvalt2(self, sender, event):
        if event.button == 1:
            self.add_actor(self.car1)
            self.add_actor(self.car2)
            self.add_actor(self.car3)
            self.add_actor(self.car1start)
            self.add_actor(self.car2start)
            self.add_actor(self.car3start)
            self.remove_actor(self.car1)
            self.remove_actor(self.car3)
            self.remove_actor(self.car1start)
            self.remove_actor(self.car3start)

    #1
    def Actvalt3(self, sender, event):
        if event.button == 1:
            self.add_actor(self.car1)
            self.add_actor(self.car2)
            self.add_actor(self.car3)
            self.add_actor(self.car1start)
            self.add_actor(self.car2start)
            self.add_actor(self.car3start)
            self.remove_actor(self.car3)
            self.remove_actor(self.car2)
            self.remove_actor(self.car3start)
            self.remove_actor(self.car2start)

    #majd4.
    #def Actvalt4(self, sender, event):
        #if event.button == 1:
            #self.add_actor(self.car1)
            #self.add_actor(self.car2)
            #elf.add_actor(self.car3)
            #self.remove_actor(self.car2)
            #self.remove_actor(self.car1)

