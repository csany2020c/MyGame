import game
from pygame import mixer
from random import Random
import Weathersim.FellnerMilan.Screen
from game.scene2d import MyOneTickTimer

class LandScape(game.scene2d.MyActor):
    def __init__(self, image_url: str = "../../!_resources/images/landscape.png"):
        super().__init__(image_url)

class Sunny(game.scene2d.MyActor):
    def __init__(self, image_url: str = "../../!_resources/images/sunny.png"):
        super().__init__(image_url)

class Sun(game.scene2d.MyActor):
    def __init__(self, image_url: str = "../../!_resources/images/sun.png"):
        super().__init__(image_url)

class Rain(game.scene2d.MyActor):

    def __init__(self, image_url: str = "../../!_resources/images/rain.png"):
        super().__init__(image_url)
        self.random = Random()
        self.set_size(25,25)
        self.x = self.random.randint(0,1280)

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y = self.y + 5


class Rainy(game.scene2d.MyActor):

    def __init__(self, image_url: str = "../../!_resources/images/cloudy.png"):
        super().__init__(image_url)

class Snow(game.scene2d.MyActor):

    def __init__(self, image_url: str = "../../!_resources/images/snow.png"):
        super().__init__(image_url)
        self.random = Random()
        self.set_size(25, 25)
        self.x = self.random.randint(0, 1280)

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y = self.y + 5

class Cloud(game.scene2d.MyActor):

    def __init__(self, image_url: str = "cloud.png"):
        super().__init__(image_url)
        self.set_size(240,130)

        self.random = Random()
        self.randomint = self.random.randint(1,5)

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x = self.x + self.randomint

        if self.x >= 1280:
            self.x = 0
            self.randomint = self.random.randint(0, 5)



class MainMenu(game.scene2d.MyActor):
    def __init__(self, image_url: str = "mainmenu.png"):
        super().__init__(image_url)
        self.width = 300
        self.x = 640 - self.width / 2
        self.y = 600
        self.hitbox_scale_h = 0.4
        self.hitbox_scale_w = 0.6
        self.set_on_mouse_down_listener(self.clickHandler)

    def clickHandler(self,sender,event):
        if event.button == 1:
            self.image_url = "mainmenuOnClick.png"
            self.t = MyOneTickTimer(interval=0.2, func=self.csereldle)
            self.add_timer(self.t)

    def csereldle(self,sender):
        self.stage.screen.game.set_screen(Weathersim.FellnerMilan.Screen.GameScreen())
        self.remove_timer(self.t)

class SnowyLandScape(game.scene2d.MyActor):
    def __init__(self, image_url: str = "snowylandscape.png"):
        super().__init__(image_url)

class SnowyRain(game.scene2d.MyActor):
    def __init__(self, image_url: str = "snowyrain.png"):
        super().__init__(image_url)
        self.random = Random()
        self.set_size(25, 25)
        self.x = self.random.randint(0, 1280)

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y = self.y + 5
class ArrowLeft(game.scene2d.MyActor):
    def __init__(self, image_url: str = "leftarrow.png"):
        super().__init__(image_url)
        self.set_size(250,125)
        self.x = 1280 - 640 - 125 - 300
        self.y = 525
        self.z_index = 100
        self.hitbox_scale_w = 0.7
        self.hitbox_scale_h = 0.8

class ArrowRight(game.scene2d.MyActor):
    def __init__(self, image_url: str = "arrowright.png"):
        super().__init__(image_url)
        self.set_size(250,125)
        self.x = 1280 - 640 - 125 + 300
        self.y = 525
        self.z_index = 100
        self.hitbox_scale_w = 0.7
        self.hitbox_scale_h = 0.8