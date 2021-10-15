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
        self.set_width(50)
        self.set_height(50)

    def act(self, delta_time: float):
        game.scene2d.MyLabel.act(self, delta_time)
        if self.x + self.width < game.scene2d.MyGame.get_screen_width():
            self.y += delta_time * 20
            self.rotate_with(delta_time * 20)


class ActorD(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("felho2.png")
        self.set_width(800)


class Stage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.a = ActorA()
        self.b = ActorB()
        self.c = ActorC()
        self.d = ActorD()
        self.d.set_x(525).set_y(-150)
        self.add_actor(self.a)
        self.add_actor(self.b)
        self.add_actor(self.c)
        self.add_actor(self.d)
        self.set_on_key_down_listener(self.key_down)

        for i in range(500):
            self.snow = ActorC()
            self.add_actor(self.snow)
            self.snow.x = random.Random().randint(0, 1230)
            self.snow.y = random.Random().randint(-5000, 750)

    def key_down(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()


class HavazosScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(Stage())

