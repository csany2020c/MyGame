import math
from math import acos
from math import sqrt
from math import pi
class AngleCalc():
    def angle_between_points(self,target, gun):
        targetX = target[0]
        targetY = target[1]

        gunX = gun[0]
        gunY = gun[1]
        myradians = math.atan2(targetY-gunY, targetX-gunX)
        degree = math.degrees(myradians)
        print(degree)
        return degree


AngleCalc().angle_between_points((0,0),(90,30))