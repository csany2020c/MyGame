import game
import pygame
from Impostorsus.Game.WarioActor import *

class WarioStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.wario = Wario4Actor()
        self.add_actor(self.wario)
        self.wario.set_on_key_press_listener(self.press)
        self.set_on_key_down_listener(self.key_down)

    def press(self, sender, event):
        # print(event.key)
        if event.key == pygame.K_d:
            sender.x += 10
        if event.key == pygame.K_a:
            sender.x -= 10
        if event.key == pygame.K_w:
            sender.y -= 10
        if event.key == pygame.K_s:
            sender.y += 10

    def interval(self, sender):
        self.wario.x += 100 * self.get_delta_time()
        pass


    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_ESCAPE:
            print("'QUIT'")
            quit()
