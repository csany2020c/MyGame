import math

from pygame.math import Vector2
from game.simpleworld.MyShape import *
from game.simpleworld.Overlaps import *

from typing import TYPE_CHECKING
from typing import List

if TYPE_CHECKING:
    from __type_checking__ import *


class MyRectangle(MyShape):
    """
       @param x Az alakzat helye
       @param y Az alakzat helye
       @param width  Az alakzat szélessége
       @param height Az alakzat magassága
       @param rotation Az alakzat forgatása az origin körül
       @param offsetRotation Az alakzat forgatása saját maga körül
       @param originX A forgatás középpontja
       @param originY A forgatás középpontja
       @param offsetX Eltolás az X koordinátától
       @param offsetY Eltolás az Y koordinátától
       @param alignToLeftBottom Igaz esetén az alakzatot a bal alsó sarkától számított X és Y koordinátákkal hozza létre, ellenkező esetben a küzepétől.
     """

    def __init__(self, x: float = 0, y: float = 0, width: float = 1, height: float = 1, rotation: float = 0,
                 offsetRotation: float = 0, originX: float = 0.5, originY: float = 0.5, offsetX: float = 0,
                 offsetY: float = 0, alignToLeftBottom: bool = True):
        super().__init__(x, y, width, height, rotation, offsetRotation, originX, originY, offsetX, offsetY,
                         alignToLeftBottom, shapeType="rectangle")

    def getCorners(self) -> List['Vector2']:
        vector2: List['Vector2'] = list()
        w2 = self._width / 2.0
        h2 = self._height / 2.0
        radius = math.sqrt(h2 * h2 + w2 * w2)
        radrot = math.radians(self._realRotation)
        angle = math.asin(h2 / radius)
        vector2.append(Vector2(self._realCenterX + radius * math.cos(radrot - angle),
                               self._realCenterY + radius * math.sin(radrot - angle)))
        vector2.append(Vector2(self._realCenterX + radius * math.cos(radrot + angle),
                               self._realCenterY + radius * math.sin(radrot + angle)))
        vector2.append(Vector2(self._realCenterX + radius * math.cos(radrot + math.pi - angle),
                               self._realCenterY + radius * math.sin(radrot + math.pi - angle)))
        vector2.append(Vector2(self._realCenterX + radius * math.cos(radrot + math.pi + angle),
                               self._realCenterY + radius * math.sin(radrot + math.pi + angle)))
        return vector2

    def overlaps(self, other: 'MyShape') -> bool:
        if other._shapeType == "circle":
            return Overlaps.rect_vs_circle(self, other)
        if other._shapeType == "rectangle":
            return Overlaps.rect_vs_rect(self, other)
        return False

