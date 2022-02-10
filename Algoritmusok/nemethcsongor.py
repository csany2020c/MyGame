import math

def binaris(bemenet: int) -> str:
    b: str = ''
    while bemenet > 0:
        if bemenet % 2 == 0:
            bemenet = bemenet // 2
            b = '0' + b
        else:
            bemenet = bemenet // 2
            b = '1' + b
    return b


szam = 65845344
if szam % 3 == 0:
    k: str = ", osztható hárommal"
else:
    k: str = ", nem osztható hárommal"
if szam % 2 == 0:
    g: str = "  és páros"
else:
    g: str = " és páratlan"
print("A " + str(szam) + " bináris értéke " + str(binaris(szam) + str(k) + str(g) + " ."))

def prim():
    gyok: int = int(math.sqrt(szam))
        for i in range(2, gyok):
            if szam % i == 0:
                return False
        return True