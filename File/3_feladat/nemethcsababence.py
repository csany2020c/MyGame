import string
from typing import TextIO
from typing import List

class Adat:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.nev: str = str(fields[0])
        self.rajtszam: str = str(fields[1])
        self.kategoria: str = str(fields[2])
        self.idoeredmeny: str = str(fields[3])
        self.elertszazalek: str = str(fields[4])

    def __str__(self) -> str:
        return "nev = {x}; rajtszam = {y}; kategoria = {z}; idoeredmeny = {w}; elertszazalek = {e}".format(x=self.nev, y=self.rajtszam, z=self.kategoria, w = self.idoeredmeny, e=self.elertszazalek)


class Main:
    def __init__(self) -> None:
        super().__init__()

        f: TextIO = open("!_Specifikacio/ub2017egyeni.txt", "r", encoding="utf-8")
        content: str = f.read()
        sorok: List['str'] = content.split(sep="\n")
        adatlist: List['Adat'] = list()
        for i in range(1, len(sorok)-1):
            d = Adat(sorok[i])
            adatlist.append(d)
        f.close()
        #3.feladat
        print("3.feladat" + "----" + "egyeni indulok: {db} fő ".format(db=len(adatlist)))
        #4.feladat
        x = 0
        for index in range(0, len(adatlist)):
            if adatlist[index].kategoria == "Noi":
                x = x + 1
        print("4.feladat" + "----" + f"noi versenyzok szama : {x}")

        #5.feladat
        adat: str = input()
        tav: int = adatlist[index].elertszazalek * 100
        for index in range(0, len(adatlist)):
            if adatlist[index].nev == adat:
                print("5.feladat" + "----" + "resztvett a versenyen")
            if adatlist[index].elertszazalek <= tav:
                print({tav} + "km utat tett meg.")



Main()