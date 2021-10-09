import game
import random

class erdo(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/landscape.png')
        self.z_index = 3

class naposeg(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/sunny.png')
        self.z_index = 1

class felhoseg(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/cloudy.png')
        self.z_index = 1

class esocsepp(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/rain.png')
        self.width = 30
        self.z_index = 4

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * random.randint(200, 400)
        if self.y > 720:
            self.y = random.randint(-500, 0)

class hopehely(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/snow.png')
        self.width = 30
        self.height = 30
        self.z_index = 5

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(2)
        self.y += delta_time * random.randint(90, 250)
        if self.y > 720:
            self.y = random.randint(-500, 0)


class nap(game.scene2d.MyActor):
    def __init__(self):
        self.map = super().__init__('!_resources/images/sun.png')
        self.x = -200
        self.y = 400
        self.z_index = 2

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(0.8)
        self.y -= delta_time * 50
        self.x += delta_time * 80
        if self.x > 1280:
            self.x = -200
            self.y = 400
            print("A nap felkel újra!")

