import game


class MenuActor1(game.scene2d.MyActor):
    def __init__(self, image_url: str = ""):
        super().__init__("../yetifc/Images/play.png")
        self.set_width(300)
        self.x = 500
        self.y = 50
        self.set_on_mouse_down_listener(self.setscreen)

    def setscreen(self, sender, event):
        self.stage.set_screen(GameScreen())

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

class MenuScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.set_background_color(0, 102, 102)
        self.add_stage(MenuStage())

class GameScreen(game.scene2d.MyScreen):
    def __init__(self):
        super().__init__()
        self.set_background_color(0, 102, 102)
        self.add_stage(GameStage())

class MenuStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        a = MenuActor1()
        a.y = 50
        self.add_actor(a)
        b = MenuActor2()
        b.y = 400
        self.add_actor(b)

class GameStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        a = MenuActor1()
        a.y = 50
        self.add_actor(a)
        b = MenuActor2()
        b.y = 400
        self.add_actor(b)

class GameRunner(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False):
        super().__init__(width, height, autorun)
        self.screen = MenuScreen()
        self.run()



GameRunner()