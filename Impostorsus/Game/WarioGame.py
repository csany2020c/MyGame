import game
import pygame
from Impostorsus.Game.WarioActor import *
from Impostorsus.Game.WarioScr import *
import Impostorsus.Game.WarioScr


class Wario(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False):
        super().__init__(width, height, autorun, autosize)
        self.screen = MenuScreen()
        self.set_on_key_down_listener(self.key_down)
        pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
        clock = pygame.time.Clock()
        pygame.display.set_caption('SUPER WARIO')
        T = pygame.image.load('Kepek/Tabla.png')
        pygame.display.set_icon(T)

    def key_down(self, sender, event):
        monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        print(sender)
        print(event)
        if event.key == pygame.K_r:
            self.screen.game.set_screen(Impostorsus.Game.WarioScr.WarioScr())
        if event.key == pygame.K_BACKSPACE:
            self.screen.game.set_screen(Impostorsus.Game.WarioScr.MenuScreen())
        if event.key == pygame.K_F11:
            pygame.display.toggle_fullscreen()
        if event.key == pygame.K_ESCAPE:
            quit()




Wario().run()



