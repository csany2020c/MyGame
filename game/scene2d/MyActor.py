import pygame
from game.scene2d.MyBaseActor import *
from game.simpleworld.Overlaps import *


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from __type_checking__ import *


class MyActor(MyBaseActor):

    def __init__(self, image_url: str = ""):
        MyBaseActor.__init__(self)
        self._original_image: pygame.Surface = None
        self._image: pygame.Surface = None
        self._image_url = image_url
        if image_url != "":
            self.set_image_url(image_url)
        self.create()

    def set_image_url(self, image_url: str) -> 'MyActor':
        # https://stackoverflow.com/questions/6395923/any-way-to-speed-up-python-and-pygame
        self._original_image = pygame.image.load(image_url).convert_alpha()
        self._image = self._original_image
        self._image_url = image_url
        self._w = self._image.get_width()
        self._h = self._image.get_height()
        self._calc_box()
        print(str(self) + " Set image: " + image_url + " " + str(self._image.get_width()) + " x " + str(self._image.get_height()))
        return self

    def get_image_url(self) -> str:
        return self._image_url

    def _transform(self):
        if self._r != 0:
            self._image = pygame.transform.smoothscale(self._original_image, (int(self._w), int(self._h)))
            self._calc_box()
            self._image = pygame.transform.rotate(self._image, -self._r)
        else:
            self._image = pygame.transform.smoothscale(self._original_image, (int(self._w), int(self._h)))
            self._calc_box()

    def set_size(self, width: int, height: int) -> 'MyActor':
        super().set_size(width, height)
        self._transform()
        return self

    def draw(self):
        self._stage.screen.game.surface.blit(self._image, (
            self._x - self._image.get_width() / 2 + self._w / 2, self._y - self._image.get_height() / 2 + self._h / 2))
        super().draw()

    def get_rotation(self) -> float:
        return self._r

    def set_rotation(self, angle: int) -> 'MyActor':
        super().set_rotation(angle)
        self._transform()
        return self

    image_url: str = property(get_image_url, set_image_url)
    r: int = property(get_rotation, set_rotation)
