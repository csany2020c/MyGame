from game.scene2d.MyText import *
from game.scene2d.MyBaseActor import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from __type_checking__ import *


class MyLabel(MyText, MyBaseActor):


    def __init__(self, string: str = "MyText", font_name: str = "system", font_size: int = 64,font_color: List['int'] = (255, 255, 255)):
        super().__init__(string, font_name, font_size, font_color)
        MyText.__init__(self, string, font_name, font_size,font_color)
        MyBaseActor.__init__(self, self.get_text_surface())

    def on_font_style_changed(self):
        super().on_font_style_changed()
        self.original_image = self.get_text_surface()

    def on_text_changed(self):
        super().on_text_changed()
        self.original_image = self.get_text_surface()

