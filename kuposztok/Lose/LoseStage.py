import game
import pygame

import kuposztok.CaraValt.CaraValtScreen
from kuposztok.Lose.LoseActors import *
import kuposztok.CaraValt.CaraValtScreen


class LoseStage(game.scene2d.MyStage):
    def __init__(self, score: int, maxScore: int):
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
        self.score = score
        self.maxScore = maxScore
        self.maxsclabel = game.scene2d.MyLabel("Az eddigi legtöbbet elért pontszámod:" + str(self.maxScore))
        self.maxsclabel.x = self.width / 14
        self.maxsclabel.y = self.height / 2
        self.maxsclabel.set_color(0, 0, 0)
        self.add_actor(self.maxsclabel)
        self.newlabel = game.scene2d.MyLabel("Gratulálok több pontot értél el mint legutóbb.")
        self.newlabel.x = self.width / 14
        self.newlabel.y = self.height / 1.5
        self.newlabel.set_color(0, 0, 0)
        if int(self.score) > int(self.maxScore):
            self.add_actor(self.newlabel)

        self.button1.set_on_mouse_down_listener(self.Klikk1)
    #
    def Klikk1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.CaraValt.CaraValtScreen.CaraValtScreen())

    def act(self, delta_time: float):
        super().act(delta_time)
        self.maxsclabel.set_text("Az eddigi legjobb pontszámod:" + str(self.maxScore))

