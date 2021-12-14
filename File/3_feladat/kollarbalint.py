import string
from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.elso: str = fields[0]
        self.masodik: str = fields[1]
        self.harmadik: str = fields[2]
        self.negyedik: str = fields[3]
        self.otodik: int = int(fields[4])

    def IdoOra(self) -> float:
        s: List['str'] = self.negyedik.split(":")
        return float(s[0]) + float(s[1])/60.0 + float(s[2])/3600.0

    def __str__(self) -> str:
        return "a = {a}; b = {b}; c = {c}; d = {d}; e = {e}".format(a=self.elso, b=self.masodik, c=self.harmadik, d=self.negyedik, e=self.otodik)

class Main:

    def __init__(self) -> None:
        super().__init__()
        print("")
        print("Adatok:")
        f: TextIO = open("!_Specifikacio//ub2017egyeni.txt", "r")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(1, len(lines) - 0):
            d = Data(lines[i])
            datalist.append(d)

        for d in datalist:
            print(d)
        f.close()
        #3.Feladat
        print("")
        print("3.Feladat:")
        print("Egyéni indulók: {szam} fő ".format(szam=len(datalist)))

        #4.Feladat
        #print("")
        print("4.Feladat:")
        fo: int = 0
        for i in range(0, len(datalist)):
            if datalist[i].harmadik == "Noi" and datalist[i].otodik == 100:
                fo += 1
        print("4. Célba érkező női sportolók: {fo} fő ".format(fo=fo))

        # print(datalist[2].elso)
        # print(datalist[2].IdoOra())

        osszeg: float = 0
        db: int = 0
        for i in datalist:
            if i.harmadik == "Ferfi" and i.otodik == 100:
                db += 1
                osszeg += i.IdoOra()
        print("Átlag {atl}".format(atl = osszeg / db))

        # noiMinIndex: int = 0
        # ferfiMinIndex: int = 0
        befutottNok: List['Data'] = list()
        befutottFerfiak: List['Data'] = list()
        for i in datalist:
            if i.harmadik == "Ferfi" and i.otodik == 100:
                befutottFerfiak.append(i)
            if i.harmadik == "Noi" and i.otodik == 100:
                befutottNok.append(i)

        # for i in befutottNok:
        #     print(i)

        minIndex = 0
        for i in range(1, len(befutottNok)):
            if befutottNok[minIndex].IdoOra() > befutottNok[i].IdoOra():
                minIndex = i
        print("Győztes: {gy}".format(gy=befutottNok[minIndex]))


        minIndex = 0
        for i in range(1, len(befutottFerfiak)):
            if befutottFerfiak[minIndex].IdoOra() > befutottFerfiak[i].IdoOra():
                minIndex = i
        print("Győztes: {gy}".format(gy=befutottFerfiak[minIndex]))

        #5.Feladat
        #print("")
        #print("5.Feladat:")

Main()