import game
import pygame
from Impostorsus.Game.WarioActor import *

class WarioStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.wario = WarioActor()
        self.wario2 = WarioActor()
        self.add_actor(self.wario)
        self.add_actor(self.wario2)
        self.fold = GroundActor()
        self.add_actor(self.fold)
        self.fold2 = GroundActor()
        self.add_actor(self.fold2)
        self.fold2.x += 200
        self.fold2.y += 615
        self.fold.x += 350
        self.fold.y += 615
        self.wario.set_on_key_press_listener(self.press)
        self.wario.set_on_key_down_listener(self.key_down)

        for i in range(10):
            self.fold2 = GroundActor()
            self.add_actor(GroundActor())
            self.fold2.x += 100


    def press(self, sender, event):
        # print(event.key)
        if event.key == pygame.K_d:
            sender.x += 10
        if event.key == pygame.K_a:
            sender.x -= 10

    def interval(self, sender):
        self.wario.x += 100 * self.get_delta_time()
        pass


    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_w:
            print("'hoppáré'")
            self.wario.y -= 120
        if event.key == pygame.K_SPACE:
            print("'hoppáré'")
            self.wario.y -= 120


    def act(self, delta_time: float):
        super().act(delta_time)
        if self.wario.overlaps(self.fold or self.fold2):
            self.wario.stop()
        if self.wario.overlaps(self.fold or self.fold2) == False:
            self.wario.start()





