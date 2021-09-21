import pygame.font

from game.scene2d.MyActor import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from __type_checking__ import *


class MyText:

    def __init__(self, font_name="arial.ttf", font_size: int = 32, string: str = "MyText"):
        self._text: str = string
        self._font_color = (155, 255, 255)
        self._font_alpha: float = 1
        self._background = None
        self._font_name = font_name
        self._font_size = font_size
        self._font = pygame.font.SysFont(font_name, font_size)
        self._font.italic = True

    def get_text_surface(self) -> pygame.Surface:
        return self._font.render(self._text, True, self._font_color, self._background)

    # def set_color(self, r: int, g: int, b: int, a: float = 1):
    #     self._font_color = (r, g, b)
    #     self._font_alpha = a
    #
    # def set_background(self, r: int, g: int, b: int):
    #     self._background = (r, g, b)
    #
    # def set_text(self, text: str):
    #     self._text = text
    #
    # def set_alpha(self, a: float):
    #     self._font_alpha = a
    #
    # def set_font_name(self, font_name: str):
    #     self._font_name = font_name
    #
    # def set_font_size(self, size: float):
    #     self._font_size = size
