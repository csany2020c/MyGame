import abc
from pygame.math import Vector2
import math


class MyShape(metaclass=abc.ABCMeta):

    def __init__(self, x:float=0, y: float=0, width: float=1, height: float=1, rotation: float=0, offsetRotation: float=0, originX: float=0.5, originY: float=0.5, offsetX: float=0, offsetY: float=0, alignToLeftBottom: bool=True):
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
        self.realCenterX: float = 0

     # 
     # Tényleges középpont. Ez alapján számolja a pozícióját. center=cx+offsetx forgatva origin körül
     #
        self.realCenterY: float = 0

     # 
     # A szélességből és magasságból számított, körülvevő kür sugara
     #
        self.realRadius: float = 0


     # 
     # Tényleges forgatás. A offsetRotation forgatás és az elforgatás összege.
     #
        self.realRotation: float = 0


     # 
     # Szélesség. Forgatásnál nem változik.
     #
        self.width: float = 0

     # 
     # Magasság. Forgatásnál nem változik.
     #
        self.height: float = 0

     # 
     # Forgatás fokban megadva.
     #
        self.rotation: float = 0

     # 
     # Relatív elforgatás. realRotation=offsetRotation+rotation
     #
        self.offsetRotation: float = 0

     # 
     # Relatív eltolás cx-től számítva. center=cx+offsetx
     #
        self.offsetX: float = 0

     # 
     # Relatív eltolás cy-tól számítva. center=cy+offsety
     #
        self.offsetY=0

     # 
     # A középpont abszolút pozíciója a játéktérben.
     #
        self.centerX: float =0

     # 
     # A középpont abszolút pozíciója a játéktérben.
     #
        self.centerY: float =0

     # 
     # A forgatás középpontja. Relatív a valódi helyétől (offsetxy+cxy) az alakzatnak.
     #
        self.originX: float = 0

     # 
     # A forgatás középpontja. Relatív a valódi helyétől (offsetxy+cxy) az alakzatnak.
     #
        self.originY: float = 0

        self.PI: float = 3.141592653589793238462643383279502884197169399375105820974944592307816406286

        self.active: bool = True

        # Az alakzathoz hozzácsatolható objektum, például egy Actor
        self.userData = None

        self.offsetX = offsetX
        self.offsetY = offsetY
        self.width = width
        self.height = height
        self.offsetRotation = offsetRotation
        self.rotation = rotation
        if alignToLeftBottom:
            self.setPosition(x, y)
            self.setOrigin(originX, originY)
        else:
            self.setPositionFromCenter(x, y)
            self.setOriginFromCenter(originX, originY)


    @abc.abstractmethod
    def getCorners(self)->[]:
        pass

    @abc.abstractmethod
    def overlaps(self, other: 'MyShape')->bool:
        pass

    def setSizeByCenter(self, width: float, height: float):
        olx = self.getLeftBottomX()
        oly = self.getLeftBottomY()
        oldW = self.width
        oldH = self.height
        oldOriginX = self.originX
        oldOriginY = self.originY
        orcx = self.realCenterX
        orcy = self.self.realCenterY

        self.originX = self.originX / self.width * width
        self.originY = self.originY / self.height * height
        self.width = width
        self.height = height
        self.calculateCenterXY()
        self.centerX += orcx - self.realCenterX
        self.centerY += orcy - self.realCenterY
        self.calculateCenterXY()

        self.sizeChanged(width, height, oldW, oldH)
        self.positionChanged(self.getLeftBottomX(), self.getLeftBottomY(), olx, oly)

    def setSize(self, width: float, height: float):
        olx = self.getLeftBottomX()
        oly = self.getLeftBottomY()
        oldOriginX = self.originX
        oldOriginY = self.originY
        oldW = self.width
        oldH = self.height

        self.originX = self.originX / self.width * width
        self.originY = self.originY / self.height * height
        self.centerX -= (self.width - width) / 2
        self.centerY -= (self.height - height) / 2
        self.width = width
        self.height = height
        self.calculateCenterXY()

        self.sizeChanged(width, height, oldW, oldH)
        self.positionChanged(self.getLeftBottomX(), self.getLeftBottomY(), olx, oly)

    def setSizeByOrigin(self, width: float, height: float):
        olx = self.getLeftBottomX()
        oly = self.getLeftBottomY()
        oldOriginX = self.originX
        oldOriginY = self.originY
        oldW = self.width
        oldH = self.height

        self.originX = self.originX / self.width * width
        self.originY = self.originY / self.height * height
        self.centerX -= self.originX - oldOriginX
        self.centerY -= self.originY - oldOriginY
        self.width = width
        self.height = height
        self.calculateCenterXY()

        self.sizeChanged(width, height, oldW, oldH)
        self.positionChanged(self.getLeftBottomX(), self.getLeftBottomY(), olx, oly)

    def calculateCenterXY(self):
        self.realRotation = self.rotation + self.offsetRotation
        origCenter = Vector2(self.centerX + self.offsetX, self.centerY + self.offsetY)
        origin =  Vector2(self.originX + self.centerX + self.offsetX,self.originY + self.centerY + self.offsetY)
        v = origCenter.__sub__(origin)
        v.rotate(self.rotation)
        s = v.__add__(origin)
        self.realCenterX = s.x
        self.realCenterY = s.y
        self.realRadius = math.sqrt(self.width * self.width + self.height * self.height) / 2.0

    def setPosition(self, X: float, Y: float):
        olx = self.getLeftBottomX()
        oly = self.getLeftBottomY()
        self.centerX = X + self.width/2.0
        self.centerY = Y + self.height/2.0
        self.calculateCenterXY()
        self.positionChanged(self.getLeftBottomX(), self.getLeftBottomY(), olx, oly)

    def setX(self, x: float):
        self.setPosition(x,self.getLeftBottomY())

    def setY(self, y: float):
        self.setPosition(self.getLeftBottomX(),y)

    def setPositionFromCenter(self, centerX: float, centerY: float):
        olx = self.getLeftBottomX()
        oly = self.getLeftBottomY()
        self.centerX = centerX
        self.centerY = centerY
        self.calculateCenterXY()
        self.positionChanged(self.getLeftBottomX(), self.getLeftBottomY(), olx, oly)

    # def setOffset(float offsetX, float offsetY){
    #     float olx = getLeftBottomX()
    #     float oly = getLeftBottomY()
    #     self.offsetX = offsetX
    #     self.offsetY = offsetY
    #     calculateCenterXY()
    #     positionChanged(getLeftBottomX(), getLeftBottomY(), olx, oly)
    # }

    # def rotateBy(float degree) {
    #     setRotation(rotation + degree)
    # }
    #
    # def setRotation(float degree) {
    #     float or = rotation
    #     rotation = degree
    #     calculateCenterXY()
    #     rotationChanged(rotation, or)
    # }
    #
    # public float getRealCenterX() {
    #     return realCenterX
    # }
    #
    # public float getRealCenterY() {
    #     return realCenterY
    # }
    #
    # public float getWidth() {
    #     return width
    # }
    #
    # public float getHeight() {
    #     return height
    # }
    #
    # public float getRotation() {
    #     return rotation
    # }
    #
    # public float getOffsetX() {
    #     return offsetX
    # }
    #
    # public float getOffsetY() {
    #     return offsetY
    # }
    #
    # public float getCenterX() {
    #     return centerX
    # }
    #
    # public float getCenterY() {
    #     return centerY
    # }
    #
    # public float getX() {
    #     return realCenterX - width/2
    # }
    #
    # public float getY() {
    #     return realCenterY - height/2
    # }


    def setOriginToCenter(self):
        ox: float = self.originX
        oy: float = self.originY
        self.originX = 0
        self.originY = 0
        self.calculateCenterXY()
        self.originChanged(self.originX, self.originY, ox, oy)


     #
     # Forgatási középpont beállítása a középponttól számítva
     # @param x
     # @param y
     #
    def setOriginFromCenter(self, x: float, y: float):
        ox = self.originX
        oy = self.originY
        self.originX = x - self.offsetX
        self.originY = y - self.offsetY
        self.calculateCenterXY()
        self.originChanged(self.originX, self.originY, ox, oy)


     # 
     # Forgatási középpont beállítása a bal alsó saroktól mérve.
     # @param x
     # @param y
     #
    def setOrigin(self, x: float, y: float):
        ox = self.originX
        oy = self.originY
        self.originX = x - self.width / 2 - self.offsetX
        self.originY = y - self.height / 2 - self.offsetY
        self.calculateCenterXY()
        self.originChanged(self.originX, self.originY, ox, oy)

    def setOriginFixedPositionAbsolute(self, x: float, y: float):
        self.setOriginFixedPosition(x - self.getLeftBottomX(),y - self.getLeftBottomY())

    def setOriginFixedPosition(self, x: float, y: float):
        ox = self.originX
        oy = self.originY
        olx = self.getLeftBottomX()
        oly = self.getLeftBottomY()
        v0 = Vector2(self.realCenterX,self.realCenterY)
        self.setOrigin(x,y)
        self.calculateCenterXY()
        v1 = Vector2(self.realCenterX, self.realCenterY)
        v0 = v0.__sub__(v1)
        self.centerX += v0.x
        self.centerY += v0.y
        self.calculateCenterXY()
        self.originChanged(self.originX, self.originY, ox, oy)
        self.positionChanged(self.getLeftBottomX(), self.getLeftBottomY(), olx, oly)

    def setOriginFixedOrigin(self, x: float, y: float):
        ox = self.originX
        oy = self.originY
        olx = self.getLeftBottomX()
        oly = self.getLeftBottomY()
        v0 = Vector2(self.getLeftBottomOriginX() + self.getLeftBottomX(), self.getLeftBottomOriginY() + self.getLeftBottomY())
        self.setOrigin(x,y)
        self.calculateCenterXY()
        v1 = Vector2(self.getLeftBottomOriginX() + self.getLeftBottomX(), self.getLeftBottomOriginY() + self.getLeftBottomY())
        v0 = v0.__sub__(v1)
        self.centerX += v0.x
        self.centerY += v0.y
        self.calculateCenterXY()
        self.originChanged(self.originX, self.originY, ox, oy)
        self.positionChanged(self.getLeftBottomX(), self.getLeftBottomY(), olx, oly)


    def getOffsetRotation(self) -> float:
        return self.offsetRotation


    def setOffsetRotation(self, offsetRotation: float):
        self.offsetRotation = offsetRotation
        self.calculateCenterXY()

    def offsetRotateBy(self, degree: float):
        self.offsetRotation += degree
        self.calculateCenterXY()

    def getRealRotation(self)-> float:
        return self.realRotation

    def getOriginX(self)->float:
        return self.originX

    def setOriginX(self, originX: float):
        self.setOrigin(originX, self.originY)

    def getOriginY(self)->float:
        return self.originY

    def setOriginY(self, originY: float):
        self.setOrigin(self.originX, originY)

    def getLeftBottomOriginY(self)->float:
        return self.originY + self.offsetY  + self.height / 2.0

    def getLeftBottomOriginX(self)->float:
        return self.originX + self.offsetX + self.width / 2.0

    def getLeftBottomY(self)->float:
        return self.originY + self.offsetY + self.centerY - (self.height + self.originY * 2.0) / 2.0

    def getLeftBottomX(self)->float:
        return self.originX + self.offsetX + self.centerX - (self.width + self.originX * 2.0) / 2.0

    def setWidth(self, width: float):
        self.setSize(width, self.height)

    def setHeight(self, height: float):
        self.setSize(self.width, height)

    def setOffsetX(self, offsetX: float):
        self.setOffset(offsetX, self.offsetY)

    def setOffsetY(self, offsetY: float):
        self.setOffset(self.offsetX, offsetY)

    def setCenter(self, cx: float, cy: float):
        x = self.getLeftBottomX()
        y = self.getLeftBottomY()
        self.centerX = cx
        self.centerY = cy
        self.calculateCenterXY()
        self.positionChanged( self.getLeftBottomX(), self.getLeftBottomY(), x,y)

    def setCenterX(self, centerX: float):
        self.setCenter(centerX, self.centerY)

    def setCenterY(self, centerY: float):
        self.setCenter(self.centerX, centerY)

    def __str__(self) -> str:
        vector2s = self.getCorners()
        corners = ""
        if vector2s != None:
            x = 1
            for v in vector2s:
                corners += "\n(X" + x + "=" + round(v.x*100.0) / 100.0 + " Y" + x + "=" + round(v.y*100.0) / 100.0 + ")"
        return "MyShape{" + "realCenterX=" + str(self.realCenterX) + ", realCenterY=" + str(self.realCenterY) + ", realRotation=" + str(self.realRotation) + ", width=" + str(self.width) + ", height=" + str(self.height) + ", rotation=" + str(self.rotation) + ", offsetRotation=" + str(self.offsetRotation) + ", offsetX=" + str(self.offsetX) + ", offsetY=" + str(self.offsetY) +                ", centerX=" + str(self.centerX) +                ", centerY=" + str(self.centerY) +                ", originX=" + str(self.originX) +                ", originY=" + str(self.originY)

    def getUserData(self)->object:
        return self.userData

    def setUserData(self, extraData: object):
        self.userData = extraData

    def isActive(self)->bool:
        return self.active

    def setActive(self, active: bool):
        self.active = active

    def originChanged(self, newX: float, newY: float, oldX: float, oldY: float):
        pass

    def positionChanged(self, newX: float, newY: float, oldX: float, oldY: float):
        pass

    def sizeChanged(self, newW: float, newH: float, oldW: float, oldH: float):
        pass

    def rotationChanged(self, newR: float, oldR: float):
        pass
