from typing import List
from typing import TextIO


class Data:
    def __init__(self, parseString: str) -> None:
        super().__init__()
        fields: List['str'] = parseString.split(";")
        self.versenyzo: str = fields[0]
        self.rajtszam: int = int(fields[1])
        self.kategoria: str = fields[2]
        self.versenyido: str = fields[3]
        self.tavszazalek: int = int(fields[4])

# 6.feladat
    def IdoOra(self) -> float:
            s: List['str'] = self.versenyido.split(";")
            return float(s[0]) + float(s[1]) / 60.0 + float(s[2]) / 3600.0

    def __str__(self) -> str:
        return "versenyzo = {a}; rajtszam = {b}; kategoria = {c}; versenyido = {d}; tavszazalek = {f}".format(a=self.versenyzo, b=self.rajtszam, c=self.kategoria, d=self.versenyido, f=self.tavszazalek)


class olvasas:
    def __init__(self) -> None:
        super().__init__()
        f: TextIO = open("!_Specifikacio/ub2017egyeni.txt", "r")
        content: str = f.read()
        lines: List['str'] = content.split(sep="\n")
        datalist: List['Data'] = list()
        for i in range(1, len(lines)):
            d = Data(lines[i])
            datalist.append(d)
#3.feladat
        print("3. feladat: Egyéni indulók: {db} fő ".format(db=len(datalist)))

#4.feladat
        no: int = 0
        noi: str = "Noi"
        for i in range(1, len(datalist)):
            if datalist[i].kategoria == noi and datalist[i].tavszazalek == 100:
                no += 1
        print("4. feladat: Célba érkező női sportolók száma: {no} fő".format(no=no))

#5.feladat
        versenev = input("5.feladat: Kérem a sportoló nevét: ")
        indul: str = "Nem"
        tav: str = "Nem"
        for x in range(1, len(datalist)):
            if datalist[x].versenyzo == versenev:
                indul = "Igen"
            if datalist[x].tavszazalek == 100 and datalist[x].versenyzo == versenev:
                tav = "Igen"
        print("Indult egyéniben a sportoló? {indul}".format(indul=indul))
        print("Teljesítette a teljes távot? {tav}".format(tav=tav))

#7.feladat
        osszeg: float = 0
        darab = int = 0
        for i in datalist:
            if i.versenyido == "Ferfi" and i.tavszazalek == "100" :
                darab+=1
                osszeg+=i.IdoOra()
        print("Átlag {atlg}".format(atlg = osszeg /darab))

#8.feladat
        befutottferfi: List['Data'] = list()
        befutottno: List['Data'] = list()
        for i in datalist:
            if i.versenyido == "Ferfi" and i.tavszazalek == 100:
                befutottferfi.append(i)
            if i.versenyido == "Noi" and i.tavszazalek == 100:
                befutottno.append(i)

        minIndex = 0
        for i in range(1, len(befutottno)):
            if befutottno[minIndex].IdoOra() > befutottno[i].IdoOra():
                minIndex = i
        print("Győztes: {gy}".format(gy=befutottno[minIndex]))
        minIndex = 0
        for i in range(1, len(befutottferfi)):
            if befutottferfi[minIndex].IdoOra() > befutottferfi[i].IdoOra():
                minIndex = i
        print("Győztes: {gy}".format(gy=befutottferfi[minIndex]))






olvasas()
