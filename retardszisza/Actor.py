import game

class szisza(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("images/szisza.png")
        self.set_width(100)

class kocsi1(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("images/kocsi.png")
        self.set_width(280)

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.x - self.width < game.scene2d.MyGame.get_screen_width():
            self.x -= delta_time * 150

class UtActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("images/uuut.png")
        self.set_width(1450)

class FalActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("images/fal.png")
        self.set_height(1000)

class Palyaszele1(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("images/palyaszele.png")
        self.set_width(1500)

class Palyaszele2(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("images/palyaszele.png")
        self.set_width(1500)

