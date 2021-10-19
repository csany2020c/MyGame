import pygame
import game
import random


class Menu(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720):
        super().__init__(width, height)
        self.screen = FoScreen()

    #def gombocska(self, sender, event):
        #if event.key == pygame.K_ESCAPE:
            #quit()


class rain (game.scene2d.MyActor):
    def __init__(self):
        super(rain, self).__init__("../!_resources/images/rain.png")
        #a


    def act(self, delta_time: float):
        game.scene2d.MyLabel.act(self, delta_time)
        if self.x + self.width < game.scene2d.MyGame.get_screen_width():
            self.y += delta_time * 10


class cloudy (game.scene2d.MyActor):
    def __init__(self):
        super(cloudy, self).__init__("../!_resources/images/cloudy.png")
        #b

class snow (game.scene2d.MyActor):
    def __init__(self):
        super(snow, self).__init__("../!_resources/images/snow.png")
        #c

    def act(self, delta_time: float):
        game.scene2d.MyLabel.act(self, delta_time)
        if self.x + self.width < game.scene2d.MyGame.get_screen_width():
            self.y += delta_time * 10

class landscape (game.scene2d.MyActor):
    def __init__(self):
        super(landscape, self).__init__("../!_resources/images/landscape.png")
        #d
    def gomb(self, sender, event):
        print(sender)
        print(event)

class sun (game.scene2d.MyActor):
    def __init__(self):
        super(sun, self).__init__("../!_resources/images/sun.png")
        #e

class sunny (game.scene2d.MyActor):
    def __init__(self):
        super(sunny, self).__init__("../!_resources/images/sunny.png")
        #f



class FoScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(FoStage())

class HavasesoScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(HavasesoStage())

class EsoScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(EsoStage())

class NapScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(NapStage())



class FoStage(game.scene2d.MyStage):
    #havas
    def __init__(self):
        super().__init__()
        self.c = snow()
        self.b = cloudy()
        self.d = landscape()
        self.add_actor(self.c)
        self.add_actor(self.b)
        self.add_actor(self.d)
        self.set_on_key_down_listener(self.jobbra)

        for i in range(200):
            self.c = snow()
            self.add_actor(self.c)
            self.c.x = random.randint(0, 1250)
            self.c.y = random.randint(0, 720)
            self.c.width = 15
            self.c.height = 15

    def jobbra(self, sender, event):
        print(event)
        if event.key == pygame.K_RIGHT:
            self.screen.game.set_screen(HavasesoScreen())

class HavasesoStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.c = snow()
        self.a = rain()
        self.b = cloudy()
        self.d = landscape()
        self.add_actor(self.c)
        self.add_actor(self.a)
        self.add_actor(self.b)
        self.add_actor(self.d)
        self.set_on_key_down_listener(self.megjobbra)


        for i in range(200):
            self.a = rain()
            self.add_actor(self.a)
            self.a.x = random.randint(0, 1250)
            self.a.y = random.randint(0, 720)
            self.a.width = 15
            self.a.height = 15

        for i in range(200):
            self.c = snow()
            self.add_actor(self.c)
            self.c.x = random.randint(0, 1250)
            self.c.y = random.randint(0, 720)
            self.c.width = 15
            self.c.height = 15

    def megjobbra(self, sender, event):
        print(event)
        if event.key == pygame.K_RIGHT:
            self.screen.game.set_screen(EsoScreen())


class EsoStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.a = rain()
        self.b = cloudy()
        self.d = landscape()
        self.add_actor(self.a)
        self.add_actor(self.b)
        self.add_actor(self.d)
        self.set_on_key_down_listener(self.meeg)


        for i in range(200):
            self.a = rain()
            self.add_actor(self.a)
            self.a.x = random.randint(0, 1250)
            self.a.y = random.randint(0, 720)
            self.a.width = 15
            self.a.height = 15

    def meeg(self, sender, event):
        print(event)
        if event.key == pygame.K_RIGHT:
            self.screen.game.set_screen(NapScreen())

class NapStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.f = sunny()
        self.e = sun()
        self.d = landscape()
        self.add_actor(self.f)
        self.add_actor(self.e)
        self.add_actor(self.d)
        self.e.set_x(500).set_y(60)
        self.set_on_key_down_listener(self.meeeg)

    def meeeg(self, sender, event):
        print(event)
        if event.key == pygame.K_RIGHT:
            self.screen.game.set_screen(FoScreen())


class FoGame(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False,
                 debug: bool = False):
        super().__init__(width, height, autorun, autosize, debug)







fogame = FoGame()

Menu().run()