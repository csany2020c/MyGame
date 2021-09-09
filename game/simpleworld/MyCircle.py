from game.simpleworld.MyShape import *


class MyCircle(MyShape):

    debugLineNumbers: int = 16

    def __init__(self, x: float = 0, y: float = 0, radius: float = 1, rotation: float = 0,
                 offsetRotation: float = 0, originX: float = 0.5, originY: float = 0.5, offsetX: float = 0,
                 offsetY: float = 0, alignToLeftBottom: bool = True):
        super().__init__(x, y, radius / 2, radius / 2, rotation, offsetRotation, originX, originY, offsetX, offsetY,
                         alignToLeftBottom)
        self.radius = radius

    def getCorners(self)->[]:
        vector2s = []
        for i in range(self.debugLineNumbers):
            v = Vector2(self.radius, 0).rotate(360.0 / self.debugLineNumbers * i + self.rotation).__add__(Vector2(self.realCenterX, self.realCenterY))
            v.rotate(360.0 / self.debugLineNumbers * i + self.rotation)
        return vector2s

    @staticmethod
    def overlaps(objA: 'MyCircle', objB: 'MyCircle')->bool:
        return (objA.realCenterX - objB.realCenterX) * (objA.realCenterX - objB.realCenterX) + (objA.realCenterY - objB.realCenterY) * (objA.realCenterY - objB.realCenterY) <= (objA.radius + objB.radius) * (objA.radius + objB.radius);

    @staticmethod
    def overlaps(objA:'MyCircle', objB:'MyRectangle')->bool:
        return 'MyRectangle'.overlaps(objB, objA)

    # def overlaps(self, other:MyShape):
    #     if isinstance (other, MyCircle):
    #         return overlaps(self, MyCircle(other))
    #     if isinstance (other, MyRectangle):
    #         return MyRectangle.overlaps(MyRectangle(other), self)
    #     return false

    def setSize(self, width: float, height: float):
        if width < height:
            self.radius = width / 2.0
        else:
            height / 2.0
        super.setSize(width, height)

    def getRadius(self)->float:
        return self.radius

    def setRadius(self, radius: float):
        self.radius = radius
        super.setSize(radius * 2.0, radius * 2.0)

