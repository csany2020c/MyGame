from Weathersim.zsebokdavidf.MainActors import *


class DayNightStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.sunny = Sunny()
        self.sunny.height = 720
        self.sunny.width = 1280
        self.add_actor(actor=self.sunny)
        self.sunny.alpha = 120
        self.upordown = 1

        self.sun = Sun()
        self.sun.width = 300
        self.sun.height = 300
        self.sun.x = -350
        self.sun.y = 600
        self.add_actor(actor=self.sun)
        self.sunway = 110

        self.moon = Moon()
        self.moon.width = 130
        self. moon.height = 130
        self.moon.x = -300
        self.moon.y = 600
        self.add_actor(actor=self.moon)
        self.moonway = 110

    def act(self, delta_time: float):
        if self.upordown == 0:
            self.sunny.alpha = self.sunny.alpha - delta_time * 12
        elif self.upordown == 1:
            self.sunny.alpha = self.sunny.alpha + delta_time * 12
        if self.sunny.alpha <= 0:
            self.upordown = 1
        elif self.sunny.alpha >= 255:
            self.upordown = 0

        self.sun.x = self.sun.x + delta_time * 80
        self.sun.y = self.sun.y - delta_time * self.sunway
        self.sunway = self.sunway - delta_time * 10

        if self.sunny.alpha < 120:
            self.sun.x = -350
            self.sun.y = 600
            self.sunway = 110

        self.moon.x = self.moon.x + delta_time * 80
        self.moon.y = self.moon.y - delta_time * self.moonway
        self.moonway = self.moonway - delta_time * 10

        if self.sunny.alpha > 140:
            self.moon.x = -400
            self.moon.y = 600
            self.moonway = 110
