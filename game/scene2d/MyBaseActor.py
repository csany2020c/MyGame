import abc

import pygame
from game.scene2d.MyBaseListeners import *
from game.scene2d.MyElapsedTime import *
from game.scene2d.MyTimers import *
from game.scene2d.MyZIndex import *

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from __type_checking__ import *


class MyBaseActor(MyElapsedTime, MyTimers, MyZIndex):

    def __init__(self) -> None:
        MyElapsedTime.__init__(self)
        MyTimers.__init__(self)
        MyZIndex.__init__(self)
        self._stage: 'MyStage' = None
        self._x: float = 0
        self._y: float = 0
        self._r: float = 0
        self._w: float = 0
        self._h: float = 0
        self._center_origin_x: float = 0
        self._center_origin_y: float = 0
        self._box = [[0, 0], [0, 0], [0, 0], [0, 0]]

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

    def set_stage(self, stage: 'MyStage') -> 'MyBaseActor':
        self._stage = stage
        if stage is None:
            self.hide()
        else:
            self.show()
        return self

    def get_stage(self) -> 'MyStage':
        return self._stage

    def is_on_stage(self) -> bool:
        return self._stage != 0

    def _calc_box(self):
        self._box = [list(self._image.get_rect().bottomleft), list(self._image.get_rect().bottomright),
                     list(self._image.get_rect().topright), list(self._image.get_rect().topleft)]
        for i in range(4):
            self._box[i][0] += self._x
            self._box[i][1] += self._y

    def set_size(self, width: float, height: float) -> 'MyBaseActor':
        self._w = width
        self._h = height
        self._calc_box()
        return self

    def rotate_with(self, degree: float) -> 'MyBaseActor':
        self.set_rotation(self.angle + degree)
        self._calc_box()
        return self

    def set_x(self, x: float) -> 'MyBaseActor':
        self._x = x
        self._calc_box()
        return self

    def set_y(self, y: float) -> 'MyBaseActor':
        self._y = y
        self._calc_box()
        return self

    def get_x(self) -> float:
        return self._x

    def get_y(self) -> float:
        return self._y

    def set_width(self, width: float, aspect_ratio: bool = True) -> 'MyBaseActor':
        if aspect_ratio:
            self.set_size(width, float(float(self.h) * (float(width) / float(self.w))))
        else:
            self.set_size(width, self.h)
        return self

    def set_height(self, height: float, aspect_ratio: bool = True) -> 'MyBaseActor':
        if aspect_ratio:
            self.set_size(float(float(self.w) * (float(height) / float(self.h))), height)
        else:
            self.set_size(self.w, height)
        return self

    def get_width(self) -> float:
        return self._w

    def get_height(self) -> float:
        return self._h

    def set_rotation(self, angle: float) -> 'MyBaseActor':
        self._r = angle
        return self

    def get_rotation(self) -> float:
        return self._r

    def get_screen_width(self) -> int:
        return self.stage.screen.game.screen_width

    def get_screen_height(self) -> int:
        return self.stage.screen.game.screen_height

    def get_z_index(self) -> int:
        return super().get_z_index()

    def set_z_index(self, z_index: int):
        super().set_z_index(z_index)
        if self._stage is not None:
            self._stage.actors.sort()

    x: int = property(get_x, set_x)
    y: int = property(get_y, set_y)
    w: int = property(get_width, set_width)
    width: int = property(get_width, set_width)
    h: int = property(get_height, set_height)
    height: int = property(get_height, set_height)
    r: int = property(get_rotation, set_rotation)
    rotation: int = property(get_rotation, set_rotation)
    screen_width: int = property(get_screen_width)
    screen_height: int = property(get_screen_height)
    stage: 'MyStage' = property(get_stage, set_stage)
    z: int = property(get_z_index, set_z_index)
    z_index: int = property(get_z_index, set_z_index)
