from game.simpleworld.MyShape import *

class MyCircle(MyShape):

    debugLineNumbers: int = 16

    # """
    # @param radius A kör sugara
    #  """
    #
    # @overload
    # def __init__(self, radius: float):
    #     super().__init__(0, 0, radius, radius, 0, 0, 0, 0, 0, 0, True)
    #     self.radius = radius
    #
    #
    # """
    # @param offsetX Eltolás az X koordinátától
    # @param offsetY Eltolás az Y koordinátától
    # @param radius A kör sugara
    #  """
    #
    # @typing.overload
    # def __init__(self, radius: float, offsetX: float, offsetY:float):
    #     super().__init__(0, 0, radius*2, radius*2, 0, 0,0, 0, offsetX, offsetY, True)
    #     self.radius = radius
    #
    #
    # """
    # @param originX A forgatás középpontja
    # @param originY A forgatás középpontja
    # @param offsetX Eltolás az X koordinátától
    # @param offsetY Eltolás az Y koordinátától
    #  """
    #
    # @typing.overload
    # def __init__(self, radius:float, offsetX:float, offsetY:float, originX:float, originY:float):
    #     super().__init__(0, 0, radius*2, radius*2, 0, 0, originX, originY, offsetX, offsetY, True)
    #     self.radius = radius
    #
    #
    # """
    # @param x Az alakzat helye
    # @param y Az alakzat helye
    # @param originX A forgatás középpontja
    # @param originY A forgatás középpontja
    # @param offsetX Eltolás az X koordinátától
    # @param offsetY Eltolás az Y koordinátától
    # @param radius A kör sugara
    #  """
    #
    # @typing.overload
    # def __init__(self, radius:float, offsetX:float, offsetY:float, originX:float, originY:float, x:float, y:float):
    #     super().__init__(x, y, radius*2, radius*2, 0, 0, originX, originY, offsetX, offsetY, True)
    #     self.radius = radius
    #
    #
    # """
    # @param alignToLeftBottom Igaz esetén az alakzatot a bal alsó sarkától számított X és Y koordinátákkal hozza létre, ellenkező esetben a küzepétől.
    # @param radius A kör sugara
    #  """
    #
    # @typing.overload
    # def __init__(self, radius:float, alignToLeftBottom: bool):
    #     super().__init__(0, 0, radius*2, radius*2, 0, 0, 0, 0, 0, 0, alignToLeftBottom)
    #     self.radius = radius
    #
    # """
    # @param offsetX Eltolás az X koordinátától
    # @param offsetY Eltolás az Y koordinátától
    # @param alignToLeftBottom Igaz esetén az alakzatot a bal alsó sarkától számított X és Y koordinátákkal hozza létre, ellenkező esetben a küzepétől.
    # @param radius A kör sugara
    #  """
    #
    # @typing.overload
    # def __init__(self, radius:float, offsetX:float, offsetY:float, alignToLeftBottom: bool):
    #     super().__init__(0, 0, radius*2, radius*2, 0, 0,0, 0, offsetX, offsetY, alignToLeftBottom)
    #     self.radius = radius
    #
    # """
    # @param originX A forgatás középpontja
    # @param originY A forgatás középpontja
    # @param offsetX Eltolás az X koordinátától
    # @param offsetY Eltolás az Y koordinátától
    # @param alignToLeftBottom Igaz esetén az alakzatot a bal alsó sarkától számított X és Y koordinátákkal hozza létre, ellenkező esetben a küzepétől.
    # @param radius A kör sugara
    #  """
    #
    # @typing.overload
    # def __init__(self, radius: float, offsetX: float, offsetY: float, originX: float, originY: float, alignToLeftBottom: bool):
    #     super().__init__(0, 0, radius*2, radius*2, 0, 0, originX, originY, offsetX, offsetY, alignToLeftBottom)
    #     self.radius = radius
    #
    # """
    # @param x Az alakzat helye
    # @param y Az alakzat helye
    # @param originX A forgatás középpontja
    # @param originY A forgatás középpontja
    # @param offsetX Eltolás az X koordinátától
    # @param offsetY Eltolás az Y koordinátától
    # @param alignToLeftBottom Igaz esetén az alakzatot a bal alsó sarkától számított X és Y koordinátákkal hozza létre, ellenkező esetben a küzepétől.
    # @param radius A kör sugara
    #  """
    #
    # @typing.overload
    # def __init__(self, x: float, y: float, radius: float, offsetX: float, offsetY: float, originX: float, originY: float, alignToLeftBottom: bool):
    #     super().__init__(x, y, radius*2, radius*2, 0, 0, originX, originY, offsetX, offsetY, alignToLeftBottom)
    #     self.radius = radius
    #
    # """
    # @param y Az alakzat helye
    # @param rotation Az alakzat forgatása az origin körül
    # @param offsetRotation Az alakzat forgatása saját maga körül
    # @param originX A forgatás középpontja
    # @param originY A forgatás középpontja
    # @param offsetX Eltolás az X koordinátától
    # @param offsetY Eltolás az Y koordinátától
    # @param alignToLeftBottom Igaz esetén az alakzatot a bal alsó sarkától számított X és Y koordinátákkal hozza létre, ellenkező esetben a küzepétől.
    #  """

    # @typing.overload
    # def __int__(self, x: float, y: float, radius: float, offsetX: float, offsetY: float, originX: float, originY: float,  rotation: float, offsetRotation: float, alignToLeftBottom: bool):
    #     super().__init__(x, y, radius*2, radius*2, rotation, offsetRotation, originX, originY, offsetX, offsetY, alignToLeftBottom)
    #     self.radius = radius

    # """
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
    #  """
    # @typing.overload
    # def __init__(self, x: float, y: float, width: float, height: float, rotation: float, offsetRotation: float,
    #              originX: float, originY: float, offsetX: float, offsetY: float, alignToLeftBottom: bool):
    #     super().__init__(x, y, width, height, rotation, offsetRotation, originX, originY, offsetX, offsetY,
    #                      alignToLeftBottom)
    #     if width < height:
    #         self.radius = width / 2.0
    #     else:
    #         height / 2.0

    def __int__(self, x: float=0, y: float=0, radius: float = 1, offsetX: float=0, offsetY: float=0, originX: float=0, originY: float=0, rotation: float=0, offsetRotation: float=0, alignToLeftBottom: bool=True):
        super().__init__(x, y, radius*2, radius*2, rotation, offsetRotation, originX, originY, offsetX, offsetY, alignToLeftBottom)
        self.radius = radius



    def getCorners(self)->[]:
        vector2s = []
        for i in range(self.debugLineNumbers):
            vector2s[i] = Vector2(self.radius, 0)
            vector2s[i].rotate(360.0 / self.debugLineNumbers * i + self.rotation)
            vector2s[i].add(self.realCenterX, self.realCenterY)
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

