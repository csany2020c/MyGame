import math


class Algorythm:
    def __init__(self) -> None:
        super().__init__()
        szam:str = input()
        intszam:int = int(szam)
        logszam: int = int(math.log2(intszam) + 1)
        max: int = int(math.pow(2, logszam))
        print(max)
        vege: str = str()
        for i in range(logszam):
            max = int(max/2)
            if (max <= intszam):
                vege += "1"
                intszam -= max
            else:
                vege += "0"
        print(vege)



Algorythm()