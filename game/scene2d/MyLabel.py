from game.scene2d.MyText import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from __type_checking__ import *


class MyLabel(MyText):

    def __init__(self, pos=(0, 0), angle=0):
        MyText.__init__(self)
        MyBaseActor.__init__(self)
        self.x: int = pos[0]
        self.y: int = pos[1]
        self.angle: int = angle

    def set_x(self, x: int):
        self.x = x

    def set_y(self, y: int):
        self.y = y

    def draw(self):
        Screen(pygame.display.get_surface()).draw.text(self.text, (self.x, self.y), angle=self.angle, color=self.color, background=self.background, fontname=self.fontname, fontsize=self.fontsize, alpha=self.alpha)

    def set_rotation(self, angle: int):
        self.angle = angle
