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
        self.set_width(30)
        self.set_height(30)

    def act(self, delta_time: float):
        game.scene2d.MyLabel.act(self, delta_time)
        if self.x + self.width < game.scene2d.MyGame.get_screen_width():
            self.y += delta_time * 80
            self.rotate_with(delta_time * 20)


class ActorD(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("rain.png")
        self.set_width(30)
        self.set_height(30)

    def act(self, delta_time: float):
        game.scene2d.MyLabel.act(self, delta_time)
        if self.x + self.width < game.scene2d.MyGame.get_screen_width():
            self.y += delta_time * 100


class ActorE(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("felho2.png")
        self.set_width(800)


class ActorF(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("szamok.jpg")
        self.set_width(220)


class ActorG(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("esc.jpg")
        self.set_width(180)


class Stage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.a = ActorA()
        self.b = ActorB()
        self.c = ActorC()
        self.d = ActorD()
        self.e = ActorE()
        self.f = ActorF()
        self.g = ActorG()
        self.e.set_x(525).set_y(-150)
        self.g.set_x(1100).set_y(0)
        self.add_actor(self.a)
        self.add_actor(self.b)
        self.add_actor(self.c)
        self.add_actor(self.d)
        self.add_actor(self.e)
        self.add_actor(self.f)
        self.add_actor(self.g)

        self.set_on_key_down_listener(self.key_down)

        for i in range(700):
            self.c = ActorC()
            self.add_actor(self.c)
            self.c.x = random.Random().randint(0, 1225)
            self.c.y = random.Random().randint(-3000, 750)

        for i in range(1000):
            self.d = ActorD()
            self.add_actor(self.d)
            self.d.x = random.Random().randint(0, 1225)
            self.d.y = random.Random().randint(-3000, 750)

    def key_down(self, sender, event):
        if event.key == pygame.K_ESCAPE:
            quit()


class HavasesosScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.add_stage(Stage())

