import game
from yetiactor import*
import pygame

class MenuStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()

        self.bg = BG()
        self.exit = Exit()
        self.add_actor(self.exit)
        #self.settings = Settings()
        #self.add_actor(self.settings)
        self.bg.y = 1280
        self.add_actor(self.bg)
        self.start = Start()
        self.start.x = 590
        self.start.y = 1200

        self.exit.x = 590
        self.exit.y = 1200

        self.start.width = 200
        self.add_actor(self.start)

    def act(self, delta_time: float):
        if self.bg.y > 0:
            self.bg.y = self.bg.y - 9
        if self.start.y > 200:
            self.start.y = self.start.y - 9


