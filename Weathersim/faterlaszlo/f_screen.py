import game
from Weathersim.faterlaszlo.f_stage import *

class f_screen_m(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.set_background_color(20, 120, 100)
        self.add_stage(f_stage_m())

#class f_screen_1(game.scene2d.MyScreen):
        #  def __init__(self):
        # super().__init__()
        #self.add_stage(f_stage1())

    #class f_screen_m(game.scene2d.MyScreen):
        # def __init__(self):
        # super().__init__()
        #self.set_background_color(20, 120, 100)
        #self.add_stage(f_stage_m())
