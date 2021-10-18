import game
import pygame
import random

class snow (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("../!_resources/images/snow.png")

    def act(self, delta_time: float):
        self.y += delta_time * 250
        if self.y > 720:
            self.y = 0

class raindrop (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("../!_resources/images/rain.png")

    def act(self, delta_time: float):
        self.y += delta_time * 500
        if self.y > 720:
            self.y = 0

class cloudy (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("../!_resources/images/cloudy.png")






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
        self.set_on_key_down_listener(self.kitt)




    def kitt(self, sender, event):
        print(event)
        if event.key == pygame.K_RIGHT:
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
        for i in range(30):
            self.c = raindrop()
            self.add_actor(self.c)
            self.c.x = random.randint(0,1280)
            self.c.y = random.randint(0,720)
            self.c.width = 60





        self.set_on_key_press_listener(self.kett)







    def kett (self, sender, event):
        print(event)
        if event.key == pygame.K_RIGHT:
            self.screen.game.set_screen(SnowScreen())






class SnowStage (game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.a = cloudy()
        self.b = landscape()


        self.add_actor(self.a)
        self.add_actor(self.b)

        for i in range(30):
            self.c = snow()
            self.add_actor(self.c)
            self.c.x = random.randint(0,1280)
            self.c.y = random.randint(0,720)
            self.c.width = 60
        self.set_on_key_down_listener(self.kott)


    def kott(self, sender, event):
        print(event)
        if event.key == pygame.K_RIGHT:
         self.screen.game.set_screen(BlizzardScreen())
            

class Blizzard (game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.a = cloudy()
        self.b = landscape()
        self.c = raindrop()
        self.d = snow()

        self.add_actor(self.a)
        self.add_actor(self.b)


        for i in range(30):
            self.c = raindrop()
            self.add_actor(self.c)
            self.c.x = random.randint(0,1280)
            self.c.y = random.randint(0,720)
            self.c.width = 60

        for i in range(30):
            self.d = snow()
            self.add_actor(self.d)
            self.d.x = random.randint(0,1280)
            self.d.y = random.randint(0,720)
            self.d.width = 60
        self.set_on_key_down_listener(self.f)

    def f (self, sender, event):
        print(event)
        if event.key == pygame.K_RIGHT:
            self.screen.game.set_screen(DaniScreen())



class BlizzardScreen (game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(Blizzard())


class SnowScreen (game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(SnowStage())






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
        self.set_on_key_down_listener(self.ketty)

    def ketty(self, sender, event):
        print(event)
        if event.key == pygame.K_ESCAPE:
            quit()


danigame = DaniGame()

danigame.run()
