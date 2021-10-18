from Weathersim.zsebokdavidf.SunStage import *
from Weathersim.zsebokdavidf.RainStage import *
from Weathersim.zsebokdavidf.SnowStage import *
from Weathersim.zsebokdavidf.DayNightStage import *
from Weathersim.zsebokdavidf.BlizzardStage import *


class MainScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.set_background_color(r=0, b=50, g=0)
        self.add_stage(DayNightStage())
        self.snow = SnowStage()
        self.rain = RainStage()
        self.sun = SunStage()
        self.blizzard = BlizzardStage()
        self.snowOn = 0
        self.rainOn = 0
        self.sunOn = 1
        self.blizzardOn = 0
        self.add_stage(stage=self.sun)
        self.set_on_key_down_listener(func=self.OnKeys)

    def OnKeys(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()
        if event.key == pygame.K_t:
            print('asd')
        if event.key == pygame.K_KP1:
            if self.blizzardOn == 1:
                self.remove_stage(stage=self.blizzard)
                self.blizzardOn = 0
            if self.sunOn == 1:
                self.remove_stage(stage=self.sun)
                self.sunOn = 0
            if self.rainOn == 1:
                self.remove_stage(stage=self.rain)
                self.rainOn = 0
            if self.snowOn == 0:
                self.add_stage(stage=self.snow)
                self.snowOn = 1
        if event.key == pygame.K_KP2:
            if self.blizzardOn == 1:
                self.remove_stage(stage=self.blizzard)
                self.blizzardOn = 0
            if self.sunOn == 1:
                self.remove_stage(stage=self.sun)
                self.sunOn = 0
            if self.snowOn == 1:
                self.remove_stage(stage=self.snow)
                self.snowOn = 0
            if self.rainOn == 0:
                self.add_stage(stage=self.rain)
                self.rainOn = 1
        if event.key == pygame.K_KP3:
            if self.blizzardOn == 1:
                self.remove_stage(stage=self.blizzard)
                self.blizzardOn = 0
            if self.rainOn == 1:
                self.remove_stage(stage=self.rain)
                self.rainOn = 0
            if self.snowOn == 1:
                self.remove_stage(stage=self.snow)
                self.snowOn = 0
            if self.sunOn == 0:
                self.add_stage(stage=self.sun)
                self.sunOn = 1
        if event.key == pygame.K_KP4:
            if self.rainOn == 1:
                self.remove_stage(stage=self.rain)
                self.rainOn = 0
            if self.snowOn == 1:
                self.remove_stage(stage=self.snow)
                self.snowOn = 0
            if self.sunOn == 1:
                self.remove_stage(stage=self.sun)
                self.sunOn = 0
            if self.blizzardOn == 0:
                self.add_stage(stage=self.blizzard)
                self.blizzardOn = 1
