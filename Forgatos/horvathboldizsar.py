import game

class forgoactor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("car.png")

    def act(self, delta_time: float):
        self.x += delta_time * -100
        self.y -= delta_time * +25

class masikforgoactor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("car.png")

    def act(self, delta_time: float):
        self.x += delta_time * -120

class forgostage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()

        a = forgoactor()
        a.y = 350
        a.x = 1023
        self.add_actor(a)

        b = masikforgoactor()
        b.y = 50
        b.x = 1023
        self.add_actor(b)

class forgoscreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.r = 0
        self.g = 0
        self.b = 0
        self.add_stage(forgostage())

class forgogame(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen = forgoscreen()

forgogame().run()