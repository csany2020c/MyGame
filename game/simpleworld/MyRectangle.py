from game.simpleworld.MyShape import *

"""
 * Created by tanulo on 2017. 12. 13..
 """

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
                         alignToLeftBottom)

    def getCorners(self)->[]:
        vector2 = [];
        w2 = self.width/2;
        h2 = self.height/2;
        radius = math.sqrt(h2*h2 + w2*w2)
        radrot = math.radians(self.realRotation)
        angle = math.asin(h2 / radius)
        vector2.append(Vector2(self.realCenterX + radius * math.cos(radrot - angle), self.realCenterY + radius * math.sin(radrot - angle)))
        vector2.append(Vector2(self.realCenterX + radius * math.cos(radrot + angle),  self.realCenterY + radius * math.sin(radrot + angle)))
        vector2.append(Vector2(self.realCenterX + radius * math.cos(radrot + self.PI - angle),  self.realCenterY + radius * math.sin(radrot + self.PI - angle)))
        vector2.append(Vector2(self.realCenterX + radius * math.cos(radrot + self.PI + angle),  self.realCenterY + radius * math.sin(radrot + self.PI + angle)))

    def overlaps(self, rectangle:'MyRectangle', circle:'MyCircle')->bool:
        if ((rectangle.realCenterX - objB.realCenterX) * (rectangle.realCenterX - objB.realCenterX) +
                (rectangle.realCenterY - objB.realCenterY) * (rectangle.realCenterY - objB.realCenterY) >
                (rectangle.realRadius + objB.realRadius) * (rectangle.realRadius + objB.realRadius)):
            return False

        #Téglalap és kör forgatása a téglalap originje körül úgy, hogy az oldalai párhuzamosak legyenek a koordináta rendszerrel. A kör középpontja megváltozik, a téglalap forgatása 0 lesz.
        circleRotCenter = Vector2(circle.realCenterX-rectangle.realCenterX, circle.realCenterY-rectangle.realCenterY).rotate(-rectangle.rotation - rectangle.offsetRotation).add(rectangle.realCenterX,rectangle.realCenterY)

        //A négyzet sarkai
        float xRect[] = new float[4];
        float yRect[] = new float[4];

        //A méret fele (gyorsítás)
        float height1 = rectangle.height / 2;
        float width1 = rectangle.width / 2;

        //Forgatás nélküli sarkok
        //Bal alsó
        xRect[0] = rectangle.realCenterX - width1;
        yRect[0] = rectangle.realCenterY - height1;

        //Bal felső
        xRect[1] = rectangle.realCenterX - width1;
        yRect[1] = rectangle.realCenterY + height1;


        //Jobb felső
        xRect[2] = rectangle.realCenterX + width1;
        yRect[2] = rectangle.realCenterY + height1;


        //Jobb alső
        xRect[3] = rectangle.realCenterX + width1;
        yRect[3] = rectangle.realCenterY - height1;

        //Ha a téglalap bármely sarka a körön beül van
        for (int i = 0; i < 4; i++) {
            if ((xRect[i] - circleRotCenter.x) * (xRect[i] - circleRotCenter.x) +
                    (yRect[i] - circleRotCenter.y) * (yRect[i] - circleRotCenter.y) <=
                    (circle.radius) * (circle.radius)){
                return true;
            }
        }

        //Elforgatott kör koordinátái
        float xCirc[] = new float[4];
        float yCirc[] = new float[4];

        // A kör legfelső pontja
        xCirc[0] = circleRotCenter.x + circle.radius;
        yCirc[0] = circleRotCenter.y;

        // legalsó pontja
        xCirc[1] = circleRotCenter.x - circle.radius;
        yCirc[1] = circleRotCenter.y;

        // bal pontja
        xCirc[2] = circleRotCenter.x;
        yCirc[2] = circleRotCenter.y - circle.radius;

        // jobb pontja
        xCirc[3] = circleRotCenter.x;
        yCirc[3] = circleRotCenter.y + circle.radius;


        //Ha a kör bármelyik (bal, jobb, felső, alsó) pontja a téglalapon belül van
        for (int i = 0; i < 4; i++) {
            if (xRect[0] <= xCirc[i] && xRect[2] >= xCirc[i] && yRect[0] <= yCirc[i] && yRect[2] >= yCirc[i]) {
                return true;
            }
        }
        return false;
    }

    //https://forums.coronalabs.com/topic/39094-code-for-rotated-rectangle-collision-detection/
    public static boolean overlaps(MyRectangle objA, MyRectangle objB) {

        if ((objA.realCenterX - objB.realCenterX) * (objA.realCenterX - objB.realCenterX) +
                (objA.realCenterY - objB.realCenterY) * (objA.realCenterY - objB.realCenterY) >
                (objA.realRadius + objB.realRadius) * (objA.realRadius + objB.realRadius)){
            return false;
        }


        //x10, y10 is centre point of rect1. x20, y20 is centre point of rect2
        //height1, width1 are half heights/widths of rect1, radrot is rotation of rect in radians

        float height1 = objA.height / 2;
        float height2 = objB.height / 2;

        float width1 = objA.width / 2;
        float width2 = objB.width / 2;

        float radrot1 = (float) Math.toRadians(objA.realRotation);
        float radrot2 = (float) Math.toRadians(objB.realRotation);

        float radius1 = (float) Math.sqrt(height1 * height1 + width1 * width1);
        float radius2 = (float) Math.sqrt(height2 * height2 + width2 * width2);

        float angle1 = (float) Math.asin(height1 / radius1);
        float angle2 = (float) Math.asin(height2 / radius2);

        float x1[] = new float[5];
        float y1[] = new float[5];
        float x2[] = new float[5];
        float y2[] = new float[5];

        x1[1] = objA.realCenterX + radius1 * (float) Math.cos(radrot1 - angle1);
        y1[1] = objA.realCenterY + radius1 * (float) Math.sin(radrot1 - angle1);
        x1[2] = objA.realCenterX + radius1 * (float) Math.cos(radrot1 + angle1);
        y1[2] = objA.realCenterY + radius1 * (float) Math.sin(radrot1 + angle1);
        x1[3] = objA.realCenterX + radius1 * (float) Math.cos(radrot1 + PI - angle1);
        y1[3] = objA.realCenterY + radius1 * (float) Math.sin(radrot1 + PI - angle1);
        x1[4] = objA.realCenterX + radius1 * (float) Math.cos(radrot1 + PI + angle1);
        y1[4] = objA.realCenterY + radius1 * (float) Math.sin(radrot1 + PI + angle1);

        x2[1] = objB.realCenterX + radius2 * (float) Math.cos(radrot2 - angle2);
        y2[1] = objB.realCenterY + radius2 * (float) Math.sin(radrot2 - angle2);
        x2[2] = objB.realCenterX + radius2 * (float) Math.cos(radrot2 + angle2);
        y2[2] = objB.realCenterY + radius2 * (float) Math.sin(radrot2 + angle2);
        x2[3] = objB.realCenterX + radius2 * (float) Math.cos(radrot2 + PI - angle2);
        y2[3] = objB.realCenterY + radius2 * (float) Math.sin(radrot2 + PI - angle2);
        x2[4] = objB.realCenterX + radius2 * (float) Math.cos(radrot2 + PI + angle2);
        y2[4] = objB.realCenterY + radius2 * (float) Math.sin(radrot2 + PI + angle2);

        float[] axisx = new float[5];
        float[] axisy = new float[5];

        axisx[1] = x1[1] - x1[2];
        axisy[1] = y1[1] - y1[2];
        axisx[2] = x1[3] - x1[2];
        axisy[2] = y1[3] - y1[2];

        axisx[3] = x2[1] - x2[2];
        axisy[3] = y2[1] - y2[2];
        axisx[4] = x2[3] - x2[2];
        axisy[4] = y2[3] - y2[2];

        for (int k = 1; k <= 4; k++) {

            float proj = x1[1] * axisx[k] + y1[1] * axisy[k];

            float minProj1 = proj;
            float maxProj1 = proj;

            for (int i = 2; i <= 4; i++) {
                proj = x1[i] * axisx[k] + y1[i] * axisy[k];

                if (proj < minProj1) {
                    minProj1 = proj;
                } else if (proj > maxProj1) {
                    maxProj1 = proj;
                }
            }

            proj = x2[1] * axisx[k] + y2[1] * axisy[k];

            float minProj2 = proj;
            float maxProj2 = proj;

            for (int j = 2; j <= 4; j++) {
                proj = x2[j] * axisx[k] + y2[j] * axisy[k];
                if (proj < minProj2) {
                    minProj2 = proj;
                } else if (proj > maxProj2) {
                    maxProj2 = proj;
                }
            }
            if (maxProj2 < minProj1 || maxProj1 < minProj2) {
                return false;
            }
        }
        return true;
    }

    public boolean overlaps(MyShape other) {
        if (other instanceof MyRectangle){
            return overlaps(this, (MyRectangle)other);
        }
        if (other instanceof MyCircle){
            return overlaps(this, (MyCircle)other);
        }
        return false;
    }
}

