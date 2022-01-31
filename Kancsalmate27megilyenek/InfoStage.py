
import game
import pygame
from Kancsalmate27megilyenek.InfoScreen import *
from Kancsalmate27megilyenek.DevActor import *
import Kancsalmate27megilyenek.MenuScreen
class InfoStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.info = pygame.display.Info()
        self.width = self.info.current_w
        self.height = self.info.current_h
        pygame.init()
        Dev = DevActor()
        self.add_actor(Dev)
        Dev.set_position(self.width/2 -Dev.get_width()/2,100)
        self.set_on_key_down_listener(self.back)


    def back(self,sender,event):
        if event.key == pygame.K_ESCAPE:
            self.screen.game.set_screen(Kancsalmate27megilyenek.MenuScreen.MenuScreen3())
