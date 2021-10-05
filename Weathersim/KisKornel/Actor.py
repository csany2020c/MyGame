import game

class SunnyActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("sun.png")


    def act(self, delta_time: float):
        super().act(delta_time)
        self.x += delta_time * 100


class backgroundActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("landscape.png")



class skyActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("sunny.png")