import game

class sunActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("resources/images/sun.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.r += 20 * delta_time
        self.x += 32 * delta_time

class rainActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("resources/images/rain.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.r += 20 * delta_time
        self.x += 32 * delta_time

class snowActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("resources/images/snow.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.r += 20 * delta_time
        self.x += 32 * delta_time

class landscapeActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("resources/images/landscape.png")

    def act(self, delta_time: float):
        super().act(delta_time)

class sunnyActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("resources/images/sunny.png")

    def act(self, delta_time: float):
        super().act(delta_time)

class cloudyActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("resources/images/cloudy.png")

    def act(self, delta_time: float):
        super().act(delta_time)
