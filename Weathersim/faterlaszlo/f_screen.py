import game
from Weathersim.faterlaszlo.f_stage import *

class f_screen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        #self.set_background_color(120, 100, 90)
        self.add_stage(f_stage4())


    def key_down(self, event, sender):
        print(sender)
        print(event)
        if event.key == pygame.K_s:
            print("Majd jó lesz")
            self.add_stage(f_stage1())
