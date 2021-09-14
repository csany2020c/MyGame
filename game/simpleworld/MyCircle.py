from game.simpleworld.MyShape import *
from game.simpleworld.Overlaps import *
from pygame.math import Vector2

from typing import TYPE_CHECKING
from typing import List

if TYPE_CHECKING:
    from __type_checking__ import *


class MyCircle(MyShape):
    debugLineNumbers: int = 16

    def __init__(self, x: float = 0, y: float = 0, radius: float = 1, rotation: float = 0,
                 offsetRotation: float = 0, originX: float = 0.5, originY: float = 0.5, offsetX: float = 0,
                 offsetY: float = 0, alignToLeftBottom: bool = True):
        super().__init__(x, y, radius / 2, radius / 2, rotation, offsetRotation, originX, originY, offsetX, offsetY,
                         alignToLeftBottom, shapeType="circle")
        self.radius = radius

    def getCorners(self) -> []:
        vector2s = []
        for i in range(self.debugLineNumbers):
            v = Vector2(self.radius, 0).rotate(360.0 / self.debugLineNumbers * i + self._rotation).__add__(
                Vector2(self._realCenterX, self._realCenterY))
            v.rotate(360.0 / self.debugLineNumbers * i + self._rotation)
            vector2s.append(v)
        return vector2s

    def overlaps(self, other: 'MyShape') -> bool:
        if other._shapeType == "circle":
            return Overlaps.circle_vs_circle(self, other)
        if other._shapeType == "rectangle":
            return Overlaps.rect_vs_circle(other, self)
        return False

    def setSize(self, width: float, height: float):
        if width < height:
            self.radius = width / 2.0
        else:
            height / 2.0
        super.setSize(width, height)

    def getRadius(self) -> float:
        return self.radius

    def setRadius(self, radius: float):
        self.radius = radius
        super.setSize(radius * 2.0, radius * 2.0)

