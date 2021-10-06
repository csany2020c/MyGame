from Weathersim.zsebokdavidf.MainActors import *


class DayNightStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.sunny = Sunny()
        self.sunny.height = 720
        self.sunny.width = 1280
        self.add_actor(actor=self.sunny)
        self.sunny.alpha = 255

    def act(self, delta_time: float):
        self.sunny.alpha = self.sunny.alpha - 1