from HawkProductions.Font import *
import game
import pygame


class IStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.H = Helvetica()
        self.add_actor(self.H)
        self.H.set_text("Lacika")
