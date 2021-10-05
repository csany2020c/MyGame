import game
import pygame
from Weathersim.zsebokdavidf.MainActors import *


class MainStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.add_actor(actor=Background())
        self.set_on_key_down_listener(self.OnKeys)

    def OnKeys(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()
        if event.key == pygame.K_t:
            print('asd')
        if event.key == pygame.K_KP1:
            print('NUM1')
            actor = SnowyGround()
            actor.height = 720
            actor.width = 1280
            actor.y = 0
            self.add_actor(actor)

        if event.key == pygame.K_KP2:
            print('NUM2')
            actor = Ice()
            actor.height = 720
            actor.width = 1280
            self.add_actor(actor)
        if event.key == pygame.K_KP3:
            print('NUM3')
        if event.key == pygame.K_KP4:
            print('NUM4')




