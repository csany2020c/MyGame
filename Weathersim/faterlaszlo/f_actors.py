import game

class bg_actor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/landscape.png")

    def act(self, delta_time: float):
        super().act(delta_time)

class eg_actor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/sunny.png")


class napocska(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/sun.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.r += 10 * delta_time
        self.x += 1.5 + delta_time

class havazas(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/snow.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.r += 0.15 * delta_time
        self.y += 100 * delta_time

class eso(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/rain.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += 0.33 + delta_time
        
class felhos_actor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/cloudy.png")