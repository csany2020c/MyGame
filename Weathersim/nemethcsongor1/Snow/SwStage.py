from Weathersim.nemethcsongor1.Actorok import *
from Weathersim.nemethcsongor1.start.SaScreen import *


class SwStage(game.scene2d.MyStage):

    def __init__(self):
        super().__init__()
        self.C = Cloudy()
        self.add_actor(self.C)

        self.Bg = Bg()
        self.add_actor(self.Bg)

        for i in range(30):
            self.S = Snow()
            self.add_actor(self.S)
            self.S.set_size(width=30, height=30)
            self.S.x = random.randint(a=0, b=1280)
            self.S.y = random.randint(a=-0, b=720)

        self.Ba = Back()
        self.add_actor(self.Ba)
        self.Ba.set_size(width=250, height=250)
        self.Ba.set_on_mouse_down_listener(self.klikk)

    def klikk(self, sender, event):
        print(sender)
        if event.button == 1:
            self.screen.game.set_screen(SaScreen())