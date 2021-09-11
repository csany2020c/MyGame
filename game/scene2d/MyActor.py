import pygame
from game.scene2d.MyBaseActor import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from __type_checking__ import *


class MyActor(MyBaseActor, MyBaseListeners):

    def __init__(self, image_url: str = ""):
        MyBaseActor.__init__(self)
        MyBaseListeners.__init__(self)
        self._original_image: pygame.Surface = None
        self._image: pygame.Surface = None
        self._image_url = image_url
        if image_url != "":
            self.set_image_url(image_url)
        self.create()

    def set_image_url(self, image_url: str) -> 'MyActor':
        self._original_image = pygame.image.load(image_url)
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
            self._image = pygame.transform.rotate(self._image, self._r)
        else:
            self._image = pygame.transform.smoothscale(self._original_image, (int(self._w), int(self._h)))
            self._calc_box()

    def set_size(self, width: int, height: int) -> 'MyActor':
        super().set_size(width, height)
        self._transform()
        return self

    def draw(self):
        super().draw()
        self._stage.screen.game.surface.blit(self._image, (
            self._x - self._image.get_width() / 2 + self._w / 2, self._y - self._image.get_height() / 2 + self._h / 2))
        for i in range(3):
            pygame.draw.line(self._stage.screen.game.surface, color=(0, 200, 27), start_pos=self._box[i],
                             end_pos=self._box[i + 1])
        pygame.draw.line(self._stage.screen.game.surface, color=(0, 200, 27), start_pos=self._box[0],
                         end_pos=self._box[3])

    def set_rotation(self, angle: int) -> 'MyActor':
        super().set_rotation(angle)
        self._transform()
        return self

    image_url: str = property(get_image_url, set_image_url)

