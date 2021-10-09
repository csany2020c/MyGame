import game
import random

class menubackground(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/menubackground.png')

class exitbutton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/exitbutton.png')

class naposbutton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/naposbutton.png')

class esosbutton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/esosbutton.png')

class havasbutton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/havasbutton.png')

class havasesobutton(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/havasesobutton.png')

class havasesocseppmenube(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/rain.png')

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
    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(0.2)
