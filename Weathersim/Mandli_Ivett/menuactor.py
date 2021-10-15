import game


class Actor1(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("sun.png")


class Actor2(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("rain.png")


class Actor3(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("havaseso.png")


class Actor4(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("snow.png")


class MenuStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.sun = Actor1()
        self.rain = Actor2()
        self.havaseso = Actor3()
        self.snow = Actor4()
        self.add_actor(self.sun)
        self.add_actor(self.rain)
        self.add_actor(self.havaseso)
        self.add_actor(self.snow)



