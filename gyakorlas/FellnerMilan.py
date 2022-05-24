import sys
from typing import TextIO, List


class Adat:
    def __init__(self,parseStr:str) -> None:
        super().__init__()
        fields:List['str'] = parseStr.strip().split(" ")
        self.ev: int = int(fields[0])
        self.het: int = int(fields[1])
        self.fordulo: int = int(fields[2])
        self.t13p1: int = int(fields[3])
        self.ny13p1: int = int(fields[4])
        self.eredmenyek: str = fields[5]

    def __str__(self) -> str:
        return str(self.ev)

    def osszespenz(self):
        return self.t13p1 * self.ny13p1


class Main:
    def __init__(self) -> None:
        super().__init__()
        file:TextIO = open("toto.txt","r")
        content:str = file.read()
        lines:List['str'] = content.strip().split("\n")
        hetek:List['Adat'] = list()
        # for i in lines:
        #     print(Adat(i))
        for i in lines:
            hetek.append(Adat(i))
        print("3.feladat:")
        print(len(lines))
        print("4.feladat:")
        telitali:int = 0
        for i in hetek:
            telitali+= i.t13p1
        print(telitali)
        print("5.feladat")
        print("Legnagyobb")
        legnagyobb:Adat = hetek[0]
        for i in hetek:
            if i.osszespenz() > legnagyobb.osszespenz():
                legnagyobb = i
        print(legnagyobb.ev)
        print(legnagyobb.het)
        print("Legkisebb")
        adatID:Adat = None
        for i in hetek:
            if  i.osszespenz() != 0 and i.osszespenz() < max:
                max = i.osszespenz()
                adatID = i
        print(max)
        print(adatID.ev)
        print(adatID.het)

Main()