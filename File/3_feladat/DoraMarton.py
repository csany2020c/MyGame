from typing import TextIO
from typing import List

class Data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.versenyzo: str = (fields[0])
        self.rajtszam: str = fields[1]
        self.kategoria: str = fields[2]
        self.versenyido: str = fields[3]
        self.tavszazalek: str = fields[4]

    def IdoOra(self) -> float:
        s: List['str'] = self.versenyido.split(":")
        return float(s[0]) + float(s[1])/60.0 + float(s[2])/3600.0

    def __str__(self) -> str:
        return "{v}, {r}, {k}, {vi}, {t}".format(v=self.versenyzo, r=self.rajtszam, k=self.kategoria, vi=self.versenyido, t=self.tavszazalek)

class bajvanhelp:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specifikacio/ub2017egyeni.txt", encoding="utf-8")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(1, len(lines) - 1):
            d = Data(lines[i])
            datalist.append(d)
            #print(d)

        f.close()

        print("Egyeniek: {db}".format(db=len(datalist)))

        nok: str = "Noi"
        no: int = 0
        tavolsag: str = "100"
        for index in range(0, len(datalist)):
            if datalist[index].tavszazalek == tavolsag and datalist[index].kategoria == nok:
                no += 1
        print("Noi sportolok: {db}".format(db=no))

        osszeg: float = 0
        db: int = 1
        for i in datalist:
            if i.kategoria == "Ferfi" and i.tavszazalek == 100:
                db += 1
                osszeg += i.IdoOra()
        print("Átlag {atl}".format(atl=osszeg / db))

        befutottNok: List['Data'] = list()
        befutottFerfiak: List['Data'] = list()
        for i in datalist:
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


bajvanhelp()