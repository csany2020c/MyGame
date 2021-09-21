from game.scene2d.MyText import *
from game.scene2d.MyBaseActor import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from __type_checking__ import *


class MyLabel(MyText, MyBaseActor):

    def __init__(self, font_name="arial.ttf", font_size: int = 32, string: str = "MyText"):
        MyText.__init__(self, font_name, font_size, string)
        MyBaseActor.__init__(self, self.get_text_surface())
