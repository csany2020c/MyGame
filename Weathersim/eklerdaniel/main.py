import game
import pygame
import random

class snow (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("../!resources/images/snow.png")

class raindrop (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("../!_resources/images/rain.png")

class cloudy (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("../!_resources/images/cloudy.png")
        self.set_on_mouse_down_listener





class sunny (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("../!_resources/images/sunny.png")
        # self.set_on_key_down_listener(2)





class sun (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("../!_resources/images/sun.png")



class landscape (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("../!_resources/images/landscape.png")
        self.set_on_mouse_down_listener(self.klikk)

    def klikk(self, sender, event):
        print(sender)
        print(event)

class DaniStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.a = sunny()
        self.b = sun()
        self.c = landscape()
        self.add_actor(self.a)
        self.add_actor(self.b)
        self.add_actor(self.c)

        self.b.x = 600
        self.set_on_mouse_down_listener(self.kitt)
        self.set_on_key_down_listener(self.kitt)

    def kitt(self, sender, event):
        print(event)
        if event.key == pygame.K_2:
        # if event.button == 1:
            self.screen.game.set_screen(RainScreen())


    def act(self, delta_time: float):
        super().act(delta_time)


class RainStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.a = cloudy()
        self.b = landscape()


        self.add_actor(self.a)
        self.add_actor(self.b)
        for i in range(20):
            self.c = raindrop()
            self.add_actor(self.c)
            self.c.x = random.randint(10,1000)


    def act(self, delta_time: float):
        super().act(delta_time)
        self.c.y += delta_time * 1500

        self.set_on_mouse_down_listener(self.katt)
        self.set_on_key_press_listener(self.katt)


    def katt (self, sender, event):
        # if event.button == 1:
        if event.key == pygame.K_1:
         self.screen.game.set_screen(DaniScreen())


class SnowScreen (game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(SnowStage)

class SnowStage (game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.a = cloudy
        self.b = landscape
        self.c = snow

        self.add_actor(self.a)
        self.add_actor(self.b)
        self.add_actor(self.c)

    def kett(self, sender, event):
        print(event)
        if event.key == pygame.K_3:
        # if event.button == 1:
            self.screen.game.set_screen(SnowScreen)




class DaniScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(DaniStage())

class RainScreen (game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(RainStage())





class DaniGame(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False,
                 debug: bool = False):
        super().__init__(width, height, autorun, autosize, debug)
        self.set_screen(DaniScreen())



danigame = DaniGame()
danigame.run()
