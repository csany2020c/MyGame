import game
import pygame
from yetigamescreen import *


class BG(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/desertbig.png")

class Start(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/start.png")

        self.set_on_mouse_down_listener(self.mouse_down)

    def mouse_down(self, sender, event):
        self.stage.screen.game.set_screen(GameScreen())

class Exit(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/exit.png")

        self.set_on_mouse_down_listener(self.mouse_down2)

    def mouse_down2(self, sender, event):
        quit()


class Settings(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Images/options.png")

        self.set_on_mouse_down_listener(self.mouse_down)
        self.set_on_key_down_listener(self.key_down)


    def mouse_down(self, sender, event):
        self.stage.screen.game.set_screen(Settingscreen())

    def key_down(self, sender, event):
        if event.key == pygame.K_F11:
            pygame.display.toggle_fullscreen()
