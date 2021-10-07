import game
import pygame
import random


class ActorA(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("cloudy.png")


class ActorB(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("landscape.png")


class ActorC(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("snow.png")
        self.set_width(70)
        self.set_height(70)

    def act(self, delta_time: float):
        game.scene2d.MyLabel.act(self, delta_time)
        if self.x + self.width < game.scene2d.MyGame.get_screen_width():
            self.x += delta_time * 20
            self.rotate_with(delta_time * 20)


class Stage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.a = ActorA()
        self.b = ActorB()
        self.c = ActorC()
        self.add_actor(self.a)
        self.add_actor(self.b)
        self.add_actor(self.c)
        self.set_on_key_down_listener(self.key_down)

    def key_down(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()


class HavazosScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(Stage())


class Start(game.scene2d.MyGame):
    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False):
        super().__init__(width, height, autorun)
        self.screen = HavazosScreen()


Start().run()
