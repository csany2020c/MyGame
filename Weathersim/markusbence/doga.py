import game
import random
import pygame

class nap(game.scene2d.MyActor):
    def __init__(self):
        super().__init__('images/sun.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(0.4)

class rain(game.scene2d.MyActor):
    def __init__(self):
        super().__init__('images/rain.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 100
        if self.y > 720:
            self.y = -50

class snow(game.scene2d.MyActor):
    def __init__(self):
        super().__init__('images/snow.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 100
        if self.y > 720:
            self.y = -50

class cloudy(game.scene2d.MyActor):
    def __init__(self):
        super().__init__('images/cloudy.png')

class hatter(game.scene2d.MyActor):
    def __init__(self):
        super().__init__('images/landscape.png')

class sunny(game.scene2d.MyActor):
    def __init__(self):
        super().__init__('images/sunny.png')

class felhocske(game.scene2d.MyActor):
    def __init__(self):
        super().__init__('images/felhocske.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 40
        if self.x > 1200:
            self.x = 200

class taj(game.scene2d.MyActor):
    def __init__(self):
        super().__init__('images/taj.jpg')

class button1(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('images/rainicon.png')

class button2(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('images/havasesoicon.jpg')

class button3(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('images/sunicon.png')

class button4(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('images/hav.png')


class rainicon(game.scene2d.MyActor):
    def __init__(self):
        super().__init__('images/rainicon.png')

class havasesoicon(game.scene2d.MyActor):
    def __init__(self):
        super().__init__('images/havasesoicon.jpg')

class sunicon(game.scene2d.MyActor):
    def __init__(self):
        super().__init__('images/sunicon.png')

class hav(game.scene2d.MyActor):
    def __init__(self):
        super().__init__('images/hav.png')



class MenuStage(game.scene2d.MyStage):

    def __init__(self):
        super(MenuStage, self).__init__()
        self.taj = taj()
        self.add_actor(self.taj)
        self.taj.z_index = 1
        self.rainicon = rainicon()
        self.rainicon.x = 450
        self.rainicon.y = 300
        self.add_actor(self.rainicon)
        self.button1 = button1()
        self.add_actor(self.button1)
        self.button1.x = 450
        self.button1.y = 300
        self.button1.z_index = 2
        self.button1.set_on_mouse_down_listener(self.klikk1)
        self.havasesoicon = havasesoicon()
        self.havasesoicon.x = 550
        self.havasesoicon.y = 300
        self.add_actor(self.havasesoicon)
        self.button2 = button2()
        self.add_actor(self.button2)
        self.button2.x = 550
        self.button2.y = 300
        self.button2.z_index = 2
        self.button2.set_on_mouse_down_listener(self.klikk2)
        self.sunicon = sunicon()
        self.sunicon.x = 650
        self.sunicon.y = 300
        self.add_actor(self.sunicon)
        self.button3 = button3()
        self.add_actor(self.button3)
        self.button3.x = 650
        self.button3.y = 300
        self.button3.z_index = 2
        self.button3.set_on_mouse_down_listener(self.klikk3)
        self.hav = hav()
        self.hav.x = 750
        self.hav.y = 300
        self.add_actor(self.hav)
        self.button4 = button4()
        self.add_actor(self.button4)
        self.button4.x = 750
        self.button4.y = 300
        self.button4.z_index = 2
        self.button4.set_on_mouse_down_listener(self.klikk4)

        self.set_on_key_down_listener(self.nyom1)



    def klikk1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(RainScreen())

    def klikk2(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(HavasesoScreen())

    def klikk3(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(SunnyScreen())

    def klikk4(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(SnowScreen())


    def nyom1(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()


class RainStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.rain=rain()
        self.rain.z_index = 4
        self.rain.x=850
        self.rain.y=-130
        self.add_actor(self.rain)
        self.landscape=hatter()
        self.landscape.z_index = 3
        self.add_actor(self.landscape)
        self.cloudy=cloudy()
        self.add_actor(self.cloudy)
        self.cloudy.z_index = 1
        self.felhocske = felhocske()
        self.felhocske.x =850
        self.felhocske.y =-20
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x =630
        self.felhocske.y =-20
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x =410
        self.felhocske.y =-20
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x =190
        self.felhocske.y =-20
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske.x = 1070
        self.felhocske.y = -20
        self.felhocske.z_index = 1
        self.add_actor(self.felhocske)

        for i in range(80):
            self.rain = rain()
            self.rain.width = 70
            self.rain.height = 70
            self.add_actor(self.rain)
            self.rain.x = random.Random().randint(0, 1280)
            self.rain.y = random.Random().randint(0, 720)
        self.set_on_key_down_listener(self.nyom2)

    def nyom2(self, sender, event):
        if event.key==pygame.K_ESCAPE:
            self.screen.game.set_screen(MenuScreen())




class SnowStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.snow = snow()
        self.snow.x = 850
        self.snow.y = -130
        self.add_actor(self.snow)
        self.landscape = hatter()
        self.landscape.z_index = 2
        self.add_actor(self.landscape)
        self.cloudy = cloudy()
        self.cloudy.z_index = 1
        self.add_actor(self.cloudy)
        self.snow.z_index = 3
        for i in range(50):
            self.snow = snow()
            self.snow.width = 70
            self.snow.height = 70
            self.add_actor(self.snow)
            self.snow.x = random.Random().randint(0,1280)
            self.snow.y = random.Random().randint(0,720)
        self.felhocske = felhocske()
        self.felhocske.x = 850
        self.felhocske.y = -20
        self.felhocske.z_index = 1
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x = 630
        self.felhocske.y = -20
        self.felhocske.z_index = 1
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x = 410
        self.felhocske.y = -20
        self.felhocske.z_index = 1
        self.add_actor(self.felhocske)
        self.felhocske.x = 190
        self.felhocske.y = -20
        self.felhocske.z_index = 1
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x = 1070
        self.felhocske.y = -20
        self.felhocske.z_index = 1
        self.add_actor(self.felhocske)
        self.set_on_key_down_listener(self.nyom3)

    def nyom3(self, sender, event):
        if event.key==pygame.K_ESCAPE:
            self.screen.game.set_screen(MenuScreen())


class SunnyStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.sunny = sunny()
        self.sunny.x = 0
        self.sunny.y = 0
        self.add_actor(self.sunny)
        self.landscape = hatter()
        self.add_actor(self.landscape)
        self.sun = nap()
        self.sun.x = 850
        self.sun.y = -95
        self.add_actor(self.sun)
        self.sunny.z_index = 4
        self.set_on_key_down_listener(self.nyom4)

    def nyom4(self, sender, event):
        if event.key==pygame.K_ESCAPE:
            self.screen.game.set_screen(MenuScreen())



class HavasesoStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.cloudy = cloudy()
        self.cloudy.x = 0
        self.cloudy.y = 0
        self.add_actor(self.cloudy)
        self.cloudy.z_index = 1
        self.landscape = hatter()
        self.landscape.z_index = 2
        self.add_actor(self.landscape)
        for i in range(50):
            self.snow = snow()
            self.snow.width = 70
            self.snow.height = 70
            self.add_actor(self.snow)
            self.snow.x = random.Random().randint(0, 1280)
            self.snow.y = random.Random().randint(0, 720)
        for i in range(60):
            self.rain = rain()
            self.rain.width = 40
            self.rain.height = 40
            self.add_actor(self.rain)
            self.rain.x = random.Random().randint(0, 1280)
            self.rain.y = random.Random().randint(0, 720)
        self.felhocske = felhocske()
        self.felhocske.x =850
        self.felhocske.y =-20
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x =630
        self.felhocske.y =-20
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x =410
        self.felhocske.y =-20
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x =190
        self.felhocske.y =-20
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske.x = 1070
        self.felhocske.y = -20
        self.felhocske.z_index = 1
        self.add_actor(self.felhocske)

        self.set_on_key_down_listener(self.nyom5)

    def nyom5(self, sender, event):
        if event.key==pygame.K_ESCAPE:
            self.screen.game.set_screen(MenuScreen())


class MenuScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0)
        self.add_stage(MenuStage())


class RainScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0)
        self.add_stage(RainStage())


class SnowScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0)
        self.add_stage(SnowStage())


class SunnyScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0)
        self.add_stage(SunnyStage())


class HavasesoScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0)
        self.add_stage(HavasesoStage())


class Program(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = MenuScreen()


Program().run()





