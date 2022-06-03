from typing import List


class Hazi:
    def __init__(self) -> None:
        super().__init__()
        print("1. Feladat \n")
        szamok:List['int'] = list()
        szam1:int = self.checkint("Írj be egy számot: \n")
        szam2:int = self.checkint("Írj be egy számot: \n")
        szam3:int = self.checkint("Írj be egy számot: \n")
        szamok.append(szam1)
        szamok.append(szam2)
        szamok.append(szam3)
        max = szamok[0]
        for i in szamok:
            if i > max:
                max = i
        print(f"A Legnagyobb szám a(z) {max}")


    def checkint(self,text:str) -> int:
        while True:
            be: str = input(text)
            try:
                szam:int = int(be)
                return szam
            except:
                pass




Hazi()