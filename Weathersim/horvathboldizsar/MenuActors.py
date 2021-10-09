import game
import random

class menubackground(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/menubackground.png')
        self.z_index = 1

class exitbutton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/exitbutton.png')
        self.z_index = 6

class naposbutton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/naposbutton.png')
        self.z_index = 6

class esosbutton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/esosbutton.png')
        self.z_index = 6

class havasbutton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/havasbutton.png')
        self.z_index = 6

class havasesobutton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/havasesobutton.png')
        self.z_index = 6

class havasesocseppmenube(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/rain.png')
        self.width = 30
        self.z_index = 2

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * random.randint(200, 400)
        if self.y > 720:
            self.y = random.randint(360, 500)

class menunap(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/sun.png')
        self.y = -220
        self.x = 1000
        self.z_index = 2

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(0.2)
