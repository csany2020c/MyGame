import game
from Weathersim.faterlaszlo.f_actors import *

class f_stage1(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.bg = bg_actor()
        self.sun = napocska()
        self.eg = eg_actor()
        self.add_actor(self.bg)
        self.add_actor(self.sun)
        self.add_actor(self.eg)
        #ezt nem szabad igy hagyni
        #self.set_on_key_down_listener(self.key_down)
        self.sun.x = 50
        self.sun.y = 80
        self.sun.w = 350
        self.eg.z_index = 0
        self.sun.z_index = 2
