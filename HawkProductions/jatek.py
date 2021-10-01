import game


class Deagle(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("image/bid2.png")

    def act(self, delta_time: float):
        self.y += 75*delta_time


class Pile1(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/oszlop-f.png")

    def act(self, delta_time: float):
        self.x -= 75 * delta_time


class Pile2(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("image/oszlop-a.png")

    def act(self, delta_time: float):
        self.x -= 75*delta_time


class Stage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.D = Deagle()
        self.add_actor(self.D)
        self.D.y = 250
        self.D.x = 50
        self.D.width = 100
        self.set_on_mouse_down_listener(self.click)

        self.P1 = Pile1()
        self.add_actor(self.P1)
        self.P1.set_x(250)
        self.P1.set_y(300)
        self.P1.set_hitbox_scale_h(0.35)
        self.P1.set_hitbox_scale_w(0.2)

        self.P2 = Pile2()
        self.add_actor(self.P2)
        self.P2.set_x(250)
        self.P2.set_y(1)
        self.P2.set_hitbox_scale_h(0.35)
        self.P2.set_hitbox_scale_w(0.2)

    def click(self, sender, event):
        print(event)
        self.D.y -= 50

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.P1.overlaps(self.D):
            self.screen.b = 80
        else:
            self.screen.b = 0


class Screen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.r = 200
        self.g = 10
        self.b = 25
        self.add_stage(Stage())


class Game(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen = Screen()


Game().run()
