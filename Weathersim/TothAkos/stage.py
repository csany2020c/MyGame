from Weathersim.TothAkos.actor import *

class Sunnystage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.b = Sun()
        self.add_actor(Sunny())
        self.add_actor(Landscape())
        self.Sun = Sun()
        self.add_actor(self.Sun)

class Snowystage (game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.b = Snow
        self.add_actor(cloudy)
        self.add_actor(Landscape)
        self.Snow = Snow()
        self.add_actor(self.Snow)