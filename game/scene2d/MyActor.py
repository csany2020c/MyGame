import pygame
import os
from game.scene2d.MyBaseActor import *


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from __type_checking__ import *


class MyActor(MyBaseActor):

    def __init__(self, image_url: str = ""):
        MyBaseActor.__init__(self, None)
        if not os.path.isfile(image_url):
            raise FileNotFoundError(image_url)
        self._image_url: str = ""
        self.set_image_url(image_url)

    def set_image_url(self, image_url: str) -> 'MyActor':
        self._image_url = image_url
        # https://stackoverflow.com/questions/6395923/any-way-to-speed-up-python-and-pygame
        try:
            self.original_image = pygame.image.load(self._image_url).convert_alpha()
        except:
            print("A képernyő nincs inicializálva.")
        return self

    def get_image_url(self) -> str:
        return self._image_url

    image_url: str = property(get_image_url, set_image_url)
