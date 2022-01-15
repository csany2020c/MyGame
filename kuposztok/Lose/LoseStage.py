import game
import pygame

import kuposztok.Game.CarOsszesScreen
from kuposztok.CaraValt.CaraValtScreen import *
from kuposztok.Lose.LoseActors import *


class LoseStage(game.scene2d.MyStage):
    def __init__(self, score: int, carvalt: int, maxScore: int):
        super().__init__()
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        print(score)
        self.bg = BgActor()
        self.add_actor(self.bg)
        self.vesztettellabel = game.scene2d.MyLabel("Sajnálom a játék végetért számodra, az elért pontszámod:" + str(score))
        self.vesztettellabel.x = self.width / 18
        self.vesztettellabel.y = 200
        self.vesztettellabel.set_color(0, 0, 0)
        self.add_actor(self.vesztettellabel)
        self.button1 = NewGame()
        self.add_actor(self.button1)
        self.carvalt = carvalt

        self.button1.set_on_mouse_down_listener(self.Klikk1)
    #
    def Klikk1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Game.CarOsszesScreen.CarOsszesScreen(carvalt=self.carvalt))