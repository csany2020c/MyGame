#1.&2.feladat
import string
from typing import TextIO
from typing import List

class Data:

    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.versenyzo: str = str(fields[0])
        self.rajtszam: str = str(fields[1])
        self.kategoria: str = str(fields[2])
        self.versenyido: str = str(fields[3])
        self.tavszazalek: int = int(fields[4])

    def IdoOra(self) -> float:
        s: List['str'] = self.versenyido.split(":")
        return float(s[0]) + float(s[1])/60.0 + float(s[2])/3600.0

    def __str__(self) -> str:
        return "versenyzo = {x}; rajtszam = {y}; kategoria = {k}; versenyido = {v}; tavszazalek = {t}".format(x=self.versenyzo, y=self.rajtszam, k=self.kategoria, v=self.versenyido, t=self.tavszazalek)

class Main:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specifikacio/ub2017egyeni.txt", "r", encoding="utf-8")
        content: str = f.read()
        line: List['str'] = content.split(sep="\n")
        dataList: List['Data'] = list()
        for i in range(1, len(line)-1):
            d = Data(line[i])
            dataList.append(d)
        f.close()


        #3.feladat
        print("{db} egyéni sportoló indult el a versenyen. ".format(db=len(dataList)))

        #4.feladat
        kategoria: str = "Noi"
        tavszazalek: int = 100
        db: int = 0
        for index in range(0, len(dataList)):
            if dataList[index].kategoria == kategoria and dataList[index].tavszazalek == tavszazalek:
                db += 1
        print("{db} célba érkező női sportoló volt".format(db=db))

        #5.feladat

        #7.feladat
        osszeg: float = 0
        db: int = 0
        for b in dataList:
            if b.kategoria == "Ferfi" and b.tavszazalek == 100:
                db+=1
                osszeg+=b.IdoOra()
        print("Átlag {atl}".format(atl = osszeg / db))

        #8.feladat
        befutottNok: List['Data'] = list()
        befutottFerfiak: List['Data'] = list()
        for i in dataList:
            if i.kategoria == "Ferfi" and i.tavszazalek == 100:
                befutottFerfiak.append(i)
            if i.kategoria == "Noi" and i.tavszazalek == 100:
                befutottNok.append(i)

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


Main()