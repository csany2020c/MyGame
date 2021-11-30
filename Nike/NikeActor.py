import game
import pygame
from game.simpleworld.ShapeType import ShapeType

class FatJordan(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/fatjordanact.png")
        self.x += 500
        self.y += 250


class MenuText(game.scene2d.MyLabel):

    def __init__(self, string: str = "Text") -> None:
            game.scene2d.MyLabel.__init__(self, string=string, font_name="arial")

class GameBg(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/bgpic.jpg")
        self.y = -450

class Sztrit(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/streett.png")
        self.y = 600
        self.set_width(5000)
        self.hitbox_shape = ShapeType.Rectangle

class FatJordanact(game.scene2d.MyActor):
    def __init__(self):
        super().__init__("images/fatjordanact.png")
        self.jump: float = 0
        self.go = True
        self.hitbox_scale_h = 0.9
        self.hitbox_scale_w = 0.9
        self.hitbox_shape = ShapeType.Rectangle
        self.bill()

    def bill(self):
        self.set_on_key_press_listener(self.key_down)

    def key_down(self, sender, event):
        print(sender)
        print(event)
        if event.key == pygame.K_w:
            self.jump()

        if event.key == pygame.K_SPACE:
            self.jump()


    def act(self, delta_time: float):
        super().act(delta_time)

        if self.jump > 0:
            self.y -= 450 * delta_time
            self.ugras -= 450 * delta_time

        else:
            if self.go:
                self.y += 6

    def jump(self):
        self.jump = 305

    def start(self):
        self.go = True

    def stop(self):
        self.go = False

    def press(self, sender, event):
        if event.key == pygame.K_d:
            sender.x += 10
            self.camera.set_tracking_window(0.2,0.2,0.6,0.2)
        if event.key == pygame.K_a:
            sender.x -= 10
            self.camera.set_tracking_window(0.6,0.2,0.2,0.2)

    def interval(self, sender):
        self.x += 100 * self.get_delta_time()
        pass





