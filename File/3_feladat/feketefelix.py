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

olvasas()
