import abc
from pygame.math import Vector2
from game.simpleworld.MyCircle import *
import math

from typing import TYPE_CHECKING
from typing import List

if TYPE_CHECKING:
    from __type_checking__ import *


class Overlaps:

    @staticmethod
    def circle_vs_point(objA: 'MyCircle', point: 'Vector2') -> bool:
        return (objA.realCenterX - point.x) * (objA.realCenterX - point.x) + (
                objA.realCenterY - point.y) * (objA.realCenterY - point.y) <= (
                objA._radius) * (objA._radius)

    @staticmethod
    def rect_vs_point(rectangle: 'MyRectangle', point: 'Vector2') -> bool:
        p = MyCircle(x=point.x, y=point.y)
        return Overlaps.rect_vs_circle(rectangle, p)

    @staticmethod
    def circle_vs_circle(objA: 'MyCircle', objB: 'MyCircle') -> bool:
        return (objA.realCenterX - objB.realCenterX) * (objA.realCenterX - objB.realCenterX) + (
                objA.realCenterY - objB.realCenterY) * (objA.realCenterY - objB.realCenterY) <= (
                objA._radius + objB._radius) * (objA._radius + objB._radius)

    @staticmethod
    def rect_vs_circle(rectangle: 'MyRectangle', circle: 'MyCircle') -> bool:
        if ((rectangle.realCenterX - circle.realCenterX) * (rectangle.realCenterX - circle.realCenterX) +
                (rectangle.realCenterY - circle.realCenterY) * (rectangle.realCenterY - circle.realCenterY) >
                (rectangle._realRadius + circle._realRadius) * (rectangle._realRadius + circle._realRadius)):
            return False
# TODO: Javítani kell!!!! 5-öst kap, aki javít és tesztel.
        # Téglalap és kör forgatása a téglalap originje körül úgy, hogy az oldalai párhuzamosak legyenek a koordináta rendszerrel. A kör középpontja megváltozik, a téglalap forgatása 0 lesz.
        circleRotCenter = Vector2(circle.realCenterX - rectangle.realCenterX,
                                  circle.realCenterY - rectangle.realCenterY).rotate(
            -rectangle._rotation - rectangle.offsetRotation).__add__(Vector2(rectangle.realCenterX, rectangle.realCenterY))

        # A négyzet sarkai
        xRect: List['float'] = [0, 0, 0, 0]
        yRect: List['float'] = [0, 0, 0, 0]

        # A méret fele (gyorsítás)
        height1: float = rectangle._height / 2
        width1: float = rectangle._width / 2

        # Forgatás nélküli sarkok
        # Bal alsó
        xRect[0] = rectangle.realCenterX - width1
        yRect[0] = rectangle.realCenterY - height1

        # Bal felső
        xRect[1] = rectangle.realCenterX - width1
        yRect[1] = rectangle.realCenterY + height1

        # Jobb felső
        xRect[2] = rectangle.realCenterX + width1
        yRect[2] = rectangle.realCenterY + height1

        # Jobb alső
        xRect[3] = rectangle.realCenterX + width1
        yRect[3] = rectangle.realCenterY - height1

        # Ha a téglalap bármely sarka a körön beül van
        for i in range(0, 4):
            if ((xRect[i] - circleRotCenter.x) * (xRect[i] - circleRotCenter.x) +
                    (yRect[i] - circleRotCenter.y) * (yRect[i] - circleRotCenter.y) <=
                    (circle._radius) * (circle._radius)):
                return True

        # Elforgatott kör koordinátái
        xCirc: List['float'] = [0, 0, 0, 0]
        yCirc: List['float'] = [0, 0, 0, 0]

        # A kör legfelső pontja
        xCirc[0] = circleRotCenter.x + circle._radius
        yCirc[0] = circleRotCenter.y

        # legalsó pontja
        xCirc[1] = circleRotCenter.x - circle._radius
        yCirc[1] = circleRotCenter.y

        # bal pontja
        xCirc[2] = circleRotCenter.x
        yCirc[2] = circleRotCenter.y - circle._radius

        # jobb pontja
        xCirc[3] = circleRotCenter.x
        yCirc[3] = circleRotCenter.y + circle._radius

        # Ha a kör bármelyik (bal, jobb, felső, alsó) pontja a téglalapon belül van
        for i in range(0, 4):
            if (xRect[0] <= xCirc[i]) and (xRect[2] >= xCirc[i]) and (yRect[0] <= yCirc[i]) and (yRect[2] >= yCirc[i]):
                return True

        return False

    # https:#forums.coronalabs.com/topic/39094-code-for-rotated-rectangle-collision-detection/
    @staticmethod
    def rect_vs_rect(objA: 'MyRectangle', objB: 'MyRectangle'):

        if ((objA.realCenterX - objB.realCenterX) * (objA.realCenterX - objB.realCenterX) +
                (objA.realCenterY - objB.realCenterY) * (objA.realCenterY - objB.realCenterY) >
                (objA._realRadius + objB._realRadius) * (objA._realRadius + objB._realRadius)):
            return False

#         height1: float = objA._height / 2
#         height2: float = objB._height / 2
#
#         width1: float = objA._width / 2
#         width2: float = objB._width / 2
# # ??????????????????????????????????????????????????
#         radrot1: float = math.radians(-objA.realRotation)
#         radrot2: float = math.radians(-objB.realRotation)
#
#         radius1: float = math.sqrt(height1 * height1 + width1 * width1)
#         radius2: float = math.sqrt(height2 * height2 + width2 * width2)
#
#         angle1: float = math.asin(height1 / radius1)
#         angle2: float = math.asin(height2 / radius2)
#
#         x1: List['float'] = [0, 0, 0, 0, 0]
#         y1: List['float'] = [0, 0, 0, 0, 0]
#         x2: List['float'] = [0, 0, 0, 0, 0]
#         y2: List['float'] = [0, 0, 0, 0, 0]
#
#         x1[1] = objA.realCenterX + radius1 * math.cos(radrot1 - angle1)
#         y1[1] = objA.realCenterY + radius1 * math.sin(radrot1 - angle1)
#         x1[2] = objA.realCenterX + radius1 * math.cos(radrot1 + angle1)
#         y1[2] = objA.realCenterY + radius1 * math.sin(radrot1 + angle1)
#         x1[3] = objA.realCenterX + radius1 * math.cos(radrot1 + math.pi - angle1)
#         y1[3] = objA.realCenterY + radius1 * math.sin(radrot1 + math.pi - angle1)
#         x1[4] = objA.realCenterX + radius1 * math.cos(radrot1 + math.pi + angle1)
#         y1[4] = objA.realCenterY + radius1 * math.sin(radrot1 + math.pi + angle1)
#
#         x2[1] = objB.realCenterX + radius2 * math.cos(radrot2 - angle2)
#         y2[1] = objB.realCenterY + radius2 * math.sin(radrot2 - angle2)
#         x2[2] = objB.realCenterX + radius2 * math.cos(radrot2 + angle2)
#         y2[2] = objB.realCenterY + radius2 * math.sin(radrot2 + angle2)
#         x2[3] = objB.realCenterX + radius2 * math.cos(radrot2 + math.pi - angle2)
#         y2[3] = objB.realCenterY + radius2 * math.sin(radrot2 + math.pi - angle2)
#         x2[4] = objB.realCenterX + radius2 * math.cos(radrot2 + math.pi + angle2)
#         y2[4] = objB.realCenterY + radius2 * math.sin(radrot2 + math.pi + angle2)

        ac = objA.getCorners()
        bc = objB.getCorners()

        # x1: List['float'] = [0, 0, 0, 0, 0]
        # y1: List['float'] = [0, 0, 0, 0, 0]
        # x2: List['float'] = [0, 0, 0, 0, 0]
        # y2: List['float'] = [0, 0, 0, 0, 0]

        x1: List['float'] = [0, ac[0].x, ac[1].x, ac[2].x, ac[3].x]
        y1: List['float'] = [0, ac[0].y, ac[1].y, ac[2].y, ac[3].y]
        x2: List['float'] = [0, bc[0].x, bc[1].x, bc[2].x, bc[3].x]
        y2: List['float'] = [0, bc[0].y, bc[1].y, bc[2].y, bc[3].y]


        axisx: List['float'] = [0, 0, 0, 0, 0]
        axisy: List['float'] = [0, 0, 0, 0, 0]

        axisx[1] = x1[1] - x1[2]
        axisy[1] = y1[1] - y1[2]
        axisx[2] = x1[3] - x1[2]
        axisy[2] = y1[3] - y1[2]

        axisx[3] = x2[1] - x2[2]
        axisy[3] = y2[1] - y2[2]
        axisx[4] = x2[3] - x2[2]
        axisy[4] = y2[3] - y2[2]

        for k in range(1, 5):
            proj = x1[1] * axisx[k] + y1[1] * axisy[k]

            minProj1 = proj
            maxProj1 = proj

            for i in range(2, 5):
                proj = x1[i] * axisx[k] + y1[i] * axisy[k]

                if proj < minProj1:
                    minProj1 = proj
                else:
                    if proj > maxProj1:
                        maxProj1 = proj

            proj = x2[1] * axisx[k] + y2[1] * axisy[k]

            minProj2 = proj
            maxProj2 = proj

            for j in range(2, 5):
                proj = x2[j] * axisx[k] + y2[j] * axisy[k]
                if proj < minProj2:
                    minProj2 = proj
                else:
                    if proj > maxProj2:
                        maxProj2 = proj

            if (maxProj2 < minProj1) or (maxProj1 < minProj2):
                return False

        return True
