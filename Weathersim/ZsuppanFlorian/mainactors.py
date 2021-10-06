import game
import random


#class taj(game.scene2d.MyActor):
    #def __init__(self):
        #self.map = super().__init__('resource/images/landscape.png')

class taj(game.scene2d.MyActor):
    def __init__(self, image_url: str = "resource/images/landscape.png"):
        super().__init__(image_url)

class eg(game.scene2d.MyActor):
    def __init__(self, image_url: str = "resource/images/cloudy.png"):
        super().__init__(image_url)


class eso(game.scene2d.MyActor):
    def __init__(self, image_url: str = "resource/images/rain.png"):
        super().__init__(image_url)

    def act(self, delta_time: float):
        super().act(delta_time)


class ho(game.scene2d.MyActor):
    def __init__(self, image_url: str = "resource/images/snow.png"):
        super().__init__(image_url)

    def act(self, delta_time: float):
        super().act(delta_time)


class nap(game.scene2d.MyActor):
    def __init__(self, image_url: str = "resource/images/sun.png"):
        super().__init__(image_url)

    def act(self, delta_time: float):
        super().act(delta_time)