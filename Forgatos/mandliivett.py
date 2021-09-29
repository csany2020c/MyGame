import game


class MyActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("car.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 100
        self.game.screen = GameScreen()


class GameStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.b = MyActor()
        self.add_actor(self.b)
        self.b.y = 150


class GameScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.set_background_color(150, 70, 35)
        self.add_stage(GameStage())


class Forgato():
    def act(self, delta_time: float):
        super().act(delta_time)
        if self.x + self.width < self.screen_width:
            self.x += delta_time * 60
            self.rotate_with(delta_time * 40)


GameScreen()
