from Weathersim.zsebokdavidf.MainStage import *
from Weathersim.zsebokdavidf.RainStage import *
from Weathersim.zsebokdavidf.SnowStage import *
from Weathersim.zsebokdavidf.DayNightStage import *


class MainScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(r=0, b=50, g=0)
        """self.add_stage(MainStage())"""
        self.add_stage(DayNightStage())
        self.add_stage(SnowStage())
        """self.add_stage(RainStage())"""
        self.set_on_key_down_listener(func=self.OnKeys)

    def OnKeys(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()
        if event.key == pygame.K_t:
            print('asd')
        if event.key == pygame.K_KP1:
            print('NUM1')
        if event.key == pygame.K_KP2:
            print('NUM2')
        if event.key == pygame.K_KP3:
            print('NUM3')
        if event.key == pygame.K_KP4:
            print('NUM4')






