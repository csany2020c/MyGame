
import game
import pygame
from Kancsalmate27megilyenek.LoseScreen import *

class WinStage(game.scene2d.MyStage):
    def __init__(self,mLvl:int,pLvl:int):
        super().__init__()
        pygame.init()
        self.width = pygame.display.get_surface().get_width()
        self.height = pygame.display.get_surface().get_height()
        self.loseLabel = MyLabel("Nyertél", "system", 128, [0, 0, 168])
        self.loseLabel.set_position(self.width / 2 - self.loseLabel.get_width() / 2, 128)
        self.add_actor(self.loseLabel)

        self.lostLvl = MyLabel("", "system", 64)
        self.lostLvl.set_text("Sikeresen teljesítetted ezt a szintet: " + str(mLvl) + "  Játékos szinted: " + str(round(pLvl,2)))
        self.lostLvl.set_position(self.width / 2 - self.lostLvl.get_width() / 2, 128 + self.loseLabel.get_height() + 35)
        self.add_actor(self.lostLvl)

        self.timer = MyOneTickTimer(func=self.timeHandle, interval=5)
        self.add_timer(self.timer)

    def timeHandle(self, sender):
        self.screen.game.set_screen(Kancsalmate27megilyenek.InGameScreen.InScreen())

