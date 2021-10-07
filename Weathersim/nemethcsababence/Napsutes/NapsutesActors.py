import game


class taj(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/landscape.png')


class kekeg(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/sunny.png')


class nap(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/sun.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.x + self.width < game.scene2d.MyGame.get_screen_width():
            self.x += delta_time * 60
            self.rotate_with(delta_time * 20)


class button4(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/napsutes.png')


class MenuImage(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/MenuScreen.png')

class button5(game.scene2d.MyActor):

    def __init__(self):
        self.map = super().__init__('images/Vissza.png')
