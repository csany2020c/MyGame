import game
import pygame

class Start(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("Res/sun.png")
        self.set_on_key_down_listener(self.key_down)
        self.set_on_mouse_down_listener(self.mouse_down)

    def key_down(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()

    def mouse_down(self, sender, event):
        print("start")


