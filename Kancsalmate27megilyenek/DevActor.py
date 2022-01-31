import game
import pygame


class DevActor(game.scene2d.MyActor):
    def __init__(self, image_url: str = "devs.png"):
        super().__init__(image_url)
        self.info = pygame.display.Info()
        self.width = self.info.current_w
        self.height = self.info.current_h
        self.set_size(400, 200)