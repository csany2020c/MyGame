import game
import pygame

import kuposztok.CaraValt.CaraValtScreen
from kuposztok.Lose.LoseActors import *
import kuposztok.CaraValt.CaraValtScreen
import kuposztok.Menu.MenuScreen


class LoseStage(game.scene2d.MyStage):

    def filebaolvasas(self):
        with open('../kuposztok/Save/file.txt', 'r') as file:
            self.max_scoreno = int(file.readline())
            self.money = int(file.readline())
            file.close()

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
        self.button1.x = self.width / 2 + self.button1.get_width() / 2
        self.button1.y = self.height / 2 - self.button1.get_height() * 2
        self.add_actor(self.button1)
        self.score = score
        self.maxScore = maxScore
        self.maxsclabel = game.scene2d.MyLabel("Az eddigi legtöbbet elért pontszámod:" + str(self.maxScore))
        self.maxsclabel.x = self.width / 14
        self.maxsclabel.y = self.height / 2
        self.maxsclabel.set_color(0, 0, 0)
        self.add_actor(self.maxsclabel)
        self.menub = Menub()
        self.menub.x = self.width - self.menub.get_width()
        self.menub.y = self.height - self.menub.get_height()
        self.add_actor(self.menub)

        self.button1.set_on_mouse_down_listener(self.Klikk1)
        self.menub.set_on_mouse_down_listener(self.katt)

    def Klikk1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.CaraValt.CaraValtScreen.CaraValtScreen(money=self.money, maxScore=self.maxScore))

    def filebairas(self):
        with open('../kuposztok/Save/file.txt', 'w') as file:
            if int(self.max_scoreno) < int(self.score):
                file.write(str(self.score))
            else:
                file.write(str(self.max_scoreno))
            file.write("\n" + str(self.money))
            file.close()

    def act(self, delta_time: float):
        super().act(delta_time)
        self.filebaolvasas()
        self.filebairas()
        self.maxsclabel.set_text("Az eddigi legjobb pontszámod:" + str(self.max_scoreno))

    def katt(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())