class Algorythm:
    def __init__(self) -> None:
        super().__init__()
        szam:str = input()
        intszam:int = int(szam)
        max: int = int(512)
        vege: str = str()
        for i in range(9):
            max = int(max/2)
            if (max <= intszam):
                vege += "1"
                intszam -= max
            else:
                vege += "0"
        print(vege)



Algorythm()