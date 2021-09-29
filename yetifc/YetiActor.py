import game

class MenuActor1(game.scene2d.MyActor):
    def __init__(self, image_url: str = ""):
        super().__init__("../yetifc/Images/play.png")
        self.set_width(300)
        self.x = 500
        self.y = 50

class MenuActor2(game.scene2d.MyActor):
    def __init__(self, image_url: str = ""):
        super().__init__("../yetifc/Images/exit.png")
        self.set_width(300)
        self.x = 500
        self.y = 10
        self.hitbox_scale_h = 0.45
        self.hitbox_scale_w = 1
        self.set_on_mouse_down_listener(self.kilepes)

    def kilepes(self, sender, event):
        exit()