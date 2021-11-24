import game

class Enemy1Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("images/szisza.png")
        self.set_width(100)



class Enemy2Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("images/kocsi.png")
        self.set_width(100)

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.x - self.width < game.scene2d.MyGame.get_screen_width():
            self.x -= delta_time * 60


class UtActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("images/ut.jpg")
        self.set_width(1450)


