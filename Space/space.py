import game


class Enemy1Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("Space/resources/images/enemy1.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.x + self.width < self.screen_width:
            self.x += self.get_delta_time() * 60


class GameStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()

    def create(self):
        super(GameStage, self).create()
        self.h1 = Enemy1Actor()
        self.h2 = Enemy1Actor()
        self.add_actor(self.h1)
        self.add_actor(self.h2)
        self.h2.x = 20
        self.h2.y = 20
        self.h2.w = 10
        self.h2.w = 200
        self.h2.z = -1100
        #self.h2.r = 45


class GameScreen(game.scene2d.MyScreen):

    def create(self):
        super().create()
        self.set_background_color(200, 100, 22)
        self.add_stage(GameStage())


class Space(game.scene2d.MyGame):

    def create(self):
        super().create()
        self.set_screen(GameScreen())




#sh = MyCircle(x=20, y=16, radius=2)
#print(sh)

