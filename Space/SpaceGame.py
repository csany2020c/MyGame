import game
from GameScreen import *


class Space(game.scene2d.MyGame):

    def __init__(self, debug: bool = True):
        super().__init__(1280, 720, debug=debug)
        self.set_screen(GameScreen())
        #self.add_timer(game.scene2d.MyOneTickTimer(self.click, 10))
        self.add_timer(MyOneTickTimer(self.tikk, interval=5))

    def tikk(self, sender):
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    def click(self, sender, event=0):
        print("KLIKK")
        print(event)
        # sender.remove_from_stage()