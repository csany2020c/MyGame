import game
from game.simpleworld.ShapeType import ShapeType


class MenuLabel(game.scene2d.MyLabel):

    def __init__(self, string: str = "MyText", x: int = 0, y: int = 0):
        super().__init__(string, "Pinzelan-Regular.ttf", 48)
        self.x = x
        self.y = y


class ActorA(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("car.png")
        self.speed = 0
        self.hitbox_scale_h = 0.1
        self.hitbox_scale_w = 0.6
        self.hitbox_shape = ShapeType.Rectangle

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * self.speed


class Stage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.a = ActorA()
        self.b = ActorA()
        self.a.speed = 80
        self.b.speed = 20
        self.a.set_x(80).set_y(190)
        self.b.set_x(390).set_y(190)
        self.add_actor(self.a)
        self.add_actor(self.b)
        self.l = game.scene2d.MyLabel("The quick brown fox jumps over the lazy dog.", "Arial", 64)

        self.l.hitbox_scale_h = 0.8
        self.l.set_font_italic(True)
        self.add_actor(self.l)
        self.add_actor(MenuLabel("start", 30, 100))
        self.add_actor(MenuLabel("Quit", 30, 200))
        self.l.x = game.scene2d.MyGame.get_screen_width() / 2 - self.l.width / 2
        self.l.y = game.scene2d.MyGame.get_screen_height() / 2 - self.l.height / 2

    def show(self):
        super().show()

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.a.overlaps(self.b):
            self.screen.b = 80
        else:
            self.screen.b = 0


class Screen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(Stage())


class Start(game.scene2d.MyGame):
    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False):
        super().__init__(width, height, autorun)
        self.screen = Screen()


Start().run()