import pygame
from game.scene2d.MyBaseListeners import *
from game.scene2d.MyElapsedTime import *
from game.scene2d.MyTimers import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from __type_checking__ import *


class MyBaseActor(MyElapsedTime, MyTimers):

    def __init__(self) -> None:
        MyElapsedTime.__init__(self)
        MyTimers.__init__(self)
        self._stage: 'MyStage' = None
        self.create()

    def get_delta_time(self) -> float:
        if self._stage is not None and self._stage.screen is not None and self._stage.screen.game is not None:
            return self._stage.screen.game.get_delta_time()
        else:
            return 0

    def act(self, delta_time: float):
        MyElapsedTime.act(self, self.get_delta_time())
        MyTimers.act(self, delta_time)

    def remove_from_stage(self):
        try:
            self._stage.remove_actor(actor=self)
        except ValueError:
            print("A következő objektum már el lett távolítva korábban: " + str(id(self)))

    def set_stage(self, stage: 'MyStage'):
        self._stage = stage
        if stage == None:
            self.hide()
        else:
            self.show()

    def get_stage(self) -> 'MyStage':
        return self._stage

    def is_on_stage(self) -> bool:
        return self._stage != 0

    stage: 'MyStage' = property(get_stage, set_stage)


class MyActor(MyBaseActor, MyBaseListeners):

    def __init__(self, image_url: str = ""):
        MyBaseActor.__init__(self)
        MyBaseListeners.__init__(self)
        self._x = 0
        self._y = 0
        self._r = 0
        self._w = 0
        self._h = 0
        self._box = [[0, 0], [0, 0], [0, 0], [0, 0]]
        self._original_image: pygame.Surface = None
        self._image: pygame.Surface = None
        if image_url != "":
            self.set_image_url(image_url)

    #
    # def overlaps_with(self, otheractor: 'MyActor') -> bool:
    #     return self.colliderect(otheractor)
    #
    # def overlaps_point(self, pos) -> bool:
    #     return self.collidepoint(pos)
    #
    # def on_mouse_down(self, pos, button):
    #     if self.overlaps_point(pos):
    #         if self._on_mouse_down_listener != 0:
    #             self._on_mouse_down_listener(pos, button)
    #
    # def on_mouse_up(self, pos, button):
    #     if self.overlaps_point(pos):
    #         if self._on_mouse_up_listener != 0:
    #             self._on_mouse_up_listener(pos, button)
    #
    # def on_mouse_move(self, pos):
    #     if self.overlaps_point(pos):
    #         if self._on_mouse_move_listener != 0:
    #             self._on_mouse_move_listener(pos)
    #
    # def on_key_down(self, key, mod, unicode):
    #     if self._on_key_down_listener != 0:
    #         self._on_key_down_listener(key, mod, unicode)
    #
    # def on_key_up(self, key, mod):
    #     if self._on_key_up_listener != 0:
    #         self._on_key_up_listener(key, mod)

    def set_image_url(self, image_url: str):
        self._original_image = pygame.image.load(image_url)
        self._image = self._original_image
        self._image_url = image_url
        self._w = self._image.get_width()
        self._h = self._image.get_height()
        self._calc_box()
        print(str(self) + " Set image: " + image_url + " " + str(self._image.get_width()) + " x " + str(self._image.get_height()))

    def get_image_url(self)->str:
        return self._image_url

    def _calc_box(self):
        self._box = [list(self._image.get_rect().bottomleft), list(self._image.get_rect().bottomright),
                     list(self._image.get_rect().topright), list(self._image.get_rect().topleft)]
        for i in range(4):
            self._box[i][0] += self._x
            self._box[i][1] += self._y

    def _transform(self):
        if self._r != 0:
            self._image = pygame.transform.smoothscale(self._original_image, (self._w, self._h))
            self._calc_box()
            self._image = pygame.transform.rotate(self._image, self._r)
        else:
            self._image = pygame.transform.smoothscale(self._original_image, (self._w, self._h))
            self._calc_box()

    def set_size(self, width: int, height: int):
        self._w = width
        self._h = height
        self._transform()

    def rotate_with(self, degree: int):
        self.set_rotation(self.angle + degree)

    def set_x(self, x: int):
        self._x = x
        self._calc_box()

    def set_y(self, y: int):
        self._y = y
        self._calc_box()

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

    def set_width(self, width: int, aspect_ratio: bool = True):
        if aspect_ratio:
            self.set_size(width, int(float(self.h) * (float(width) / float(self.w))))
        else:
            self.set_size(width, self.h)

    def set_height(self, height: int, aspect_ratio: bool = True):
        if aspect_ratio:
            self.set_size(int(float(self.w) * (float(height) / float(self.h))), height)
        else:
            self.set_size(self.w, height)

    def get_width(self)->int:
        return self._w

    def get_height(self)->int:
        return self._h

    def draw(self):
        super().draw()
        self._stage.screen.game.pgScreen.blit(self._image, (
            self._x - self._image.get_width() / 2 + self._w / 2, self._y - self._image.get_height() / 2 + self._h / 2))
        for i in range(3):
            pygame.draw.line(self._stage.screen.game.pgScreen, color=(0, 200, 27), start_pos=self._box[i],
                             end_pos=self._box[i + 1])
        pygame.draw.line(self._stage.screen.game.pgScreen, color=(0, 200, 27), start_pos=self._box[0],
                         end_pos=self._box[3])

    def set_rotation(self, angle: int):
        self._r = angle
        self._transform()

    def get_rotation(self) -> int:
        return self._r

    def get_screen_width(self) -> int:
        return self.stage.screen.game.screen_width

    def get_screen_height(self) -> int:
        return self.stage.screen.game.screen_height

    x: int = property(get_x, set_x)
    y: int = property(get_y, set_y)
    w: int = property(get_width, set_width)
    width: int = property(get_width, set_width)
    h: int = property(get_height, set_height)
    height: int = property(get_height, set_height)
    r: int = property(get_rotation, set_rotation)
    rotation: int = property(get_rotation, set_rotation)
    image_url: str = property(get_image_url, set_image_url)
    screen_width: int = property(get_screen_width)
    screen_height: int = property(get_screen_height)
