import game

class Enemy1Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("images/start.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.x + self.width < game.scene2d.MyGame.get_screen_width():
            self.x += delta_time * 60
