import abc
from pygame.math import Vector2
import math


class MyShape(metaclass=abc.ABCMeta):

    def __init__(self, x:float, y: float, width: float, height: float, rotation: float, offsetRotation: float, originX: float, originY: float, offsetX: float, offsetY: float, alignToLeftBottom: bool):
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

        self.originX = originX / self.width * width
        self.originY = originY / self.height * height
        self.centerX -= (self.width - width) / 2f
        self.centerY -= (self.height - height) / 2f
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
        self.centerX -= originX - oldOriginX
        self.centerY -= originY - oldOriginY
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
        self.centerX = X + self.width/2
        self.centerY = Y + self.height/2
        self.calculateCenterXY()
        self.positionChanged(self.getLeftBottomX(), self.getLeftBottomY(), olx, oly)

    def setX(self, x: float):
        self.setPosition(x,self.getLeftBottomY())

    def setY(self, y: float):
        self.setPosition(self.getLeftBottomX(),y)

    def setPositionFromCenter(self, centerX: float, centerY: float)
        olx = self.getLeftBottomX()
        oly = self.getLeftBottomY()
        self.centerX = centerX
        self.centerY = centerY
        self.calculateCenterXY()
        self.positionChanged(self.getLeftBottomX(), self.getLeftBottomY(), olx, oly)

    # public void setOffset(float offsetX, float offsetY){
    #     float olx = getLeftBottomX()
    #     float oly = getLeftBottomY()
    #     self.offsetX = offsetX
    #     self.offsetY = offsetY
    #     calculateCenterXY()
    #     positionChanged(getLeftBottomX(), getLeftBottomY(), olx, oly)
    # }

    # public void rotateBy(float degree) {
    #     setRotation(rotation + degree)
    # }
    #
    # public void setRotation(float degree) {
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
    }

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

    def setOriginFixedPositionAbsolute(self, x: float, y: float)
        self.setOriginFixedPosition(x - self.getLeftBottomX(),y - self.getLeftBottomY())

    public void setOriginFixedPosition(float x, float y){
        float ox = originX
        float oy = originY
        float olx = getLeftBottomX()
        float oly = getLeftBottomY()
        Vector2 v0 = new Vector2(realCenterX,realCenterY)
        setOrigin(x,y)
        calculateCenterXY()
        v0.sub(realCenterX, realCenterY)
        centerX += v0.x
        centerY += v0.y
        calculateCenterXY()
        originChanged(originX, originY, ox, oy)
        positionChanged(getLeftBottomX(), getLeftBottomY(), olx, oly)
    }


    public void setOriginFixedOrigin(float x, float y){
        float ox = originX
        float oy = originY
        float olx = getLeftBottomX()
        float oly = getLeftBottomY()
        Vector2 v0 = new Vector2(getLeftBottomOriginX() + getLeftBottomX(),getLeftBottomOriginY() + getLeftBottomY())
        setOrigin(x,y)
        calculateCenterXY()
        v0.sub(getLeftBottomOriginX() + getLeftBottomX(),getLeftBottomOriginY() + getLeftBottomY())
        centerX += v0.x
        centerY += v0.y
        calculateCenterXY()
        originChanged(originX, originY, ox, oy)
        positionChanged(getLeftBottomX(), getLeftBottomY(), olx, oly)
    }


    public float getOffsetRotation() {
        return offsetRotation
    }

    public void setOffsetRotation(float offsetRotation) {
        self.offsetRotation = offsetRotation
        calculateCenterXY()
    }

    public void offsetRotateBy(float degree) {
        self.offsetRotation += degree
        calculateCenterXY()
    }

    public float getRealRotation() {
        return realRotation
    }

    public float getOriginX() {
        return originX
    }

    public void setOriginX(float originX) {
        setOrigin(originX, originY)
    }

    public float getOriginY() {
        return originY
    }

    public void setOriginY(float originY) {
        setOrigin(originX, originY)
    }


    public float getLeftBottomOriginY() {
        return originY + offsetY  + height/2
    }


    public float getLeftBottomOriginX() {
        return originX + offsetX + width / 2
    }


    public float getLeftBottomY() {
        return originY + offsetY + centerY - (height + originY*2) / 2f
    }


    public float getLeftBottomX() {
        return originX + offsetX + centerX - (width + originX*2) / 2f
    }


    public void setWidth(float width) {
        setSize(width, height)
    }

    public void setHeight(float height) {
        setSize(width, height)
    }


    public void setOffsetX(float offsetX) {
        setOffset(offsetX, offsetY)
    }

    public void setOffsetY(float offsetY) {
        setOffset(offsetX, offsetY)
    }

    public void setCenter(float cx, float cy){
        float x = getLeftBottomX()
        float y = getLeftBottomY()
        self.centerX = cx
        self.centerY = cy
        calculateCenterXY()
        positionChanged( getLeftBottomX(), getLeftBottomY(), x,y)
    }

    public void setCenterX(float centerX) {
        setCenter(centerX, centerY)
    }

    public void setCenterY(float centerY) {
        setCenter(centerX, centerY)
    }

    @Override
    public String toString() {
        Vector2[] vector2s = getCorners()
        String corners = ""
        if (vector2s != null) {
            int x = 1
            for (Vector2 v : vector2s) {
                corners += "\n(X" + x + "=" + Math.round(v.x*100.0f)/100.0f + " Y" + x + "=" + Math.round(v.y*100.0f)/100.0f + ")"
            }
        }
        return "MyShape{" +
                "realCenterX=" + realCenterX +
                ", realCenterY=" + realCenterY +
                ", realRotation=" + realRotation +
                ", width=" + width +
                ", height=" + height +
                ", rotation=" + rotation +
                ", offsetRotation=" + offsetRotation +
                ", offsetX=" + offsetX +
                ", offsetY=" + offsetY +
                ", centerX=" + centerX +
                ", centerY=" + centerY +
                ", originX=" + originX +
                ", originY=" + originY
    }

    public Object getUserData() {
        return userData
    }

    public void setUserData(Object extraData) {
        self.userData = extraData
    }

    @Deprecated
    public void setExtraData(Object userData) {
        self.userData = userData
    }

    @Deprecated
    public Object getExtraData() {
        return userData
    }

    public boolean isActive() {
        return active
    }

    public void setActive(boolean active) {
        self.active = active
    }

    protected void originChanged(float newX, float newY, float oldX, float oldY){}
    protected void positionChanged(float newX, float newY, float oldX, float oldY) {}
    protected void sizeChanged(float newW, float newH, float oldW, float oldH) {}
    protected void rotationChanged(float newR, float oldR) {}

