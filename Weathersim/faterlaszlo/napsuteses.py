import game

class napsutesesactor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/landscape.png")

    def act(self, delta_time: float):
        super().act(delta_time)


class napocska(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("!_resources/images/sun.png")


    def act(self, delta_time: float):
        super().act(delta_time)
        self.r += 10 * delta_time
        self.x += 2 + delta_time


class napstage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.bg = napsutesesactor()
        self.sun = napocska()
        self.add_actor(self.bg)
        self.add_actor(self.sun)
        self.sun.x = 5
        self.sun.y = 50
        self.sun.w = 300






class napscreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.set_background_color(120, 100, 90)
        self.add_stage(napstage())

class maga_a_game(game.scene2d.MyGame):
    def __init__(self):
        super().__init__()
        self.set_screen(napscreen())


maga_a_game().run()

