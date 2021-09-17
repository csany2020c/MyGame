import game


class MenuScr(game.scene2d.MyScreen):


    def create(self):
        super().create()
        self.r = 100
        self.g = 0
        self.b = 0

class Menu(game.scene2d.MyGame):



    def create(self):
        super().create()
        self.screen = MenuScr()

Menu()