import game
from yetiactor import*
import pygame

class MenuStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        pygame.mixer.music.load("Images/cowboymusic.wav")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(1)
        self.bg = BG()
        self.bg.y = 1280
        self.add_actor(self.bg)
        self.start = Start()
        self.start.x = 590
        self.start.y = 1500

        self.start.width = 200
        self.add_actor(self.start)

    def act(self, delta_time: float):
        if self.bg.y > 0:
            self.bg.y = self.bg.y - 4
        if self.start.y > 300:
            self.start.y = self.start.y - 4



