import game

class forgoactor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("car.png")
    def act(self, delta_time: float):
        self.r += delta_time * -100

class masikforgoactor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("car.png")
    def act(self, delta_time: float):
        self.r += delta_time * 100

class forgostage(game.scene2d.MyStage):

    def create(self):
        super().create()

        a = forgoactor()
        a.y = 200
        a.x = 1023
        self.add_actor(a)

        b = masikforgoactor()
        b.y = 200
        b.x = 0
        self.add_actor(b)

class forgoscreen(game.scene2d.MyScreen):

    def create(self):
        super().create()
        self.r = 0
        self.g = 0
        self.b = 0
        self.add_stage(forgostage())

class forgogame(game.scene2d.MyGame):

    def create(self):
        super().create()
        self.screen = forgoscreen()

forgogame().run()