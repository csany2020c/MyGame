import game
from Nike.NikeScreen import *
from Nike.NikeActor import *
import Nike.NikeScreen
import random
import pygame

class MenuStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.FatJordan = FatJordan()
        self.add_actor(FatJordan())
        self.text = MenuText()
        self.add_actor(self.text)
        self.text.set_text("Fat Jordan")
        self.text.set_alpha(500)
        self.text.set_width(80)
        self.text.set_height(80)
        self.text.x += 500
        self.text.y += 150