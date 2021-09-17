import game


class Enemy1Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("resources/images/enemy1.png")
        self.life = 5

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.x + self.width < self.screen_width:
            self.x += delta_time * 60
            self.rotate_with(delta_time * 20)