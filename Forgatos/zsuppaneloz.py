import game

class Car(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("car.png")
        self.speed= 0

    def act(self, delta_time: float):
        super().act(delta_time)




class Stage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.A = Car()
        self.A2 = Car()
        self.add_actor(self.A)
        self.add_actor(self.A2)
        self.A.y = 100
        self.A.x = 1000
        self.A2.y = 400
        self.A2.x = 1000

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.A.overlaps(self.A2):
            self.screen.b = 80
        else:
            self.screen.b = 0
        self.A.x = self.A.x - 2
        self.A2.x = self.A2.x - 1


class Screen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.r = 220
        self.g = 10
        self.b = 25
        self.add_stage(Stage())

class game(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen = Screen()

    pass

game().run()