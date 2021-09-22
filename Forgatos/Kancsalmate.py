import game

class Auto(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("car.png")

    def act(self, delta_time: float):
        super().act(delta_time)




class Stage(game.scene2d.MyStage):

    def create(self):

        c = 50
        super().create()
        self.A = Auto()
        self.A2 = Auto()
        self.add_actor(self.A)
        self.add_actor(self.A2)
        self.A.y = 100
        self.A2.x = 300
        self.A2.y = 100



    def act(self, delta_time: float):
        super().act(delta_time)
        self.A.x = self.A.x + 2
        self.A2.x = self.A2.x + 1




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