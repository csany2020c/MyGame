from HawkProductions.Font import *
import pygame

class OverStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        pygame.mixer.init()
        pygame.mixer.music.load("../HawkProductions/Music/Over.wav")
        pygame.mixer.music.play(-1)
        self.F = Arial()
        self.add_actor(self.F)
        self.F.set_text("Game Over")
        self.F.set_color(204, 0, 0)
