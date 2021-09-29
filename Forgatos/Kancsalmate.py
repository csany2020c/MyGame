import game

class Auto(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("car.png")

    def act(self, delta_time: float):
        super().act(delta_time)




class Stage(game.scene2d.MyStage):


    def __init__(self):
        super().__init__()
        c = 50

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

    def __init__(self):
        super().__init__()
        self.r = 200
        self.g = 10
        self.b = 25
        self.add_stage(Stage())

class game(game.scene2d.MyGame):

    def __init__(self):
        super().__init__()
        self.screen = Screen()

    pass

game().run()