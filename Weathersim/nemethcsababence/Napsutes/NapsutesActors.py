import game


class taj(game.scene2d.MyActor):

    def __init__(self):
        self.taj = super().__init__('images/landscape.png')


class kekeg(game.scene2d.MyActor):

    def __init__(self):
        self.eg = super().__init__('images/sunny.png')

class madar(game.scene2d.MyActor):

    def __init__(self):
        self.madar = super().__init__('images/madar.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 20
        self.x += delta_time * 100
        if self.x > 1350:
            self.y = 0
            self.x = 0





class nap(game.scene2d.MyActor):

    def __init__(self):
        self.nap = super().__init__('images/sun.png')

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.x + self.width < game.scene2d.MyGame.get_screen_width():
            self.x += delta_time * 60
            self.rotate_with(delta_time * 20)


class button4(game.scene2d.MyActor):

    def __init__(self):
        self.butt4 = super().__init__('images/napsutes.png')


class MenuImage(game.scene2d.MyActor):

    def __init__(self):
        self.Image = super().__init__('images/menuimage.png')

class button5(game.scene2d.MyActor):

    def __init__(self):
        self.butt5 = super().__init__('images/Vissza.png')
