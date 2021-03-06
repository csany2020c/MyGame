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
        pygame.display.set_caption('KUNU WARIO')
        T = pygame.image.load('Kepek/Tabla.png')
        pygame.display.set_icon(T)
        pygame.display.toggle_fullscreen()

    def key_down(self, sender, event):
        monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
        self.height = pygame.display.get_surface().get_height()
        self.width = pygame.display.get_surface().get_width()
        print(sender)
        print(event)
        if event.key == pygame.K_BACKSPACE:
            self.screen.game.set_screen(Impostorsus.Game.WarioScr.MenuScreen())
        if event.key == pygame.K_F11:
            pygame.display.toggle_fullscreen()
        if event.key == pygame.K_ESCAPE:
            quit()
        if event.key == pygame.K_LCTRL:
            pygame.mixer.music.load('audio/rajosan.mp3')
            pygame.mixer.music.stop()
            pygame.mixer.music.load('audio/spartai.mp3')
            pygame.mixer.music.stop()
        if event.key == pygame.K_RCTRL:
            pygame.mixer.music.load('audio/rajosan.mp3')
            pygame.mixer.music.stop()
            pygame.mixer.music.load('audio/spartai.mp3')
            pygame.mixer.music.stop()




Wario().run()



