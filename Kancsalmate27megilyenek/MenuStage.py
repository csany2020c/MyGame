import pygame

from Kancsalmate27megilyenek.MenuActor import *
import game


class Stage3(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        pygame.init()
        self.info = pygame.display.Info()
        self.width = self.info.current_w
        self.height = self.info.current_h
        self.a = MenuActor1()
        self.a.set_size(self.width * 0.313, self.height * 0.1)
        self.a.x = self.width - self.width / 2 - self.a.width / 2
        self.a.y = (self.height - self.height * 0.2) - self.a.height/2
        self.add_actor(self.a)
        self.a.set_on_mouse_down_listener(game.scene2d.MyGame.exit(game))

        self.b = MenuActor2()
        self.b.set_size(self.width * 0.313, self.height * 0.1)
        self.b.x = self.width - self.width / 2 - self.b.width / 2
        self.b.y = (self.height - self.height * 0.75) - self.b.height / 2
        self.add_actor(self.b)

