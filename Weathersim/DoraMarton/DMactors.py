import game
import pygame
from Weathersim.DoraMarton.DMscreen import *

class rain(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("rain.png")

        self.set_width(50)

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 1000
        if self.y > 720:
            self.y = -100

class snow(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("snow.png")

    def act(self, delta_time: float):
        super().act(delta_time)
        self.y += delta_time * 200
        self.rotate_with(delta_time * 20)
        if self.y > 720:
            self.y = -100

class sun(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("sun.png")
        self.y = -100
    def act(self, delta_time: float):
        super().act(delta_time)
        if self.x + self.width < game.scene2d.MyGame.get_screen_width():
            self.x += delta_time * 40
        self.rotate_with(delta_time * 10)

class sunny(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("sunny.png")

class cloudy(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("cloudy.png")

class landscape(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("landscape.png")

class egyikiras(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("egyiras.PNG")
        self.x = 500
        self.y = 100
class megegyiras(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("megegyiras.PNG")
        self.x = 500
        self.y = 200
class ismetiras(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("vanmeg.PNG")
        self.x = 500
        self.y = 300
class elsefogy(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("eskuutso.PNG")
        self.x = 500
        self.y = 400
class demegis(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("kamuztam.PNG")
        self.x = 500
        self.y = 500

class exit(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("exit.png")
        self.x = 1060
        self.y = 500
        def mouse_down(sender, event):
            print(event)
            print(sender)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
        self.set_on_mouse_down_listener(mouse_down)
