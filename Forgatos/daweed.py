import game


class KocsiActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("car.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 50

class KocsiActor2(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("car.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 200


class TestStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()

        kocsi1 = KocsiActor()
        kocsi2 = KocsiActor2()
        kocsi1.x = 400
        self.add_actor(kocsi1)
        self.add_actor(kocsi2)


class TestScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(TestStage())


class Test(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen = TestScreen()


Test().run()

