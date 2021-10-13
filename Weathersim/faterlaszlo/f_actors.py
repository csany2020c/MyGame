import game

class bg_actor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/landscape.png")

    def act(self, delta_time: float):
        super().act(delta_time)

class bg_actor_s(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/landscape_s.png")

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

        if self.elapsed_time > 8:
            self.x = 750

class havazas(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/snow.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.r += 0.15 * delta_time
        self.y += 75 * delta_time
        if self.y > 720:
            self.y = 0

class eso(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/rain.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += 75 * delta_time
        if self.y > 720:
            self.y = 0
        
class felhos_actor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/cloudy.png")

class Bg1(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/bg1.jpg")

class apple(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/apple.png")

class cloud(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/cloud.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += 90 * delta_time
        if self.elapsed_time > 10:
            self.x = 1000

class snowman(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/snowman.png")
