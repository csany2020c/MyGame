import game

class Auto(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("car.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(delta_time * 30)



class Stage(game.scene2d.MyStage):

    def create(self):
        super().create()
        self.A = Auto()
        self.A2 = Auto()
        self.add_actor(self.A)
        self.add_actor(self.A2)
        self.A.y = 100
        self.A.x = 50
        self.A2.y = 100
        self.A2.x = 400

    def act(self, delta_time: float):
        super().act(delta_time)
        self.A.rotate_with(delta_time * -100)
        if self.A.overlaps(self.A2):
            self.screen.b = 80
        else:
            self.screen.b = 0




class Screen(game.scene2d.MyScreen):

    def create(self):
        super().create()
        self.r = 200
        self.g = 10
        self.b = 25
        self.add_stage(Stage())

class game(game.scene2d.MyGame):

    def create(self):
        super().create()
        self.screen = Screen()

    pass

game().run()