import game
import pygame
from game.scene2d.MyLabel import *
from game.scene2d.MyStage import *
from game.scene2d import MyPermanentTimer, MyOneTickTimer, MyBaseActor, MyTickTimer, MyIntervalTimer

class AlertBox(game.scene2d.MyActor):
    def __init__(self,stage:MyStage,text:str):
        super().__init__("successalert.png")
        pygame.init()
        self.thatStage = stage
        self.irany = "in"
        self.szelesseg = pygame.display.get_surface().get_width()
        self.set_position(self.szelesseg / 2 - self.get_width()/2, -300)
        self.text = MyLabel("","system",64,[255,255,255])
        self.text.set_text(text)
        self.text.set_position(int(self.get_x() + self.get_width()/2),self.get_y() + self.get_height()/2)
        self.thatStage.add_actor(self.text)
        self.timer = MyOneTickTimer(func=self.handleTimer,interval=1)

    def handleTimer(self,sender):
        self.menjFel()

    def act(self, delta_time: float):
        super().act(delta_time)
        if self.irany == "in":
            if self.get_y() > 0:
                self.y = int(self.get_y() + 10)
            else:
                self.add_timer(self.timer)
        elif self.irany == "out":
            if self.get_y() > - 200:
                self.y = int(self.get_y() - 10)
            else:
                self.thatStage.remove_actor(self)

    def menjFel(self):
        self.irany = "out"

