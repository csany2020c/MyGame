import game


class NapocskaActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("jarasok/sun.png")
        self.x += 650
        self.y += 125
        self.set_width(800)

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(0.2)


class HatterActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("jarasok/sunny.png")


class Hatter2Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("jarasok/cloudy.png")


class LandscapeActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("jarasok/landscape.png")


class HavzikActor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("jarasok/snow.png")
        self.y -= 50

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(3)
        self.y += delta_time * 100
        self.x += delta_time * 100


class Havzik2Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("jarasok/snow.png")
        self.x += 300
        self.y -= 50

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(3)
        self.y += delta_time * 100
        self.x += delta_time * 100


class Havzik3Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("jarasok/snow.png")
        self.x -= 300
        self.y -= 50

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(3)
        self.y += delta_time * 100
        self.x += delta_time * 100


class Havzik4Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("jarasok/snow.png")
        self.x += 600
        self.y -= 50

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(3)
        self.y += delta_time * 100
        self.x += delta_time * 100


class Havzik5Actor(game.scene2d.MyActor):

    def __init__(self):
        super().__init__("jarasok/snow.png")
        self.x += 900
        self.y -= 50

    def act(self, delta_time: float):
        super().act(delta_time)
        self.rotate_with(3)
        self.y += delta_time * 100
        self.x += delta_time * 100


class CseppActor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("jarasok/rain.png")
        self.set_width(50)

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 1000


class Icon1Actor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("jarasok/icon1.png")
        self.set_width(50)

class Icon2Actor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("jarasok/icon2.png")
        self.set_width(60)
        self.x += 50

class Icon3Actor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("jarasok/icon3.png")
        self.set_width(45)
        self.x += 110

class Icon4Actor(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("jarasok/icon4.png")
        self.set_width(50)
        self.x += 160

