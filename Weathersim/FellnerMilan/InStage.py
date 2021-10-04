from Weathersim.FellnerMilan.Screen import *
from Weathersim.FellnerMilan.InActors import *
import game

class InStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.ls = LandScape()
        self.add_actor(self.ls)
        self.ls.z_index = 1

        self.sunny = Sunny()
        self.add_actor(self.sunny)
        self.sunny.z_index = 0

        self.sun = Sun()
        self.add_actor(self.sun)
        self.sun.z_index = 2
        self.sun.width = 400
        self.sun.x = 1280 - 250
        self.sun.y = 0 - 150

        self.backbutton = MainMenu()
        self.add_actor(self.backbutton)
        self.backbutton.set_on_mouse_down_listener(self.onClick)

    def act(self, delta_time: float):
        super().act(delta_time)
        self.sun.rotation = self.sun.rotation + 0.1


    def onClick(self,sender,event):
        if event.button == 1:
            quit()

