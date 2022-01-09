import game
import pygame
from kuposztok.Lose.LoseActors import *
import kuposztok.Game.CarOsszesStage


class LoseStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        carvaltstage = kuposztok.Game.CarOsszesStage.CarOsszesStage.getScore()
        self.bg = BgActor()
        self.add_actor(self.bg)
        self.vesztettellabel = game.scene2d.MyLabel("Sajnálom a játék végetért számodra, az elért pontszámod:" + str(carvaltstage))
        self.vesztettellabel.x = self.width / 18
        self.vesztettellabel.y = 200