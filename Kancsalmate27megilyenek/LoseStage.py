import game
import pygame

import Kancsalmate27megilyenek.InGameScreen
from Kancsalmate27megilyenek.LoseScreen import *
from game.scene2d import MyLabel
from game.scene2d import MyTickTimer,MyOneTickTimer


class LoseStage(game.scene2d.MyStage):
    def __init__(self,mLevel:int,pLevel:int):
        super().__init__()
        pygame.init()
        self.width = pygame.display.get_surface().get_width()
        self.height = pygame.display.get_surface().get_height()
        self.loseLabel = MyLabel("Vesztettél","system",128,[168,0,0])
        self.loseLabel.set_position(self.width/2 - self.loseLabel.get_width()/2,128)
        self.add_actor(self.loseLabel)

        self.lostLvl = MyLabel("","system",64)
        self.lostLvl.set_text("Ezt a szintet nem tudtad teljesíteni: " + str(mLevel) + "  Játékos szinted: " + str(round(pLevel,2)))
        self.lostLvl.set_position(self.width/2 - self.lostLvl.get_width()/2,128+self.loseLabel.get_height() + 35)
        self.add_actor(self.lostLvl)

        self.timer = MyOneTickTimer(func=self.timeHandle,interval=5)
        self.add_timer(self.timer)

    def timeHandle(self,sender):
        self.screen.game.set_screen(Kancsalmate27megilyenek.InGameScreen.InScreen())


