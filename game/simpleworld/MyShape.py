import abc
from pygame.math import Vector2
import math

from typing import TYPE_CHECKING
from typing import List

if TYPE_CHECKING:
    from __type_checking__ import *


class MyShape(metaclass=abc.ABCMeta):

    def __init__(self, x: float = 0, y: float = 0, width: float = 1, height: float = 1, rotation: float = 0,
                 offsetRotation: float = 0, originX: float = 0.5, originY: float = 0.5, offsetX: float = 0,
                 offsetY: float = 0, alignToLeftBottom: bool = True, shapeType = "shape"):

        self._shapeType = shapeType

        #
        # @param x Az alakzat helye
        # @param y Az alakzat helye
        # @param width  Az alakzat szélessége
        # @param height Az alakzat magassága
        # @param rotation Az alakzat forgatása az origin körül
        # @param offsetRotation Az alakzat forgatása saját maga körül
        # @param originX A forgatás középpontja
        # @param originY A forgatás középpontja
        # @param offsetX Eltolás az X koordinátától
        # @param offsetY Eltolás az Y koordinátától
        # @param alignToLeftBottom Igaz esetén az alakzatot a bal alsó sarkától számított X és Y koordinátákkal hozza létre, ellenkező esetben a küzepétől.
        #
        #
        # Tényleges középpont. Ez alapján számolja a pozícióját. center=cx+offsetx forgatva origin körül
        #
        self._realCenterX: float = 0

        #
        # Tényleges középpont. Ez alapján számolja a pozícióját. center=cx+offsetx forgatva origin körül
        #
        self._realCenterY: float = 0

        #
        # A szélességből és magasságból számított, körülvevő kür sugara
        #
        self._realRadius: float = 0

        #
        # Tényleges forgatás. A offsetRotation forgatás és az elforgatás összege.
        #
        self._realRotation: float = 0

        #
        # Szélesség. Forgatásnál nem változik.
        #
        self._width: float = 0

        #
        # Magasság. Forgatásnál nem változik.
        #
        self._height: float = 0

        #
        # Forgatás fokban megadva.
        #
        self._rotation: float = 0

        #
        # Relatív elforgatás. realRotation=offsetRotation+rotation
        #
        self._offsetRotation: float = 0

        #
        # Relatív eltolás cx-től számítva. center=cx+offsetx
        #
        self._offsetX: float = 0

        #
        # Relatív eltolás cy-tól számítva. center=cy+offsety
        #
        self._offsetY: float = 0

        #
        # A középpont abszolút pozíciója a játéktérben.
        #
        self._centerX: float = 0

        #
        # A középpont abszolút pozíciója a játéktérben.
        #
        self._centerY: float = 0

        #
        # A forgatás középpontja. Relatív a valódi helyétől (offsetxy+cxy) az alakzatnak.
        #
        self._originX: float = 0

        #
        # A forgatás középpontja. Relatív a valódi helyétől (offsetxy+cxy) az alakzatnak.
        #
        self._originY: float = 0

        self._active: bool = True

        # Az alakzathoz hozzácsatolható objektum, például egy Actor
        self._userData = None

        self._offsetX = offsetX
        self._offsetY = offsetY
        self._width = width
        self._height = height
        self._offsetRotation = offsetRotation
        self._rotation = rotation
        if alignToLeftBottom:
            self.setPosition(x, y)
            self.setOrigin(originX, originY)
        else:
            self.setPositionFromCenter(x, y)
            self.setOriginFromCenter(originX, originY)

    @abc.abstractmethod
    def getCorners(self) -> List['Vector2']:
        pass

    @abc.abstractmethod
    def overlaps(self, other: 'MyShape') -> bool:
        pass

    def setSizeByCenter(self, width: float, height: float)->'MyShape':
        olx = self.getLeftBottomX()
        oly = self.getLeftBottomY()
        oldW = self._width
        oldH = self._height
        oldOriginX = self._originX
        oldOriginY = self._originY
        orcx = self._realCenterX
        orcy = self.self._realCenterY

        self._originX = self._originX / self._width * width
        self._originY = self._originY / self._height * height
        self._width = width
        self._height = height
        self.calculateCenterXY()
        self._centerX += orcx - self._realCenterX
        self._centerY += orcy - self._realCenterY
        self.calculateCenterXY()

        self.sizeChanged(width, height, oldW, oldH)
        self.positionChanged(self.getLeftBottomX(), self.getLeftBottomY(), olx, oly)
        return self

    def setSize(self, width: float, height: float)->'MyShape':
        olx = self.getLeftBottomX()
        oly = self.getLeftBottomY()
        oldOriginX = self._originX
        oldOriginY = self._originY
        oldW = self._width
        oldH = self._height

        self._originX = self._originX / self._width * width
        self._originY = self._originY / self._height * height
        self._centerX -= (self._width - width) / 2
        self._centerY -= (self._height - height) / 2
        self._width = width
        self._height = height
        self.calculateCenterXY()

        self.sizeChanged(width, height, oldW, oldH)
        self.positionChanged(self.getLeftBottomX(), self.getLeftBottomY(), olx, oly)
        return self

    def setSizeByOrigin(self, width: float, height: float)->'MyShape':
        olx = self.getLeftBottomX()
        oly = self.getLeftBottomY()
        oldOriginX = self._originX
        oldOriginY = self._originY
        oldW = self._width
        oldH = self._height

        self._originX = self._originX / self._width * width
        self._originY = self._originY / self._height * height
        self._centerX -= self._originX - oldOriginX
        self._centerY -= self._originY - oldOriginY
        self._width = width
        self._height = height
        self.calculateCenterXY()

        self.sizeChanged(width, height, oldW, oldH)
        self.positionChanged(self.getLeftBottomX(), self.getLeftBottomY(), olx, oly)
        return self

    def calculateCenterXY(self)->'MyShape':
        self._realRotation = self._rotation + self._offsetRotation
        origCenter = Vector2(self._centerX + self._offsetX, self._centerY + self._offsetY)
        origin = Vector2(self._originX + self._centerX + self._offsetX, self._originY + self._centerY + self._offsetY)
        v = origCenter.__sub__(origin)
        v.rotate(self._rotation)
        s = v.__add__(origin)
        self._realCenterX = s.x
        self._realCenterY = s.y
        self._realRadius = math.sqrt(self._width * self._width + self._height * self._height) / 2.0
        return self

    def setPosition(self, X: float, Y: float)->'MyShape':
        olx = self.getLeftBottomX()
        oly = self.getLeftBottomY()
        self._centerX = X + self._width / 2.0
        self._centerY = Y + self._height / 2.0
        self.calculateCenterXY()
        self.positionChanged(self.getLeftBottomX(), self.getLeftBottomY(), olx, oly)
        return self

    def setX(self, x: float)->'MyShape':
        self.setPosition(x, self.getLeftBottomY())
        return self

    def setY(self, y: float)->'MyShape':
        self.setPosition(self.getLeftBottomX(), y)
        return self

    def setPositionFromCenter(self, centerX: float, centerY: float)->'MyShape':
        olx = self.getLeftBottomX()
        oly = self.getLeftBottomY()
        self._centerX = centerX
        self._centerY = centerY
        self.calculateCenterXY()
        self.positionChanged(self.getLeftBottomX(), self.getLeftBottomY(), olx, oly)
        return self

    def setOffset(self, offsetX: float, offsetY: float)->'MyShape':
        olx = self.getLeftBottomX()
        oly = self.getLeftBottomY()
        self._offsetX = offsetX
        self._offsetY = offsetY
        self.calculateCenterXY()
        self.positionChanged(self.getLeftBottomX(), self.getLeftBottomY(), olx, oly)
        return self

    def rotateBy(self, degree: float)->'MyShape':
        self.setRotation(self._rotation + degree)
        return self

    def setRotation(self, degree: float)->'MyShape':
        oro = self._rotation
        self._rotation = degree
        self.calculateCenterXY()
        self.rotationChanged(self._rotation, oro)
        return self

    def getRealCenterX(self) -> float:
        return self._realCenterX

    def getRealCenterY(self) -> float:
        return self._realCenterY

    def getWidth(self) -> float:
        return self._width

    def getHeight(self) -> float:
        return self._height

    def getRotation(self) -> float:
        return self._rotation

    def getOffsetX(self) -> float:
        return self._offsetX

    def getOffsetY(self) -> float:
        return self._offsetY

    def getCenterX(self) -> float:
        return self._centerX

    def getCenterY(self) -> float:
        return self._centerY

    def getX(self) -> float:
        return self._realCenterX - self._width / 2

    def getY(self) -> float:
        return self._realCenterY - self._height / 2

    def setOriginToCenter(self)->'MyShape':
        ox: float = self._originX
        oy: float = self._originY
        self._originX = 0
        self._originY = 0
        self.calculateCenterXY()
        self.originChanged(self._originX, self._originY, ox, oy)
        return self

    #
    # Forgatási középpont beállítása a középponttól számítva
    # @param x
    # @param y
    #
    def setOriginFromCenter(self, x: float, y: float)->'MyShape':
        ox = self._originX
        oy = self._originY
        self._originX = x - self._offsetX
        self._originY = y - self._offsetY
        self.calculateCenterXY()
        self.originChanged(self._originX, self._originY, ox, oy)
        return self

    #
    # Forgatási középpont beállítása a bal alsó saroktól mérve.
    # @param x
    # @param y
    #
    def setOrigin(self, x: float, y: float)->'MyShape':
        ox = self._originX
        oy = self._originY
        self._originX = x - self._width / 2 - self._offsetX
        self._originY = y - self._height / 2 - self._offsetY
        self.calculateCenterXY()
        self.originChanged(self._originX, self._originY, ox, oy)
        return self

    def setOriginFixedPositionAbsolute(self, x: float, y: float)->'MyShape':
        self.setOriginFixedPosition(x - self.getLeftBottomX(), y - self.getLeftBottomY())
        return self

    def setOriginFixedPosition(self, x: float, y: float)->'MyShape':
        ox = self._originX
        oy = self._originY
        olx = self.getLeftBottomX()
        oly = self.getLeftBottomY()
        v0 = Vector2(self._realCenterX, self._realCenterY)
        self.setOrigin(x, y)
        self.calculateCenterXY()
        v1 = Vector2(self._realCenterX, self._realCenterY)
        v0 = v0.__sub__(v1)
        self._centerX += v0.x
        self._centerY += v0.y
        self.calculateCenterXY()
        self.originChanged(self._originX, self._originY, ox, oy)
        self.positionChanged(self.getLeftBottomX(), self.getLeftBottomY(), olx, oly)
        return self

    def setOriginFixedOrigin(self, x: float, y: float)->'MyShape':
        ox = self._originX
        oy = self._originY
        olx = self.getLeftBottomX()
        oly = self.getLeftBottomY()
        v0 = Vector2(self.getLeftBottomOriginX() + self.getLeftBottomX(),
                     self.getLeftBottomOriginY() + self.getLeftBottomY())
        self.setOrigin(x, y)
        self.calculateCenterXY()
        v1 = Vector2(self.getLeftBottomOriginX() + self.getLeftBottomX(),
                     self.getLeftBottomOriginY() + self.getLeftBottomY())
        v0 = v0.__sub__(v1)
        self._centerX += v0.x
        self._centerY += v0.y
        self.calculateCenterXY()
        self.originChanged(self._originX, self._originY, ox, oy)
        self.positionChanged(self.getLeftBottomX(), self.getLeftBottomY(), olx, oly)
        return self

    def getOffsetRotation(self) -> float:
        return self._offsetRotation

    def setOffsetRotation(self, offsetRotation: float)->'MyShape':
        self._offsetRotation = offsetRotation
        self.calculateCenterXY()
        return self

    def offsetRotateBy(self, degree: float):
        self._offsetRotation += degree
        self.calculateCenterXY()

    def getRealRotation(self) -> float:
        return self._realRotation

    def getOriginX(self) -> float:
        return self._originX

    def setOriginX(self, originX: float)->'MyShape':
        self.setOrigin(originX, self._originY)
        return self

    def getOriginY(self) -> float:
        return self._originY

    def setOriginY(self, originY: float)->'MyShape':
        self.setOrigin(self._originX, originY)
        return self

    def getLeftBottomOriginY(self) -> float:
        return self._originY + self._offsetY + self._height / 2.0

    def getLeftBottomOriginX(self) -> float:
        return self._originX + self._offsetX + self._width / 2.0

    def getLeftBottomY(self) -> float:
        return self._originY + self._offsetY + self._centerY - (self._height + self._originY * 2.0) / 2.0

    def getLeftBottomX(self) -> float:
        return self._originX + self._offsetX + self._centerX - (self._width + self._originX * 2.0) / 2.0

    def setWidth(self, width: float)->'MyShape':
        self.setSize(width, self._height)
        return self

    def setHeight(self, height: float)->'MyShape':
        self.setSize(self._width, height)
        return self

    def setOffsetX(self, offsetX: float)->'MyShape':
        self.setOffset(offsetX, self._offsetY)
        return self

    def setOffsetY(self, offsetY: float)->'MyShape':
        self.setOffset(self._offsetX, offsetY)
        return self

    def setCenter(self, cx: float, cy: float)->'MyShape':
        x = self.getLeftBottomX()
        y = self.getLeftBottomY()
        self._centerX = cx
        self._centerY = cy
        self.calculateCenterXY()
        self.positionChanged(self.getLeftBottomX(), self.getLeftBottomY(), x, y)
        return self

    def setCenterX(self, centerX: float)->'MyShape':
        self.setCenter(centerX, self._centerY)
        return self

    def setCenterY(self, centerY: float)->'MyShape':
        self.setCenter(self._centerX, centerY)
        return self

    def __str__(self) -> str:
        vector2s = self.getCorners()
        corners = ""
        if vector2s != None:
            x = 1
            for v in vector2s:
                corners += "\n(X" + x + "=" + round(v._x * 100.0) / 100.0 + " Y" + x + "=" + round(
                    v._y * 100.0) / 100.0 + ")"
        return "MyShape{" + "realCenterX=" + str(self._realCenterX) + ", realCenterY=" + str(
            self._realCenterY) + ", realRotation=" + str(self._realRotation) + ", width=" + str(
            self._width) + ", height=" + str(self._height) + ", rotation=" + str(
            self._rotation) + ", offsetRotation=" + str(self._offsetRotation) + ", offsetX=" + str(
            self._offsetX) + ", offsetY=" + str(self._offsetY) + ", centerX=" + str(self._centerX) + ", centerY=" + str(
            self._centerY) + ", originX=" + str(self._originX) + ", originY=" + str(self._originY)

    def getUserData(self) -> object:
        return self._userData

    def setUserData(self, extraData: object)->'MyShape':
        self._userData = extraData
        return self

    def isActive(self) -> bool:
        return self._active

    def setActive(self, active: bool)->'MyShape':
        self._active = active
        return self

    def originChanged(self, newX: float, newY: float, oldX: float, oldY: float):
        pass

    def positionChanged(self, newX: float, newY: float, oldX: float, oldY: float):
        pass

    def sizeChanged(self, newW: float, newH: float, oldW: float, oldH: float):
        pass

    def rotationChanged(self, newR: float, oldR: float):
        pass

    def getRealRadius(self):
        return self.realRadius

    def getActive(self):
        return self._active

    def getShapeType(self):
        return self._shapeType

    shapeType = property(getShapeType)
    realCenterX: float = property(getRealCenterX)
    realCenterY: float = property(getRealCenterY)
    realRadius: float = property(getRealRadius)
    realRotation: float = property(getRealRotation)
    width: float = property(getWidth, setWidth)
    height: float = property(getHeight, setHeight)
    rotation: float = property(getRotation, setRotation)
    offsetRotation: float = property(getOffsetRotation, setOffsetRotation)
    offsetX: float = property(getOffsetX, setOffsetX)
    offsetY: float = property(getOffsetY, setOffsetY)
    centerX: float = property(getCenterX, setCenterX)
    centerY: float = property(getCenterY, setCenterY)
    originX: float = property(getOriginX, setOriginX)
    originY: float = property(getOriginY, setOriginY)
    active: bool = property(getActive, setActive)
    userData = property(getUserData, setUserData)
