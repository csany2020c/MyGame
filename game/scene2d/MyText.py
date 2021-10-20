import pygame.font

from game.scene2d.MyActor import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from __type_checking__ import *


class MyText:

    def __init__(self, string: str = "MyText", font_name: str = "system", font_size: int = 64):
        self._text: str = string
        self._font_color: List['int'] = [255, 255, 255]
        self._font_alpha: float = 1
        self._font_background: List['int'] = None
        self._font_name: str = font_name
        self._font_size: int = font_size
        self._font: pygame.font.Font = None
        self._load_font()

    def _load_font(self):
        if self._font_name.count(".ttf") != 0 or self._font_name.count(".otf") != 0:
            self._font = pygame.font.Font(self._font_name, self._font_size)
        else:
            self._font = pygame.font.SysFont(self._font_name, self._font_size)

    def get_text_surface(self) -> pygame.Surface:
        return self._font.render(self._text, True, self._font_color, self._font_background).convert_alpha()

    def set_bg_red(self, component: int):
        if self._font_background is None:
            self._font_background = [0, 0, 0]
        self._font_background[0] = component
        self.on_font_style_changed()
        
    def set_bg_green(self, component: int):
        if self._font_background is None:
            self._font_background = [0, 0, 0]
        self._font_background[1] = component
        self.on_font_style_changed()

    def set_bg_blue(self, component: int):
        if self._font_background is None:
            self._font_background = [0, 0, 0]
        self._font_background[2] = component
        self.on_font_style_changed()

    def set_bg_none(self):
        self._font_background = None

    def set_fg_red(self, component: int):
        self._font_color[0] = component
        self.on_font_style_changed()

    def set_fg_green(self, component: int):
        self._font_color[1] = component
        self.on_font_style_changed()

    def set_fg_blue(self, component: int):
        self._font_color[2] = component
        self.on_font_style_changed()

    def set_color(self, r: int, g: int, b: int):
        self._font_color = (r, g, b)
        self.on_font_style_changed()
   
    def set_background(self, r: int, g: int, b: int):
        self._font_background = (r, g, b)
        self.on_font_style_changed()
   
    def set_text(self, text: str):
        self._text = text
        self.on_text_changed()

    def set_font_name(self, font_name: str):
        self._font_name = font_name
        self._load_font()
        self.on_font_style_changed()
   
    def set_font_size(self, size: float):
        self._font_size = size
        self._load_font()
        self.on_font_style_changed()

    def set_font_italic(self, italic: bool):
        self._font.italic = italic
        self.on_font_style_changed()

    def set_font_bold(self, bold: bool):
        self._font.bold = bold
        self.on_font_style_changed()

    def set_font_underline(self, underline: bool):
        self._font.underline = underline
        self.on_font_style_changed()

    def on_font_style_changed(self):
        pass

    def on_text_changed(self):
        pass


#TODO: Getter, property fejlesztése, hasonlóan, mint a többi osztályban. 5-öst kap a helyesen megoldó.
