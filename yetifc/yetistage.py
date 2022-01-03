import game
from yetiactor import*
import pygame

class MenuStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()

        self.bg = BG()
        self.exit = Exit()
        self.add_actor(self.exit)
        self.settings = Settings()
        self.bg.y = 1280
        self.bg.z_index = 0
        self.add_actor(self.bg)
        self.start = Start()
        self.start.x = 590
        self.start.y = 1200

        self.exit.x = 590
        self.exit.y = 1200

        self.start.z_index = 1
        self.start.width = 200
        self.add_actor(self.start)

        self.settings.width = 200
        self.settings.x = 600
        self.settings.y = 900
        self.settings.z_index = 2
        self.add_actor(self.settings)

        self.exit.width = 300
        self.exit.x = 550
        self.exit.y = 900

    def act(self, delta_time: float):
        if self.bg.y > 0:
            self.bg.y = self.bg.y - 15
        if self.start.y > 200:
            self.start.y = self.start.y - 13
        if self.settings.y > 360:
            self.settings.y = self.settings.y - 10
        if self.exit.y > 500:
            self.exit.y = self.exit.y - 8



