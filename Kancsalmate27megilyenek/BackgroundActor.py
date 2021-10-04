import game
import pygame
class BackgroundActor(game.scene2d.MyActor):
    def __init__(self, image_url: str = "background.png"):
        super().__init__(image_url)
        pygame.init()
        self.info = pygame.display.Info()
        self.width = self.info.current_w
        self.height = self.info.current_h
        self.set_size(1920, 1080)

