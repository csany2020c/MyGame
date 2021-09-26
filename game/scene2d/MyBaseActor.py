import abc

import pygame
from game.simpleworld.MyRectangle import *
from game.simpleworld.MyCircle import *
from game.scene2d.MyMouseListeners import *
from game.scene2d.MyKeyboardListeners import *
from game.scene2d.MyElapsedTime import *
from game.scene2d.MyTimers import *
from game.scene2d.MyZIndex import *
from game.simpleworld.Overlaps import *
from game.simpleworld.ShapeType import *

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from __type_checking__ import *


class MyBaseActor(MyElapsedTime, MyTimers, MyZIndex, MyMouseListeners, MyKeyboardListeners):

    def __init__(self, surface: pygame.Surface) -> None:
        MyElapsedTime.__init__(self)
        MyTimers.__init__(self)
        MyZIndex.__init__(self)
        MyMouseListeners.__init__(self)
        MyKeyboardListeners.__init__(self)
        self._stage: 'MyStage' = None
        self._x: float = 0
        self._y: float = 0
        self._r: float = 0
        self._w: float = 0
        self._h: float = 0
        self._hitbox_shapetype: ShapeType = ShapeType.Rectangle
        self._hitbox_scale_w: float = 1
        self._hitbox_scale_h: float = 1
        self._center_origin_x: float = 0
        self._center_origin_y: float = 0
        self._original_image: pygame.Surface = None
        self._image: pygame.Surface = None
        self._debug: bool = True
        self._alpha: int = 255
        self.set_original_image(surface)
        #self._box = [[0, 0], [0, 0], [0, 0], [0, 0]]

    def _transform(self):
        if self._r != 0:
            self._image = pygame.transform.smoothscale(self._original_image, (int(self._w), int(self._h)))
            self._image = pygame.transform.rotate(self._image, -self._r)
        else:
            self._image = pygame.transform.smoothscale(self._original_image, (int(self._w), int(self._h)))

    def get_delta_time(self) -> float:
        if self._stage is not None and self._stage.screen is not None and self._stage.screen.game is not None:
            return self._stage.screen.game.get_delta_time()
        else:
            return 0

    def act(self, delta_time: float):
        MyElapsedTime.act(self, delta_time)
        # MyTimers.act(self, delta_time)
#        MyMouseListeners.act(self, delta_time)

    def get_border_box(self)-> 'MyRectangle':
        return MyRectangle(x=self._x, y=self._y, width=self._w, height=self._h, rotation=self._r)

    def draw(self):
        self._stage.screen.game.surface.blit(self._image, (
            self._x - self._image.get_width() / 2 + self._w / 2,
            self._y - self._image.get_height() / 2 + self._h / 2))

        if self._debug:
            m = self.get_border_box()
            i = m.getCorners()
            for k in range(0, len(i) - 1):
                pygame.draw.line(self._stage.screen.game.surface, color=(0, 200, 27), start_pos=i[k], end_pos=i[k+1])
            pygame.draw.line(self._stage.screen.game.surface, color=(0, 200, 27), start_pos=i[0], end_pos=i[k+1])

            m = self.get_hitbox()
            i = m.getCorners()
            for k in range(0, len(i) - 1):
                pygame.draw.line(self._stage.screen.game.surface, color=(200, 200, 27), start_pos=i[k], end_pos=i[k+1])
            pygame.draw.line(self._stage.screen.game.surface, color=(200, 200, 27), start_pos=i[0], end_pos=i[k+1])

    def remove_from_stage(self):
        if self._stage is not None:
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
        return self._stage is not None

#    def _calc_box(self):
#        self._box = [list(self._image.get_rect().bottomleft), list(self._image.get_rect().bottomright),
#                     list(self._image.get_rect().topright), list(self._image.get_rect().topleft)]
        #        for i in range(4):
        #    self._box[i][0] += self._x
    #    self._box[i][1] += self._y

    def set_size(self, width: float, height: float) -> 'MyBaseActor':
        self._w = width
        self._h = height
        self._transform()
        return self

    def rotate_with(self, degree: float) -> 'MyBaseActor':
        self.set_rotation(self._r + degree)
        return self

    def set_x(self, x: float) -> 'MyBaseActor':
        self._x = x
        return self

    def set_y(self, y: float) -> 'MyBaseActor':
        self._y = y
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
        self._transform()
        return self

    def get_rotation(self) -> float:
        return self._r

    def get_z_index(self) -> int:
        return super().get_z_index()

    def set_z_index(self, z_index: int):
        super().set_z_index(z_index)
        if self._stage is not None:
            self._stage.actors.sort()

    def set_hitbox_shape(self, type: 'ShapeType'):
        self._hitbox_shapetype = type

    def set_hitbox_scale_w(self, w: float):
        self._hitbox_scale_w = w

    def set_hitbox_scale_h(self, h: float):
        self._hitbox_scale_h = h

    def get_hitbox_shape(self) -> 'ShapeType':
        return self._hitbox_shapetype

    def get_hitbox_scale_w(self) -> float:
        return self._hitbox_scale_w

    def get_hitbox_scale_h(self) -> float:
        return self._hitbox_scale_h

    def set_original_image(self, surface: pygame.Surface) -> 'MyBaseActor':
        if surface == None:
            self._original_image = None
            return
        self._original_image = surface  # pygame.image.load(image_url).convert_alpha()
        self._image = self._original_image
        self._image.set_alpha(self._alpha)
        self._w = self._image.get_width()
        self._h = self._image.get_height()
        print(str(self) + " Create Surface image: " + str(self._image.get_width()) + " x " + str(self._image.get_height()))

    def get_original_image(self) -> pygame.Surface:
        return self._original_image

    def set_alpha(self, alpha: int) -> 'MyBaseActor':
        self._alpha = alpha
        self._image.set_alpha(alpha)

    def get_alpha(self) -> int:
        return self._alpha

    def get_hitbox(self) -> 'MyShape':
        if self._hitbox_shapetype == ShapeType.Rectangle:
            return MyRectangle(x=self._x + (self._w - self._w * self._hitbox_scale_w) / 2, y=self._y + (self._h - self._h * self._hitbox_scale_h) / 2, width=self._w * self.hitbox_scale_w, height=self._h * self.hitbox_scale_h, rotation=self._r)
        if self._hitbox_shapetype == ShapeType.Circle:
            return MyCircle(x=self._x + self._w / 2,
                            y=self._y + self._h / 2,
                            radius=self._h / 2 * min(self.hitbox_scale_w, self.hitbox_scale_h),
                            alignToLeftBottom=False,
                            rotation=self._r)
        if self._hitbox_shapetype == ShapeType.Point:
            return MyCircle(x=self._x + self._w / 2,
                            y=self._y + self._h / 2,
                            radius=1,
                            alignToLeftBottom=False,
                            rotation=self._r)
        if self._hitbox_shapetype == ShapeType.Null:
            return None

    def overlaps_xy(self, x: int, y: int):
        #other = MyCircle(x=x, y=y, radius=1, alignToLeftBottom=False, rotation=0)
        other = Vector2(x,y)
        if self._hitbox_shapetype == ShapeType.Rectangle:
            return Overlaps.rect_vs_point(self.get_hitbox(), other)
        if self._hitbox_shapetype == ShapeType.Circle:
            return Overlaps.circle_vs_point(self.get_hitbox(), other)
        if self._hitbox_shapetype == ShapeType.Point:
            return Overlaps.circle_vs_point(self.get_hitbox(), other)

    def overlaps(self, other: 'MyBaseActor'):
        if self._hitbox_shapetype == ShapeType.Rectangle and other._hitbox_shapetype == ShapeType.Rectangle:
            return Overlaps.rect_vs_rect(self.get_hitbox(), other.get_hitbox())
        if self._hitbox_shapetype == ShapeType.Rectangle and other._hitbox_shapetype == ShapeType.Circle:
            return Overlaps.rect_vs_circle(self.get_hitbox(), other.get_hitbox())
        if self._hitbox_shapetype == ShapeType.Rectangle and other._hitbox_shapetype == ShapeType.Point:
            return Overlaps.rect_vs_circle(self.get_hitbox(), other.get_hitbox())
        if self._hitbox_shapetype == ShapeType.Circle and other._hitbox_shapetype == ShapeType.Rectangle:
            return Overlaps.rect_vs_circle(other.get_hitbox(), self.get_hitbox())
        if self._hitbox_shapetype == ShapeType.Circle and other._hitbox_shapetype == ShapeType.Circle:
            return Overlaps.circle_vs_circle(other.get_hitbox(), self.get_hitbox())
        if self._hitbox_shapetype == ShapeType.Circle and other._hitbox_shapetype == ShapeType.Point:
            return Overlaps.circle_vs_circle(other.get_hitbox(), self.get_hitbox())
        if self._hitbox_shapetype == ShapeType.Point and other._hitbox_shapetype == ShapeType.Rectangle:
            return Overlaps.rect_vs_circle(other.get_hitbox(), self.get_hitbox())
        if self._hitbox_shapetype == ShapeType.Point and other._hitbox_shapetype == ShapeType.Point:
            return Overlaps.circle_vs_circle(self.get_hitbox(), other.get_hitbox())
        if self._hitbox_shapetype == ShapeType.Point and other._hitbox_shapetype == ShapeType.Circle:
            return Overlaps.circle_vs_circle(self.get_hitbox(), other.get_hitbox())
        return False

    x: int = property(get_x, set_x)
    y: int = property(get_y, set_y)
    w: int = property(get_width, set_width)
    width: int = property(get_width, set_width)
    h: int = property(get_height, set_height)
    height: int = property(get_height, set_height)
    r: int = property(get_rotation, set_rotation)
    rotation: int = property(get_rotation, set_rotation)
    # screen_width: int = property(get_screen_width)
    # screen_height: int = property(get_screen_height)
    stage: 'MyStage' = property(get_stage, set_stage)
    z: int = property(get_z_index, set_z_index)
    z_index: int = property(get_z_index, set_z_index)
    hitbox_shape: str = property(get_hitbox_shape, set_hitbox_shape)
    hitbox_scale_w: float = property(get_hitbox_scale_w, set_hitbox_scale_w)
    hitbox_scale_h: float = property(get_hitbox_scale_h, set_hitbox_scale_h)
    original_image: pygame.Surface = property(get_original_image, set_original_image)
    alpha: int = property(get_alpha, set_alpha)
