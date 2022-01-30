import kuposztok.Credit.CreditScreen
import pygame
from kuposztok.Credit.CreditActors import *



class CreditStage(game.scene2d.MyStage):

    def soundvaltread(self):
        with open('../kuposztok/Save/options.txt', 'r') as beskinfile1:
            self.soundvaltbe = int(beskinfile1.readline())
            self.musica = int(beskinfile1.readline())
            beskinfile1.close()

    def __init__(self):
        super().__init__()
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        self.soundvaltread()
        creditact = Creditlist()
        self.add_actor(creditact)
        self.soundvalt = self.soundvaltbe
        creditact.width = self.width
        creditact.height = self.height
        pygame.mixer.init()
        pygame.mixer.music.load("../kuposztok/music/creditmusica.wav")
        pygame.mixer.music.play(-1)
        if self.soundvalt == 0 or self.soundvalt == 1:
            pygame.mixer.music.set_volume(0.5)
        if self.soundvalt == 2:
            pygame.mixer.music.set_volume(0.20)
        if self.soundvalt == 3:
            pygame.mixer.music.set_volume(0.07)
        if self.soundvalt == 4:
            pygame.mixer.music.stop()
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


