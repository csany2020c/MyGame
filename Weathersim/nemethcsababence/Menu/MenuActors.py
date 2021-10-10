import game


class menunap(game.scene2d.MyActor):

    def __init__(self):
        self.nap = super().__init__('images/sun.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(delta_time * 20)


class menuho(game.scene2d.MyActor):

    def __init__(self):
        self.ho = super().__init__('images/snow.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 50
        self.rotate_with(delta_time * 20)
        if self.y > 375:
            self.y = 100


class menueso(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/rain.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 50
        if self.y > 375:
            self.y = 100


class tajkep(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/tajkep.jpg')