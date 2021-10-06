import game

class cloudy (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("../!_resources/images/cloudy.png")


class sunny (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("../!_resources/images/sunny.png")
        self.set_on_key_down_listener(2)





class sun (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("../!_resources/images/sun.png")



class landscape (game.scene2d.MyActor):
    def __init__(self):
        super().__init__("../!_resources/images/landscape.png")
        self.set_on_mouse_down_listener(self.klikk)

    def klikk(self, sender, event):
        print(sender)
        print(event)

class DaniStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.a = sunny()
        self.b = sun()
        self.c = landscape()
        self.add_actor(self.a)
        self.add_actor(self.b)
        self.add_actor(self.c)

        self.b.x = 600


    def act(self, delta_time: float):
        super().act(delta_time)



class DaniScreen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(DaniStage())
        self.set_on_key_down_listener()





class DaniGame(game.scene2d.MyGame):

    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False,
                 debug: bool = False):
        super().__init__(width, height, autorun, autosize, debug)
        self.set_screen(DaniScreen())



danigame = DaniGame()
danigame.run()
