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
        self.y += delta_time * 200
        if self.y > 720:
            self.y = -50

class snow(game.scene2d.MyActor):
    def __init__(self):
        super().__init__('images/snow.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 200
        if self.y > 720:
            self.y = -50

class cloudy(game.scene2d.MyActor):
    def __init__(self):
        super().__init__('images/cloudy.png')

class landscape(game.scene2d.MyActor):
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
        self.x += delta_time * 50
        if self.x > 1300:
            self.x = 50

class menustage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.nap=nap()
        self.nap.x=850
        self.nap.y=-130
        self.add_actor(self.nap)
        self.button1=nap()
        self.add_actor(self.button1)
        self.button1.x = 850
        self.button1.y = 200
        self.button1.z_index=4
        self.button1.set_on_mouse_down_listener(self.katt1)
        self.set_on_key_down_listener(self.nyom1)
        self.button2=nap()
        self.add_actor(self.button2)
        self.button2.x = -200
        self.button2.y = -110
        self.button2.z_index = 4
        self.button2.set_on_mouse_down_listener(self.katt2)
        self.button3=snow()
        self.add_actor(self.button3)
        self.button3.x = -100
        self.button3.y = -110
        self.button3.z_index = 4
        self.button3.set_on_mouse_down_listener(self.katt3)
        self.button4=nap()
        self.add_actor(self.button4)
        self.button4.x = -50
        self.button4.y = -110
        self.button4.z_index = 4
        self.button4.set_on_mouse_down_listener(self.katt4)

    def katt1(self, sender, event):
        if event.button==1:
            self.screen.game.set_screen(rainscreen())

    def katt2(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(havasesoscreen())

    def katt3(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(sunnyscreen())

    def katt4(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(snowscreen())



    def nyom1(self, sender, event):
        if event.key==pygame.K_ESCAPE:
            quit()


class rainstage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.rain=rain()
        self.rain.z_index = 4
        self.rain.x=850
        self.rain.y=-130
        self.add_actor(self.rain)
        self.landscape=landscape()
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
        self.felhocske.x =1070
        self.felhocske.y =-20
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x =850
        self.felhocske.y =70
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x =610
        self.felhocske.y =70
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x =190
        self.felhocske.y =-20
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x = -10
        self.felhocske.y = -20
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x = 410
        self.felhocske.y = 70
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x = 190
        self.felhocske.y = 70
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x = -10
        self.felhocske.y = 70
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x = 1070
        self.felhocske.y = 70
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)

        for i in range(35):
            self.rain = rain()
            self.rain.width = 70
            self.rain.height = 70
            self.add_actor(self.rain)
            self.rain.x = random.Random().randint(0, 1280)
            self.rain.y = random.Random().randint(0, 720)

class snowstage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.snow=snow()
        self.snow.x=850
        self.snow.y=-130
        self.add_actor(self.snow)
        self.landscape=landscape()
        self.landscape.z_index = 2
        self.add_actor(self.landscape)
        self.cloudy=cloudy()
        self.cloudy.z_index = 1
        self.add_actor(self.cloudy)
        self.snow.z_index = 3
        for i in range(50):
            self.snow=snow()
            self.snow.width=70
            self.snow.height=70
            self.add_actor(self.snow)
            self.snow.x=random.Random().randint(0,1280)
            self.snow.y=random.Random().randint(0,720)
        self.felhocske = felhocske()
        self.felhocske.x = 850
        self.felhocske.y = -20
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x = 630
        self.felhocske.y = -20
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x = 410
        self.felhocske.y = -20
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x = 1070
        self.felhocske.y = -20
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)


class sunnystage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.sunny=sunny()
        self.sunny.x = 0
        self.sunny.y = 0
        self.add_actor(self.sunny)
        self.landscape=landscape()
        self.add_actor(self.landscape)
        self.sun=nap()
        self.sun.x = 850
        self.sun.y = -95
        self.add_actor(self.sun)
        self.sunny.z_index = 4



class havasesostage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.cloudy=cloudy()
        self.cloudy.x=0
        self.cloudy.y=0
        self.add_actor(self.cloudy)
        self.landscape=landscape()
        self.add_actor(self.landscape)
        self.felhocske = felhocske()
        self.felhocske.x = 850
        self.felhocske.y = -20
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x = 630
        self.felhocske.y = -20
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x = 410
        self.felhocske.y = -20
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x = 1070
        self.felhocske.y = -20
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x = 850
        self.felhocske.y = 70
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x = 610
        self.felhocske.y = 70
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x = 190
        self.felhocske.y = -20
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x = -10
        self.felhocske.y = -20
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x = 410
        self.felhocske.y = 70
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x = 190
        self.felhocske.y = 70
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x = -10
        self.felhocske.y = 70
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        self.felhocske = felhocske()
        self.felhocske.x = 1070
        self.felhocske.y = 70
        self.felhocske.z_index = 2
        self.add_actor(self.felhocske)
        for i in range(50):
            self.snow=snow()
            self.snow.width=70
            self.snow.height=70
            self.add_actor(self.snow)
            self.snow.x=random.Random().randint(0,1280)
            self.snow.y=random.Random().randint(0,720)

        for i in range(60):
            self.rain=rain()
            self.rain.width=40
            self.rain.height = 40
            self.add_actor(self.rain)
            self.rain.x = random.Random().randint(0, 1280)
            self.rain.y = random.Random().randint(0, 720)


class menuscreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0)
        self.add_stage(menustage())

class rainscreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0)
        self.add_stage(rainstage())

class snowscreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0)
        self.add_stage(snowstage())


class sunnyscreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0)
        self.add_stage(sunnystage())


class havasesoscreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(0, 0, 0)
        self.add_stage(havasesostage())

class Program(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = havasesoscreen()


Program().run()





