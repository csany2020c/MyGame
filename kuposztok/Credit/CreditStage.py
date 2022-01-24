import kuposztok.Credit.CreditScreen
import pygame
from kuposztok.Credit.CreditActors import *



class CreditStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        creditact = Creditlist()
        self.add_actor(creditact)
        creditact.width = self.width
        creditact.height = self.height
        pygame.mixer.init()
        pygame.mixer.music.load("../kuposztok/music/creditmusica.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
        self.button1 = Visszagomb()
        self.add_actor(self.button1)
        self.button1.width = 125
        self.button1.height = 75
        self.button1.y = self.height - 80
        self.button1.x = self.width - self.button1.get_width()

        self.button1.set_on_mouse_down_listener(self.Klikk1)
        self.set_on_key_down_listener(self.Escape)

    def Klikk1(self, sender, event):
        if event.button == 1:
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())

    def Escape(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            self.screen.game.set_screen(kuposztok.Menu.MenuScreen.MenuScreen())


