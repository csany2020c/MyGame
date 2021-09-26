import game
from GameScreen import *


class Space(game.scene2d.MyGame):

    def __init__(self):
        super().__init__(1280, 720)
        self.set_screen(GameScreen())
        self.add_timer(game.scene2d.MyOneTickTimer(self.click, 10))
        self.run()


    def click(self, sender, event=0):
        print("KLIKK")
        print(event)
        # sender.remove_from_stage()