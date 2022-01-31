import game
import pygame


class DevActor(game.scene2d.MyActor):
    def __init__(self, image_url: str = "devs.png"):
        super().__init__(image_url)
        self.set_size(400, 200)