import pygame

from Kancsalmate27megilyenek.MenuActor import *
from Kancsalmate27megilyenek.InGameScreen import *
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
        self.a.set_on_mouse_down_listener(self.exit)

        self.b = MenuActor2()
        self.b.set_size(self.width * 0.313, self.height * 0.1)
        self.b.x = self.width - self.width / 2 - self.b.width / 2
        self.b.y = (self.height - self.height * 0.75) - self.b.height / 2
        self.add_actor(self.b)
        self.b.set_on_mouse_down_listener(self.start)

        self.c = MenuActor3()
        self.c.set_size(self.width * 0.313, self.height * 0.1)
        self.c.x = self.width - self.width / 2 - self.c.width / 2
        self.c.y = (self.height - self.height * 0.60 - self.c.height / 2)
        self.add_actor(self.c)

        self.d = MenuActor4()
        self.d.set_size(self.width * 0.313, self.height * 0.1)
        self.d.x = self.width - self.width / 2 - self.d.width / 2
        self.d.y = (self.height - self.height * 0.35 - self.d.height / 2)
        self.add_actor(self.d)



    def exit(self, sender, event):
        print(event)
        if event.button == 1:
            quit()

    def start(self,sender,event):
        if event.button == 1:
            self.screen.game.set_screen(InScreen())




