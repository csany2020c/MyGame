from Weathersim.HorvathMark.Actors import *

class Sunnystage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.sun = Sunactor()
        self.bg = Background()
        self.sky = Sunnysky()
        #self.add_actor(self.sky)
        self.add_actor(self.sun)
        self.add_actor(self.bg)
        self.sun.x = 800
        self.sun.y = 200
        self.sun.w = 600

